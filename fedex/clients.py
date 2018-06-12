from zeep import Client


class WebWervices(object):

    @classmethod
    def get_country_service_client(cls):
        return Client("./wsdls/web_services/CountryService_v6.wsdl")

    @classmethod
    def get_location_service_client(cls):
        return Client("./wsdls/web_services/LocationService_v7.wsdl")

    @classmethod
    def get_rate_service_client(cls):
        return Client("./wsdls/web_services/RateService_v22.wsdl")

    @classmethod
    def get_track_service_client(cls):
        return Client("./wsdls/web_services/TrackServie_v14.wsdl")

    @classmethod
    def get_validation_client(cls):
        return Client("./wsdls/web_services/ValidationAvailabilityAndCommitmentService_v8.wsdl")
