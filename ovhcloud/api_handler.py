import json

import ovh as ovh
import requests

from ovh import Client as OvhClient
from errors import InternalError


# This class is used to store the clients request values
# @url : The requested url (ex : /me/accessRestriction/enable)
# @method : The REST method type (ex: POST)
# @data : Data for REST
class Ovh_Request(object):
    def __init__(self, cli_req, rest_method, request_data):
        self._url = self.build_url(cli_req)
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

    def build_url(self, cli_req):
        url = ''
        for url_part in cli_req:
            url += '/' + url_part

        return url


class Api_Handler(object):
    def __init__(self, ovh_client: OvhClient, request: Ovh_Request):
        self._ovh_request = request
        self._ovh_client = ovh_client

    def request(self):

        response = None

        # Handle specific treatment and generic exceptions (eg invalid URL)
        try:
            if (self._ovh_request.method == 'get'):
                response = self.launch_get()
            elif (self._ovh_request.method == 'post'):
                response = self.launch_post()
            elif (self._ovh_request.method == 'put'):
                response = self.launch_put()
            elif (self._ovh_request.method == 'delete'):
                response = self.launch_delete()
            else:
                raise InternalError('Invalid REST method')
        except ovh.exceptions.ResourceNotFoundError as e:
            print(str(e))
            print("Invalid URL: " + self._ovh_request.url)
            exit(1)

        self.printResult(response)

    def printResult(self, response):
        print(response)
        exit(0)

    # Specific treatment for GET
    def launch_get(self):
        response = self._ovh_client.get(self._ovh_request.url)

    # Specific treatment for POST
    def launch_post(self):
        response = self._ovh_client.post(self._ovh_request.url)

    # Specific treatment for PUT
    def launch_put(self):
        response = self._ovh_client.put(self._ovh_request.url)

    # Specific treatment for DELETE
    def launch_delete(self):
        response = self._ovh_client.delete(self._ovh_request.url)


def OVH_AllApis(ovh_url):
    # Get the list of primary OVH api's
    request_data = requests.get(url=ovh_url)
    return json.loads(request_data.text)
