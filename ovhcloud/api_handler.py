import json
import requests
import ovhcloud

from ovh import Client as OvhClient

# This class is used to store the clients request values
# @url : The requested url (ex : /me/accessRestriction/enable)
# @method : The REST method type (ex: POST)
# @data : Data for REST
class OVH_Request(object):
    def __init__(self, cli_req, rest_method,request_data):
        self._url = cli_req
        self._method = rest_method
        self._data = request_data

    @property
    def url(self):
        return self._url

    @property
    def method(self):
        return self._method

    @property
    def data(self):
        return self._data


class Api_Handler(object):
    def __init__(self, api_data, ovh_client: OvhClient):
        self._api_data = api_data
        self._ovh_client = ovh_client

    def request(self):
        print("Request")

        response = OVH_AllApis(ovhcloud.OVH_API_URL + self._api_data['path'] + '.json')

        #TODO Only works on basic apis for now
        #response = self._ovh_client.get(self._api_data['path'])
        print(response)




def OVH_AllApis(ovh_url):
    # Get the list of primary OVH api's
    request_data = requests.get(url=ovh_url)
    return json.loads(request_data.text)