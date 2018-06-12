import os
from zeep import Client


class TrackServiceClient(object):

    def __init__(self, key, password, account_number, meter_number):
        wsdl_path = os.path.join(
            os.path.dirname(__file__),
            "wsdls",
            "web_services",
            "TrackService_v14.wsdl"
        )
        self.client = Client(wsdl_path)
        self.key = key
        self.password = password
        self.account_number = account_number
        self.meter_number = meter_number

    def track_by_tracking_number_or_doortag(self, tracking_number_or_doortag):
        track_request_dict = {
            'WebAuthenticationDetail': {
                'UserCredential': {
                    'Key': self.key,
                    'Password': self.password,
                }
            },
            'ClientDetail': {
                'AccountNumber': self.account_number,
                'MeterNumber': self.meter_number,
            },
            'TransactionDetail': {
                'CustomerTransactionId': 'Track By Number_v14',
                'Localization': {
                    'LanguageCode': 'EN',
                    'LocaleCode': 'US'
                }
            },
            'Version': {
                'ServiceId': 'trck',
                'Major': '14',
                'Intermediate': '0',
                'Minor': '0'
            },
            'SelectionDetails': {
                'CarrierCode': 'FDXE',
                'PackageIdentifier': {
                    'Type': 'TRACKING_NUMBER_OR_DOORTAG',
                    'Value': tracking_number_or_doortag,
                },
            },
        }
        return self.client.service.track(**track_request_dict)
