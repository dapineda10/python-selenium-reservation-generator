import json
import random

import requests


class MockarooRequest:

    def postRequest(self, schema, num_rows_to_generate):
        mockaroo_url = 'https://api.mockaroo.com/api/generate.json'
        mockaroo_key = '82912180'
        url = mockaroo_url + '?key=' + mockaroo_key + '&count=' + str(num_rows_to_generate) + '&schema=' + schema
        response = requests.post(url)
        json_response = json.loads(response.content)
        return json_response

    def GetLoginData(self):
        return self.postRequest('Schema000004', '1')

    def GetDataSearchOneRoomOnePassengerTravelIt(self):
        return self.postRequest('Schema000010', '1')

    def GetNetNFFPassengersData(self):
        return self.postRequest('Schema000001', '1')

    def GetNetNFFUPaymentData(self):
        return self.postRequest('Schema000003', '1')

    def GetDataSearchOneRoomTwoPassengersTravelIt(self):
        return self.postRequest('Schema000011', '1')

    def GetDataSearchOneRoomTwoPassengersOneChildrenTravelIt(self):
        return self.postRequest('Schema000012', '1')

    def GetDataSearchTwoRoomOnePassengerTwoPassengersOneChildrenTravelIt(self):
        return self.postRequest('Schema000013', '1')

    def GetDataQuestionExtraPassenger(self):
        return self.postRequest('Schema000014', '1')

    def GetDocumentPassenger(self):
        return str(random.randint(1000000, 2000000))
