# -*- encoding: utf-8 -*-
import unittest

from eurekalab.client import EurekaClient
from eurekalab.exceptions import *
from eurekalab.model.app_instance_dto import AppInstanceDTO
from eurekalab.model.eureka_server_dto import EurekaServerDTO


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.eureka_server =  EurekaServerDTO(
            # eureka_url="http://asdf.com:8080/eureka/",
            eureka_url="http://192.168.1.41",
            eureka_domain_name="test.yourdomain.net",
            data_center="MyOwn",
            eureka_port=8080,
            endpoint="eureka"
        )

        self.my_app = AppInstanceDTO(
            vip_address="app.yourdomain.net",
            port=9999, #De mi app
            host_name="localhost",
            secure_port=443, #De mi app
            ip_addr="80.80.80.80",
            home_page_url="localhost",
            health_check_url="localhost",
            status_page_url="localhost",
            app_name="MockApp"
        )

    def tearDown(self):
        pass

    def test_is_subclass_of_abstract_classifier (self):
        self.assertTrue(issubclass(EurekaClient.__class__, object))

    def test_creation(self):
        a = EurekaClient(self.eureka_server, self.my_app)
        self.assertIsNotNone(a)

    def test_bad_or_unsupported_data_center_exception_raised(self):
        self.eureka_server.data_center="foofoo"
        self.assertRaises(
            BadDataCenterException, EurekaClient, self.eureka_server, self.my_app
        )

        self.eureka_server.data_center="Netflix"
        self.assertRaises(
            DatacenterNotSupportedYetException, EurekaClient,
            self.eureka_server, self.my_app
        )

        self.eureka_server.data_center=u"Netflix"
        self.assertRaises(
            DatacenterNotSupportedYetException, EurekaClient,
            self.eureka_server, self.my_app
        )

        self.eureka_server.data_center="Amazon"
        self.assertRaises(
            DatacenterNotSupportedYetException, EurekaClient,
            self.eureka_server, self.my_app
        )

        self.eureka_server.data_center=u"Amazon"
        self.assertRaises(
            DatacenterNotSupportedYetException, EurekaClient,
            self.eureka_server, self.my_app
        )


        self.eureka_server.data_center="MyOwn"
        a = EurekaClient(self.eureka_server, self.my_app)
        self.assertIsNotNone(a)

    def test_base_url_generation(self):
        a = EurekaClient(self.eureka_server, self.my_app)
        self.assertEquals("http://192.168.1.41:8080/eureka", a._build_base_url())


    def test_register_url_generation(self):
        a = EurekaClient(self.eureka_server, self.my_app)
        expected = "http://192.168.1.41:8080/eureka/apps/MockApp"
        self.assertEquals(expected, a._get_app_url())

##============================================================================
## Missing App properties
##============================================================================
    def test_vip_address_missing_raises_exception(self):
        self.my_app.vip_address = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

    def test_port_missing_raises_exception(self):
        self.my_app.port = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

    def test_host_name_missing_raises_exception(self):
        self.my_app.host_name = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

    def test_secure_port_missing_raises_exception(self):
        self.my_app.secure_port = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

    def test_ip_add_missing_raises_exception(self):
        self.my_app.ip_addr = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

    def test_status_page_url_missing_raises_exception(self):
        self.my_app.status_page_url = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

    def test_app_name_missing_raises_exception(self):
        self.my_app.app_name = None
        self.assertRaises(
            MandatoryAppFields, EurekaClient, self.eureka_server, self.my_app
        )

##============================================================================
## Missing Eureka server properties
##============================================================================
    def test_eureka_url_missing_raises_exception(self):
        self.eureka_server.eureka_url = None
        self.assertRaises(
            MandatoryEurekaServerFields, EurekaClient, self.eureka_server,
            self.my_app
        )

    def test_eureka_domain_name_missing_raises_exception(self):
        self.eureka_server.eureka_domain_name = None
        self.assertRaises(
            MandatoryEurekaServerFields, EurekaClient, self.eureka_server,
            self.my_app
        )

    def test_data_center_missing_raises_exception(self):
        self.eureka_server.data_center = None
        self.assertRaises(
            MandatoryEurekaServerFields, EurekaClient, self.eureka_server,
            self.my_app
        )

    def test_eureka_port_missing_raises_exception(self):
        self.eureka_server.eureka_port = None
        self.assertRaises(
            MandatoryEurekaServerFields, EurekaClient, self.eureka_server,
            self.my_app
        )

    def test_endpoint_missing_raises_exception(self):
        self.eureka_server.endpoint = None
        self.assertRaises(
            MandatoryEurekaServerFields, EurekaClient, self.eureka_server,
            self.my_app
        )

if __name__ == '__main__':
    unittest.main ()
