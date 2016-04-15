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
        if len(metadata_xml.getchildren())<1:
            return None

        temp_dict = {}
        for element in metadata_xml.getchildren():
            temp_dict[element.tag]=element.text
        return temp_dict