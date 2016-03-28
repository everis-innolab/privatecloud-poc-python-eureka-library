from eurekalab import constants


class BadDataCenterException(Exception):
    def __init__(self):
        message = 'data_center should be "MyOwn", "Netflix", or "Amazon"'
        super(BadDataCenterException, self).__init__(message)


class DatacenterNotSupportedYetException(Exception):
    def __init__(self):
        message = '"Netflix" and "Amazon datacenter are no supported yet"'
        super(DatacenterNotSupportedYetException, self).__init__(message)

class MandatoryAppFields(Exception):
    def __init__(self):
        message = 'The following fields are mandatory for the app properties ' \
                  ': %s'%", ".join(constants.mandatory_app_fields)
        super(MandatoryAppFields, self).__init__(message)


class MandatoryEurekaServerFields(Exception):
    def __init__(self):
        message = 'The following fields are mandatory for the eureka server ' \
                  'properties : %s'%", ".join(constants.mandatory_server_fields)
        super(MandatoryEurekaServerFields, self).__init__(message)