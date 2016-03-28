import json
from urllib2 import HTTPError

from eurekalab.exceptions import *
from eurekalab.tools import requests
from eurekalab.tools.eureka_xml_parser import EurekaXMLParser


class EurekaClient(object):

    def __init__(self, eureka_server_properties, my_service_properties=None):
        super(EurekaClient, self).__init__()
        self.eureka = eureka_server_properties
        self.app = my_service_properties
        self.__service_only = self.app is None
        self.__check_data_integrity(self.__service_only)
        self.__build_spring_style_metadata_instance_id()

    def __check_data_integrity(self, client_only=False):
        self.__check_mandatory_fields(client_only)
        self.__check_data_center()

    def __check_data_center(self):
        dc = self.eureka.data_center;
        valid = ["MyOwn", "Netflix", "Amazon",u"MyOwn", u"Netflix", u"Amazon"]

        if dc not in valid:
            raise BadDataCenterException()
        elif dc == "NetFlix" or dc == u"Netflix":
            raise DatacenterNotSupportedYetException();
        elif dc == "Amazon" or dc == u"Amazon":
            raise DatacenterNotSupportedYetException();

    def __check_mandatory_fields(self, client_only=False):
        app_complete = EurekaClient.__object_has_all_this_properties_non_none(
                self.app, constants.mandatory_app_fields
        )
        if app_complete is False and client_only is False:
            raise MandatoryAppFields()

        server_complete = EurekaClient.__object_has_all_this_properties_non_none(
                self.eureka, constants.mandatory_server_fields
        )
        if server_complete is False:
            raise MandatoryEurekaServerFields()

    def __build_spring_style_metadata_instance_id(self):
        self.app.metadata_dicc = {
            "instanceId":"%s:%d"%(self.app.app_name, self.app.port)
        }

    def register(self, status="STARTING"):
        try:
            response = requests.post(
                self._get_app_url(),
                self._get_register_body_data(),
                headers=self._get_default_header()
            )

            response.raise_for_status()
        except HTTPError as e:
            raise e

    def de_register(self):
        try:
            response = requests.delete(self._get_instace_url())
            response.raise_for_status()
        except HTTPError as e:
            raise e

    def heartbeat(self):
        try:
            response = requests.put(self._get_instace_url())
            response.raise_for_status()
        except HTTPError as e:
            raise e

    def get_all_instaces_of_app(self, app_name=None):
        result = None
        try:
            response = requests.get(self._get_app_url(app_name))
            result = EurekaXMLParser.parse_all_instances_of_app_string(response.content)
            response.raise_for_status()
        except Exception as e:
            raise e
        finally:
            return result

    def get_all_instaces(self):
        result = None
        try:
            response = requests.get(self._get_all_apps_url())
            result = EurekaXMLParser.parse_all_instances_string(response.content)
            response.raise_for_status()
        except HTTPError as e:
            raise e
        finally:
            return result

    def take_out_of_service(self):
        try:
            response = requests.put(self._get_out_of_service_full_url)
            response.raise_for_status()
        except HTTPError as e:
            raise e

    def take_back_to_service(self):
        try:
            response = requests.put(self._get_back_to_service_full_url())
            response.raise_for_status()
        except HTTPError as e:
            raise e

    def update_metadata(self, key, value):
        try:
            response = requests.put(self._get_update_metada_url(key, value))
            response.raise_for_status()
        except HTTPError as e:
            raise e
        pass

##DC:==========================================================================
##DC: URL, BODY AND HEADER GENERATION
##DC:==========================================================================
    def _get_app_url(self, app_name=None):
        if app_name is None:
            app_name = self.app.app_name
        return self._get_all_apps_url() + "/%s" % app_name

    def _get_instace_url(self):
        if self.__does_the_instance_have_intance_id_field_in_metadata():
            path = "/%s:%s" %(
                self.app.host_name, self.app.metadata_dicc["instanceId"]
            )
        else:
            path = "/%s" % self.app.host_name

        return self._get_app_url()+path

    def __does_the_instance_have_intance_id_field_in_metadata(self):

        return self.app.metadata_dicc is not None and \
            self.app.metadata_dicc.get("instanceId",None) is not None


    def _build_base_url(self):
        return self.eureka.eureka_url + ":%d/"%self.eureka.eureka_port + \
               self.eureka.endpoint

    def _get_register_body_data(self):
        data = {
            ## Esto es lo que publicas en Eureka si no estamos en EC2
            'instance': {
                'hostName': self.app.host_name,
                'app': self.app.app_name,
                'vipAddress': self.app.vip_address or '',
                'secureVipAddress': self.app.secure_vip_address or '',
                'status': self.app.status,
                'port': self.app.port,
                'securePort': self.app.secure_port,
                'dataCenterInfo': {
                    'name': self.eureka.data_center
                },
                'ipAddr':self.app.ip_addr,
                "homePageUrl": self.app.home_page_url, # Opcional
                "healthCheckUrl":self.app.health_check_url,
                "statusPageUrl":self.app.status_page_url,
                "metadata":self.app.metadata_dicc
            }
        }

        return json.dumps(data)

    def _get_default_header(self):
        return {'Content-Type': 'application/json'}

    def _get_out_of_service_full_url(self):
        return self._get_instace_url() + "/status?value=OUT_OF_SERVICE"

    def _get_back_to_service_full_url(self):
        return self._get_instace_url() + "/status?value=UP"

    def _get_update_metada_url(self,key, value):
        return self._get_instace_url() + "/metadata?%s=%s"%(key, value)

    def _get_all_apps_url(self):
        return self._build_base_url() + "/apps"

    @staticmethod
    def __object_has_all_this_properties_non_none(object, properties_list):
        for property in properties_list:
            try:
                a = getattr(object, property)
            except Exception, e:
                a = None
            finally:
                if a is None:
                    return False
        return True