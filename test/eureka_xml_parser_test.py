import unittest
import xml
from eurekalab.model.app_instance_dto import AppInstanceDTO
from eurekalab.tools.eureka_xml_parser import EurekaXMLParser


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.single_instance_with_metadata ="""
            <instance>
                <hostName>localhost1</hostName>
                <app>MOCKAPP</app>
                <ipAddr>80.80.80.82</ipAddr>
                <status>STARTING</status>
                <overriddenstatus>UNKNOWN</overriddenstatus>
                <port enabled="true">9991</port>
                <securePort enabled="false">443</securePort>
                <countryId>1</countryId>
                <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                    <name>MyOwn</name>

                </dataCenterInfo>
                <leaseInfo>
                    <renewalIntervalInSecs>30</renewalIntervalInSecs>
                    <durationInSecs>90</durationInSecs>
                    <registrationTimestamp>1456760023620</registrationTimestamp>
                    <lastRenewalTimestamp>1456760023620</lastRenewalTimestamp>
                    <evictionTimestamp>0</evictionTimestamp>
                    <serviceUpTimestamp>0</serviceUpTimestamp>
                </leaseInfo>
                <metadata>
                    <instanceId>MockApp:9991</instanceId>

                </metadata>
                <homePageUrl>localhost</homePageUrl>
                <statusPageUrl>localhost</statusPageUrl>
                <healthCheckUrl>localhost</healthCheckUrl>
                <vipAddress>app.yourdomain.net</vipAddress>
                <secureVipAddress>25.25.25.25</secureVipAddress>
                <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                <lastUpdatedTimestamp>1456760023620</lastUpdatedTimestamp>
                <lastDirtyTimestamp>1456760022937</lastDirtyTimestamp>
                <actionType>ADDED</actionType>
            </instance>
        """

        self.parsed_single_instance_with_metadata = \
            xml.etree.ElementTree.XML(self.single_instance_with_metadata)

        self.single_instance_with_metadata_dto = AppInstanceDTO(
            vip_address="app.yourdomain.net",
            secure_vip_address="25.25.25.25",
            port=9991,
            host_name="localhost1",
            secure_port=443,
            ip_addr="80.80.80.82",
            home_page_url="localhost",
            health_check_url="localhost",
            status_page_url="localhost",
            status="STARTING",
            app_name="MOCKAPP",
            metadata_dicc={"instanceId":"MockApp:9991"}
        )

        self.all_instances_of_app_id_with_metadata = """
            <application>
                <name>MOCKAPP</name>
                <instance>
                    <hostName>localhost2</hostName>
                    <app>MOCKAPP</app>
                    <ipAddr>80.80.80.82</ipAddr>
                    <status>STARTING</status>
                    <overriddenstatus>UNKNOWN</overriddenstatus>
                    <port enabled="true">9992</port>
                    <securePort enabled="false">443</securePort>
                    <countryId>1</countryId>
                    <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                        <name>MyOwn</name>

                    </dataCenterInfo>
                    <leaseInfo>
                        <renewalIntervalInSecs>30</renewalIntervalInSecs>
                        <durationInSecs>90</durationInSecs>
                        <registrationTimestamp>1456761194262</registrationTimestamp>
                        <lastRenewalTimestamp>1456761194262</lastRenewalTimestamp>
                        <evictionTimestamp>0</evictionTimestamp>
                        <serviceUpTimestamp>0</serviceUpTimestamp>

                    </leaseInfo>
                    <metadata>
                        <instanceId>MockApp:9992</instanceId>

                    </metadata>
                    <homePageUrl>localhost</homePageUrl>
                    <statusPageUrl>localhost</statusPageUrl>
                    <healthCheckUrl>localhost</healthCheckUrl>
                    <vipAddress>app.yourdomain.net</vipAddress>
                    <secureVipAddress>25.25.25.25</secureVipAddress>
                    <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                    <lastUpdatedTimestamp>1456761194262</lastUpdatedTimestamp>
                    <lastDirtyTimestamp>1456761193912</lastDirtyTimestamp>
                    <actionType>ADDED</actionType>

                </instance>
                <instance>
                    <hostName>localhost1</hostName>
                    <app>MOCKAPP</app>
                    <ipAddr>80.80.80.82</ipAddr>
                    <status>STARTING</status>
                    <overriddenstatus>UNKNOWN</overriddenstatus>
                    <port enabled="true">9991</port>
                    <securePort enabled="false">443</securePort>
                    <countryId>1</countryId>
                    <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                        <name>MyOwn</name>

                    </dataCenterInfo>
                    <leaseInfo>
                        <renewalIntervalInSecs>30</renewalIntervalInSecs>
                        <durationInSecs>90</durationInSecs>
                        <registrationTimestamp>1456761185660</registrationTimestamp>
                        <lastRenewalTimestamp>1456761185660</lastRenewalTimestamp>
                        <evictionTimestamp>0</evictionTimestamp>
                        <serviceUpTimestamp>0</serviceUpTimestamp>

                    </leaseInfo>
                    <metadata>
                        <instanceId>MockApp:9991</instanceId>

                    </metadata>
                    <homePageUrl>localhost</homePageUrl>
                    <statusPageUrl>localhost</statusPageUrl>
                    <healthCheckUrl>localhost</healthCheckUrl>
                    <vipAddress>app.yourdomain.net</vipAddress>
                    <secureVipAddress>25.25.25.25</secureVipAddress>
                    <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                    <lastUpdatedTimestamp>1456761185661</lastUpdatedTimestamp>
                    <lastDirtyTimestamp>1456761184851</lastDirtyTimestamp>
                    <actionType>ADDED</actionType>

                </instance>
                <instance>
                    <hostName>localhost3</hostName>
                    <app>MOCKAPP</app>
                    <ipAddr>80.80.80.82</ipAddr>
                    <status>STARTING</status>
                    <overriddenstatus>UNKNOWN</overriddenstatus>
                    <port enabled="true">9993</port>
                    <securePort enabled="false">443</securePort>
                    <countryId>1</countryId>
                    <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                        <name>MyOwn</name>

                    </dataCenterInfo>
                    <leaseInfo>
                        <renewalIntervalInSecs>30</renewalIntervalInSecs>
                        <durationInSecs>90</durationInSecs>
                        <registrationTimestamp>1456761200766</registrationTimestamp>
                        <lastRenewalTimestamp>1456761200766</lastRenewalTimestamp>
                        <evictionTimestamp>0</evictionTimestamp>
                        <serviceUpTimestamp>0</serviceUpTimestamp>

                    </leaseInfo>
                    <metadata>
                        <instanceId>MockApp:9993</instanceId>

                    </metadata>
                    <homePageUrl>localhost</homePageUrl>
                    <statusPageUrl>localhost</statusPageUrl>
                    <healthCheckUrl>localhost</healthCheckUrl>
                    <vipAddress>app.yourdomain.net</vipAddress>
                    <secureVipAddress>25.25.25.25</secureVipAddress>
                    <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                    <lastUpdatedTimestamp>1456761200766</lastUpdatedTimestamp>
                    <lastDirtyTimestamp>1456761200458</lastDirtyTimestamp>
                    <actionType>ADDED</actionType>

                </instance>
            </application>
        """
        self.all_instances_of_app_id_with_metadata_dto_list = [
            AppInstanceDTO(
                vip_address="app.yourdomain.net",
                secure_vip_address="25.25.25.25",
                port=9991,
                host_name="localhost1",
                secure_port=443,
                ip_addr="80.80.80.82",
                home_page_url="localhost",
                health_check_url="localhost",
                status_page_url="localhost",
                status="STARTING",
                app_name="MOCKAPP",
                metadata_dicc={"instanceId":"MockApp:9991"}
            ),
            AppInstanceDTO(
                vip_address="app.yourdomain.net",
                secure_vip_address="25.25.25.25",
                port=9992,
                host_name="localhost2",
                secure_port=443,
                ip_addr="80.80.80.82",
                home_page_url="localhost",
                health_check_url="localhost",
                status_page_url="localhost",
                status="STARTING",
                app_name="MOCKAPP",
                metadata_dicc={"instanceId":"MockApp:9992"}
            ),
            AppInstanceDTO(
                vip_address="app.yourdomain.net",
                secure_vip_address="25.25.25.25",
                port=9993, #De mi app
                host_name="localhost3",
                secure_port=443, #De mi app
                ip_addr="80.80.80.82",
                home_page_url="localhost",
                health_check_url="localhost",
                status_page_url="localhost",
                status="STARTING",
                app_name="MOCKAPP",
                metadata_dicc={"instanceId":"MockApp:9993"}
            )
        ]



        self.all_instances_with_metadata = """
            <applications>
                <versions__delta>1</versions__delta>
                <apps__hashcode>STARTING_2_</apps__hashcode>
                <application>
                    <name>PYTHONAPP</name>
                    <instance>
                        <hostName>localhost2</hostName>
                        <app>PYTHONAPP</app>
                        <ipAddr>80.80.80.82</ipAddr>
                        <status>STARTING</status>
                        <overriddenstatus>UNKNOWN</overriddenstatus>
                        <port enabled="true">9992</port>
                        <securePort enabled="false">443</securePort>
                        <countryId>1</countryId>
                        <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                            <name>MyOwn</name>

                        </dataCenterInfo>
                        <leaseInfo>
                            <renewalIntervalInSecs>30</renewalIntervalInSecs>
                            <durationInSecs>90</durationInSecs>
                            <registrationTimestamp>1456761644385</registrationTimestamp>
                            <lastRenewalTimestamp>1456761644385</lastRenewalTimestamp>
                            <evictionTimestamp>0</evictionTimestamp>
                            <serviceUpTimestamp>0</serviceUpTimestamp>

                        </leaseInfo>
                        <metadata>
                            <instanceId>PythonApp:9992</instanceId>

                        </metadata>
                        <homePageUrl>localhost</homePageUrl>
                        <statusPageUrl>localhost</statusPageUrl>
                        <healthCheckUrl>localhost</healthCheckUrl>
                        <vipAddress>app.yourdomain.net</vipAddress>
                        <secureVipAddress>25.25.25.25</secureVipAddress>
                        <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                        <lastUpdatedTimestamp>1456761644385</lastUpdatedTimestamp>
                        <lastDirtyTimestamp>1456761644035</lastDirtyTimestamp>
                        <actionType>ADDED</actionType>

                    </instance>

                </application>
                <application>
                    <name>MOCKAPP</name>
                    <instance>
                        <hostName>localhost1</hostName>
                        <app>MOCKAPP</app>
                        <ipAddr>80.80.80.82</ipAddr>
                        <status>STARTING</status>
                        <overriddenstatus>UNKNOWN</overriddenstatus>
                        <port enabled="true">9991</port>
                        <securePort enabled="false">443</securePort>
                        <countryId>1</countryId>
                        <dataCenterInfo class="com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo">
                            <name>MyOwn</name>

                        </dataCenterInfo>
                        <leaseInfo>
                            <renewalIntervalInSecs>30</renewalIntervalInSecs>
                            <durationInSecs>90</durationInSecs>
                            <registrationTimestamp>1456761633802</registrationTimestamp>
                            <lastRenewalTimestamp>1456761633802</lastRenewalTimestamp>
                            <evictionTimestamp>0</evictionTimestamp>
                            <serviceUpTimestamp>0</serviceUpTimestamp>

                        </leaseInfo>
                        <metadata>
                            <instanceId>MockApp:9991</instanceId>

                        </metadata>
                        <homePageUrl>localhost</homePageUrl>
                        <statusPageUrl>localhost</statusPageUrl>
                        <healthCheckUrl>localhost</healthCheckUrl>
                        <vipAddress>app.yourdomain.net</vipAddress>
                        <secureVipAddress>25.25.25.25</secureVipAddress>
                        <isCoordinatingDiscoveryServer>false</isCoordinatingDiscoveryServer>
                        <lastUpdatedTimestamp>1456761633802</lastUpdatedTimestamp>
                        <lastDirtyTimestamp>1456761633095</lastDirtyTimestamp>
                        <actionType>ADDED</actionType>

                    </instance>

                </application>
            </applications>
        """
        self.all_instances_with_metadata_dto_list = [
            AppInstanceDTO(
                vip_address="app.yourdomain.net",
                secure_vip_address="25.25.25.25",
                port=9991,
                host_name="localhost1",
                secure_port=443,
                ip_addr="80.80.80.82",
                home_page_url="localhost",
                health_check_url="localhost",
                status_page_url="localhost",
                status="STARTING",
                app_name="MOCKAPP",
                metadata_dicc={"instanceId":"MockApp:9991"}
            ),
            AppInstanceDTO(
                vip_address="app.yourdomain.net",
                secure_vip_address="25.25.25.25",
                port=9992,
                host_name="localhost2",
                secure_port=443,
                ip_addr="80.80.80.82",
                home_page_url="localhost",
                health_check_url="localhost",
                status_page_url="localhost",
                status="STARTING",
                app_name="PYTHONAPP",
                metadata_dicc={"instanceId":"PythonApp:9992"}
            ),
        ]

    def tearDown(self):
        pass

    def test_single_instace_parsing(self):
        instance_dto = EurekaXMLParser._parse_instance_xml(
            self.parsed_single_instance_with_metadata
        )
        self.assertEquals(self.single_instance_with_metadata_dto, instance_dto)

    def test_all_instances_of_app_parsing(self):
        instance_dto_list = EurekaXMLParser.parse_all_instances_of_app_string(
            self.all_instances_of_app_id_with_metadata
        )
        for expected in self.all_instances_of_app_id_with_metadata_dto_list:
            self.assertIn(expected, instance_dto_list)

    def test_all_instances_parsing(self):
        instance_dto_list = EurekaXMLParser.parse_all_instances_string(
            self.all_instances_with_metadata
        )
        for expected in self.all_instances_with_metadata_dto_list:
            self.assertIn(expected, instance_dto_list)

if __name__ == '__main__':
    unittest.main()