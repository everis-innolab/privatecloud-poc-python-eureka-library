#==============================================================================
# NOTAS
#==============================================================================
Las pruebas se han realizado con el contenedor: springcloud/eureka
    docker run -t -i -p 8080:8761 springcloud/eureka

Tambien se realizaron otras antes con: netflixoss/eureka:1.1.142


Para consultar las apps registradas se hace un get al endpoint
    http://192.168.56.102:8080/eureka/apps


#==============================================================================
# CORRECCIONES NECESARIAS A HACERLE A LA LIBRERÍA
#==============================================================================

La librería de python-eureka no incluye todos estos campos. En concreto, faltan:

      "ipAddr":"80.80.80.80",
      "homePageUrl": "http://mrmx-everis:8001/",
      "healthCheckUrl":"http://mrmx-everis:8001/healthcheck",
      "statusPageUrl":"http://mrmx-everis:8001/Status"

Los valores que eureka springboot admite para el campo datacenterInfo son:

      "dataCenterInfo": {
         "name": "MyOwn" | "Netflix" | "Amazon"
      }

Ha habido tambien que modificar el requests para que ignore el proxy. Esto no
estoy seguro de si es

    eureka_properties_list = [
        "eureka_url", "eureka_domain_name", "data_center",
        "use_dns", "region", "prefer_same_zone",
        "endpoint", "eureka_port",
    ]
    
    my_service_properties_list = [
        "app_name","host_name","vip_address","secure_vip_address", "port",
        "secure_port", "ip_addr", "home_page_url","health_check_url",
        "status_page_url", "status"
    ]

https://github.com/Netflix/eureka/wiki/Eureka-REST-operations

appID is the name of the application and instanceID is the unique id 
associated with the instance. In AWS cloud, instanceID is the instance id of 
the instance and in other data centers, it is the hostname of the instance.


EUREKA no deja registrar dos instancias que tengan el mismo hostname!!! 
Es decir, no podemos tener dos servicios ejecutandos en el mismo nombre de 
host aunque tengan distintos puertos. Por este motivo es necesario asignar un 
campo en "metadata" con el nombre "instance_id" con un valor único. De esta 
forma podremos tener dos instancias en el mismo hostname.