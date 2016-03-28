

class EurekaServerDTO(object):
    def __init__(self, eureka_url=None, eureka_domain_name=None,
                 data_center=None, use_dns=None, region=None,
                 prefer_same_zone=None, endpoint=None, eureka_port=None):
        self.__eureka_url = eureka_url
        self.__eureka_domain_name = eureka_domain_name
        self.__data_center = data_center
        self.__use_dns = use_dns
        self.__region = region
        self.__prefer_same_zone = prefer_same_zone
        self.__endpoint = endpoint
        self.__eureka_port = eureka_port

##DC:==========================================================================
##DC: GETTERS
##DC:==========================================================================

    @property
    def eureka_url(self):
        return self.__eureka_url

    @property
    def eureka_domain_name(self):
        return self.__eureka_domain_name

    @property
    def data_center(self):
        return self.__data_center

    @property
    def use_dns(self):
        return self.__use_dns

    @property
    def region(self):
        return self.__region

    @property
    def prefer_same_zone(self):
        return self.__prefer_same_zone

    @property
    def endpoint(self):
        return self.__endpoint

    @property
    def eureka_port(self):
        return self.__eureka_port

##DC:==========================================================================
##DC: SETTERS
##DC:==========================================================================

    @eureka_url.setter
    def eureka_url(self, eureka_url):
        self.__eureka_url = eureka_url

    @eureka_domain_name.setter
    def eureka_domain_name(self, eureka_domain_name):
        self.__eureka_domain_name = eureka_domain_name

    @data_center.setter
    def data_center(self, data_center):
        self.__data_center = data_center

    @use_dns.setter
    def use_dns(self, use_dns):
        self.__use_dns = use_dns

    @region.setter
    def region(self, region):
        self.__region = region

    @prefer_same_zone.setter
    def prefer_same_zone(self, prefer_same_zone):
        self.__prefer_same_zone = prefer_same_zone

    @endpoint.setter
    def endpoint(self, endpoint):
        self.__endpoint = endpoint

    @eureka_port.setter
    def eureka_port(self, eureka_port):
        self.__eureka_port = eureka_port

    def __eq__(self, other):
        return (
            self.eureka_url == other.eureka_url and
            self.eureka_domain_name == other.eureka_domain_name and
            self.data_center == other.data_center and
            self.use_dns == other.use_dns and
            self.region == other.region and
            self.prefer_same_zone == other.prefer_same_zone and
            self.endpoint == other.endpoint and
            self.eureka_port == other.eureka_port
        )

    def __str__(self):
        return (
            'eureka_url: str(%s)\n'%(self.__eureka_url)+
            'eureka_domain_name: str(%s)\n'%(self.__eureka_domain_name)+
            'data_center: str(%s)\n'%(self.__data_center)+
            'use_dns: str(%s)\n'%(self.__use_dns)+
            'region: str(%s)\n'%(self.__region)+
            'prefer_same_zone: str(%s)\n'%(self.__prefer_same_zone)+
            'endpoint: str(%s)\n'%(self.__endpoint)+
            'eureka_port: str(%s)\n'%(self.__eureka_port)
        )