class AppInstanceDTO(object):

    def __init__(self, app_name=None, host_name=None, vip_address=None,
                 secure_vip_address=None, port=None, secure_port=None,
                 ip_addr=None, home_page_url=None, health_check_url=None,
                 status_page_url=None, status="STARTING",
                 metadata_dicc=None):
        self.__app_name = app_name
        self.__host_name = host_name
        self.__vip_address = vip_address
        self.__secure_vip_address = secure_vip_address
        self.__port = port
        self.__secure_port = secure_port
        self.__ip_addr = ip_addr
        self.__home_page_url = home_page_url
        self.__health_check_url = health_check_url
        self.__status_page_url = status_page_url
        self.__status = status
        self.__metadata_dicc = metadata_dicc

##DC:==========================================================================
##DC: GETTERS
##DC:==========================================================================

    @property
    def app_name(self):
        return self.__app_name

    @property
    def host_name(self):
        return self.__host_name

    @property
    def vip_address(self):
        return self.__vip_address

    @property
    def secure_vip_address(self):
        return self.__secure_vip_address

    @property
    def port(self):
        return self.__port

    @property
    def secure_port(self):
        return self.__secure_port

    @property
    def ip_addr(self):
        return self.__ip_addr

    @property
    def home_page_url(self):
        return self.__home_page_url

    @property
    def health_check_url(self):
        return self.__health_check_url

    @property
    def status_page_url(self):
        return self.__status_page_url

    @property
    def status(self):
        return self.__status

    @property
    def metadata_dicc(self):
        return self.__metadata_dicc

##DC:==========================================================================
##DC: SETTERS
##DC:==========================================================================

    @app_name.setter
    def app_name(self, app_name):
        self.__app_name = app_name

    @host_name.setter
    def host_name(self, host_name):
        self.__host_name = host_name

    @vip_address.setter
    def vip_address(self, vip_address):
        self.__vip_address = vip_address

    @secure_vip_address.setter
    def secure_vip_address(self, secure_vip_address):
        self.__secure_vip_address = secure_vip_address

    @port.setter
    def port(self, port):
        self.__port = port

    @secure_port.setter
    def secure_port(self, secure_port):
        self.__secure_port = secure_port

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        self.__ip_addr = ip_addr

    @home_page_url.setter
    def home_page_url(self, home_page_url):
        self.__home_page_url = home_page_url

    @health_check_url.setter
    def health_check_url(self, health_check_url):
        self.__health_check_url = health_check_url

    @status_page_url.setter
    def status_page_url(self, status_page_url):
        self.__status_page_url = status_page_url

    @status.setter
    def status(self, status):
        self.__status = status

    @metadata_dicc.setter
    def metadata_dicc(self, metadata_dicc):
        self.__metadata_dicc = metadata_dicc

    def __eq__(self, other):
        return (
            self.app_name == other.app_name and
            self.host_name == other.host_name and
            self.vip_address == other.vip_address and
            self.secure_vip_address == other.secure_vip_address and
            self.port == other.port and
            self.secure_port == other.secure_port and
            self.ip_addr == other.ip_addr and
            self.home_page_url == other.home_page_url and
            self.health_check_url == other.health_check_url and
            self.status_page_url == other.status_page_url and
            self.status == other.status and
            self.metadata_dicc == other.metadata_dicc
        )

    def __str__(self):
        return (
            'app_name: %s\n'%str(self.__app_name)+
            'host_name: %s\n'%str(self.__host_name)+
            'vip_address: %s\n'%str(self.__vip_address)+
            'secure_vip_address: %s\n'%str(self.__secure_vip_address)+
            'port: %s\n'%str(self.__port)+
            'secure_port: %s\n'%str(self.__secure_port)+
            'ip_addr: %s\n'%str(self.__ip_addr)+
            'home_page_url: %s\n'%str(self.__home_page_url)+
            'health_check_url: %s\n'%str(self.__health_check_url)+
            'status_page_url: %s\n'%str(self.__status_page_url)+
            'status: %s\n'%str(self.__status)+
            'metadata_dicc: %s\n'%str(self.__metadata_dicc)
        )