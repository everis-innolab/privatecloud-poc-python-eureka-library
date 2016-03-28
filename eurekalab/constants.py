mandatory_app_fields = [
    "vip_address", "port","host_name","secure_port","ip_addr",
    "status_page_url","app_name"
]

mandatory_server_fields = [
    "eureka_url","eureka_domain_name", "data_center","eureka_port", "endpoint",
]


INSTANCE_XML_MAPPING = {
    "hostName": ("host_name","str"),
    "app": ("app_name","str"),
    "ipAddr": ("ip_addr","str"),
    "port": ("port","int"),
    "securePort": ("secure_port","int"),
    "homePageUrl": ("home_page_url","str"),
    "statusPageUrl": ("status_page_url","str"),
    "healthCheckUrl": ("health_check_url","str"),
    "status":("status","str"),
    "vipAddress":("vip_address","str"),
    "secureVipAddress":("secure_vip_address","str")
}

VERSION = "0.1.0"
