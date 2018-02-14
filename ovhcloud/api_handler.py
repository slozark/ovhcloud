# -*- encoding: utf-8 -*-

import json

import ovh as ovh
import requests
import ovhcloud

from ovh import Client as OvhClient
from errors import InternalError


# This class is used to store the clients request values
# @cli_req : The requested url (ex : /me/accessRestriction/enable)
# @rest_method : The REST method type (ex: POST)
# @request_data : Data for REST (put/post)
# @show_info : flag asking for information
class Ovh_Request(object):
    def __init__(self, cli_req, show_info, rest_method, request_data):
        self._url = self.build_url(cli_req)
        self._show_info = show_info
        self._method = rest_method.lower()
        self._data = request_data

    @property
    def url(self):
        return self._url

    @property
    def showInfo(self):
        return self._show_info

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

        # If the user asked for information, only display that information
        if (self._ovh_request.showInfo):
            print(self.display_info())
            exit(0)

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
        except ovh.exceptions.BadParametersError as e:
            print(str(e))
            print("See the list of properties for this API below :\n" + showApiArguments(self._ovh_request.url,
                                                                                         self._ovh_request.method))
            exit(1)

        self.printResult(response)

    def printResult(self, response):
        print(response)
        exit(0)

    # Specific treatment for GET
    def launch_get(self):
        return self._ovh_client.get(self._ovh_request.url)

    # Specific treatment for POST
    def launch_post(self):
        return self._ovh_client.post(self._ovh_request.url, **self._ovh_request.data)

    # Specific treatment for PUT
    def launch_put(self):
        return self._ovh_client.put(self._ovh_request.url, **self._ovh_request.data)

    # Specific treatment for DELETE
    def launch_delete(self):
        return self._ovh_client.delete(self._ovh_request.url)

    # Based on the command line provided, the displayed information changes
    def display_info(self):
        #TODO differenciate complete URLs from partial ones
        return ""


def showApiArguments(url, rest_type):
    # Get the whole API file
    url_base = url.split('/')[1]
    base_api_data = requests.get(ovhcloud.OVH_API_URL + "/" + url_base + ".json")
    base_api_json = base_api_data.json()

    # Pinpoint the specific data base on the url
    selected_api = [s for s in base_api_json['apis'] if s['path'] == url][0]
    selected_data = [s for s in selected_api['operations'] if s['httpMethod'] == rest_type.upper()][0]

    display_text = '\nPROPERTY\t\tREQUIRED\tDATATYPE\tDESCRIPTION\n'
    for param in selected_data['parameters']:
        display_text += "%s\t\t%s\t%s\t%s\n" % (
            param['name'], param['required'], param['dataType'], param['description'])

    return display_text


def OVH_AllApis(ovh_url):
    # Get the list of primary OVH API's
    request_data = requests.get(url=ovh_url)
    return json.loads(request_data.text)