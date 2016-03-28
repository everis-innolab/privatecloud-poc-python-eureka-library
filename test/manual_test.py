import random

from eurekalab.client import EurekaClient
from eurekalab.model.app_instance_dto import AppInstanceDTO
from eurekalab.model.eureka_server_dto import EurekaServerDTO


eureka_server =  EurekaServerDTO(
    eureka_url="http://192.168.56.102",
    eureka_domain_name="test.yourdomain.net",
    data_center="MyOwn",
    eureka_port=8080,
    endpoint="eureka"
)

my_app = AppInstanceDTO(
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
    app_name="PythonApp",
    # metadata_dicc={"instanceId":random.randint(1,15000)}
)

ec = EurekaClient(eureka_server, my_app)

# print ec.register()
# ec.de_register()
# print ec.heartbeat()
# print ec.get_all_instaces_of_app("MockApp")
# ec.take_out_of_service()
# ec.take_back_to_service()
# ec.update_metadata("miCampo","33")
# print ec.get_all_instaces()

