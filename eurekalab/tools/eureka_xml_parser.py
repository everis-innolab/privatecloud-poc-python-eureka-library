import xml
from xml.etree.ElementTree import ElementTree
from eurekalab.constants import INSTANCE_XML_MAPPING
from eurekalab.model.app_instance_dto import AppInstanceDTO


class EurekaXMLParser():

    @staticmethod
    def parse_all_instances_string(xml_as_string):
        app_instance_dto_list = []
        document = xml.etree.ElementTree.XML(xml_as_string)

        for node in document.getchildren():
            if node.tag == 'application':
                temp_list = EurekaXMLParser.parse_all_instances_of_app_xml(node)
                if temp_list is not None:
                    app_instance_dto_list += temp_list

        if len(app_instance_dto_list)<1:
            app_instance_dto_list = None

        return app_instance_dto_list

    @staticmethod
    def parse_all_instances_of_app_string(xml_as_string):
        document = xml.etree.ElementTree.XML(xml_as_string)
        return EurekaXMLParser.parse_all_instances_of_app_xml(document)

    @staticmethod
    def parse_all_instances_of_app_xml(xml_document):
        app_instance_dto_list = []
        app_name = xml_document.find("name").text

        for node in xml_document.getchildren():
            if node.tag == 'instance':
                new_app_instance = EurekaXMLParser._parse_instance_xml(node)
                new_app_instance.app_name = app_name
                app_instance_dto_list.append(new_app_instance)

        if len(app_instance_dto_list)<1:
            app_instance_dto_list = None

        return app_instance_dto_list

    @staticmethod
    def _parse_instance_xml(instance_xml):
        instance_dto = AppInstanceDTO()
        for element in instance_xml.getchildren():
            if element.tag == "metadata":
                meta_dict = EurekaXMLParser.__parse_instance_metadata_into_dict(element)
                instance_dto.metadata_dicc = meta_dict

            else:
                mapping = INSTANCE_XML_MAPPING.get(element.tag, None)
                if mapping is not None:
                    if mapping[1] == "int":
                        value = int(element.text)
                    else:
                        value = element.text

                    setattr(instance_dto, mapping[0], value)
        return instance_dto

    @staticmethod
    def __parse_instance_metadata_into_dict(metadata_xml):
        """
        <metadata>
            <miCampo>33</miCampo>
        </metadata>
        :param metadata_xml:
        :return:
        """
        if len(metadata_xml.getchildren())<1:
            return None

        temp_dict = {}
        for element in metadata_xml.getchildren():
            temp_dict[element.tag]=element.text
        return temp_dict

if __name__ == "__main__":

    test_xml = """
        <application>
            <name>MOCKAPP</name>
            <instance>
                <hostName>localhost</hostName>
                <app>MOCKAPP</app>
                <ipAddr>80.80.80.82</ipAddr>
                <status>STARTING</status>
                <overriddenstatus>UNKNOWN</overriddenstatus>
                <port enabled="true">9999</port>
                <securePort enabled="false">443</securePort>
                <countryId>1</countryId>
                <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                    <name>MyOwn</name>
                </dataCenterInfo>
                <leaseInfo>
                    <renewalIntervalInSecs>30</renewalIntervalInSecs>
                    <durationInSecs>90</durationInSecs>
                    <registrationTimestamp>1456321574027</registrationTimestamp>
                    <lastRenewalTimestamp>1456321719072</lastRenewalTimestamp>
                    <evictionTimestamp>0</evictionTimestamp>
                    <serviceUpTimestamp>0</serviceUpTimestamp>

                </leaseInfo>
                <metadata>
                    <miCampo>33</miCampo>
                </metadata>
                <homePageUrl>localhost</homePageUrl>
                <statusPageUrl>localhost</statusPageUrl>
                <healthCheckUrl>localhost</healthCheckUrl>
                <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                <lastUpdatedTimestamp>1456321574027</lastUpdatedTimestamp>
                <lastDirtyTimestamp>1456321573803</lastDirtyTimestamp>
                <actionType>ADDED</actionType>

            </instance>
            <instance>
                <hostName>localhost2</hostName>
                <app>MOCKAPP</app>
                <ipAddr>80.80.80.82</ipAddr>
                <status>STARTING</status>
                <overriddenstatus>UNKNOWN</overriddenstatus>
                <port enabled="true">9999</port>
                <securePort enabled="false">443</securePort>
                <countryId>1</countryId>
                <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                    <name>MyOwn</name>

                </dataCenterInfo>
                <leaseInfo>
                    <renewalIntervalInSecs>30</renewalIntervalInSecs>
                    <durationInSecs>90</durationInSecs>
                    <registrationTimestamp>1456323845503</registrationTimestamp>
                    <lastRenewalTimestamp>1456323845503</lastRenewalTimestamp>
                    <evictionTimestamp>0</evictionTimestamp>
                    <serviceUpTimestamp>0</serviceUpTimestamp>

                </leaseInfo>
                <metadata class="java.util.Collections$EmptyMap"/>
                <homePageUrl>localhost</homePageUrl>
                <statusPageUrl>localhost</statusPageUrl>
                <healthCheckUrl>localhost</healthCheckUrl>
                <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                <lastUpdatedTimestamp>1456323845503</lastUpdatedTimestamp>
                <lastDirtyTimestamp>1456323845207</lastDirtyTimestamp>
                <actionType>ADDED</actionType>

            </instance>
        </application>
    """
    parser = EurekaXMLParser()
    result = parser.parse_all_instances_of_app_xml(test_xml)
    print result

