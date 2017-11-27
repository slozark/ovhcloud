import json
import requests
import ovhcloud

from ovh import Client as OvhClient
from errors import InternalError

# This class is used to store the clients request values
# @url : The requested url (ex : /me/accessRestriction/enable)
# @method : The REST method type (ex: POST)
# @data : Data for REST
class OVH_Request(object):
    def __init__(self, cli_req, rest_method,request_data):
        self._url = cli_req
        self._method = rest_method.lower()
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
    def __init__(self, ovh_client: OvhClient, request : OVH_Request):
        self._ovh_request = request
        self._ovh_client = ovh_client

    def request(self):
        print('Request')

        response = None

        if(self._ovh_request.method == 'get'):
            response = self._ovh_client.get(self._ovh_request.url)
        elif(self._ovh_request.method == 'post'):
            response = self._ovh_client.post(self._ovh_request.url)
        elif(self._ovh_request.method == 'put'):
            response = self._ovh_client.put(self._ovh_request.url)
        elif(self._ovh_request.method == 'delete'):
            response = self._ovh_client.delete(self._ovh_request.url)
        else:
            raise InternalError('Invalid REST method')

        print(response)




def OVH_AllApis(ovh_url):
    # Get the list of primary OVH api's
    request_data = requests.get(url=ovh_url)
    return json.loads(request_data.text)