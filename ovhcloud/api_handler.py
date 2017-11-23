import json
import requests
import ovhcloud

from ovh import Client as OvhClient

class Api_Handler(object):
    def __init__(self, api_data, ovh_client: OvhClient):
        self._api_data = api_data
        self._ovh_client = ovh_client

    def request(self):
        print("Request")
        #TODO Only works on basic apis for now
        response = self._ovh_client.get(self._api_data['path'])
        print(response)




def OVH_AllApis():
    # Get the list of primary OVH api's
    request_data = requests.get(url=ovhcloud.OVH_API_URL)
    return json.loads(request_data.text)