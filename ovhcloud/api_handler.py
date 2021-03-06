# -*- encoding: utf-8 -*-

import json

import ovh as ovh
import requests
import ovhcloud

from ovh import Client as OvhClient
from ovhcloud.errors import InternalError


class Ovh_Request(object):
    """
        This class is used to store the clients request values

        :param cli_req : The requested url (ex : /me/accessRestriction/enable)
        :param rest_method : The REST method type (ex: POST)
        :param request_data : Data for REST (put/post)
        :param show_info : flag asking for information
    """

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

    """
        This is the main function of the Api handler, it will
        decide to call or not a request to the API and show results.
        In some cases (eg display help), we need to make a 
        raw request (send_request) so I had to divide requests in two
    """
    def request(self, display=True):
        # If the user asked for information, only display that information
        if (self._ovh_request.showInfo):
            self.display_info()
            exit(0)

        # Handle specific treatment and generic exceptions (eg invalid URL)
        try:
            response = self.send_request()
        except ovh.exceptions.ResourceNotFoundError as e:
            print(str(e))
            print("Invalid URL: " + self._ovh_request.url)
            exit(1)
        except ovh.exceptions.BadParametersError as e:
            print(str(e))
            print("See the list of properties for this API below :\n %s" % showApiArguments(self._ovh_request.url,
                                                                                            self._ovh_request.method))
            exit(1)

        if (display): self.printResult(response)


    def send_request(self):
        response = None

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

        return response


    def printResult(self, response):
        print(json.dumps(response, indent=4, sort_keys=True))

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
        displayed_message = ""

        # 1 - Valid request ?
        valid=True
        try:
            request_result = self.send_request()
        except ovh.exceptions.ResourceNotFoundError as e:
            valid=False

        displayed_message += "\t1)\t%s %s %s a valid request" \
                             % (self._ovh_request.method, self._ovh_request.url, ("is" if valid else "is not"))

        # 2 - Exists in other modes ?
        displayed_message += "\n\t2)\tMore coming soon"

        # 3 - See also


        print(displayed_message)


def showApiArguments(url, rest_type):
    base_api_json = OVH_specificApi(url)

    # Pinpoint the specific data base on the url
    selected_api = [s for s in base_api_json['apis'] if s['path'] == url][0]
    selected_data = [s for s in selected_api['operations'] if s['httpMethod'] == rest_type.upper()][0]

    display_text = '\nPROPERTY\t\tREQUIRED\tDATATYPE\tDESCRIPTION\n'
    for param in selected_data['parameters']:
        display_text += "%s\t\t%s\t%s\t%s\n" % (
            param['name'], param['required'], param['dataType'], param['description'])

    return display_text


def OVH_specificApi(ovh_url):
    # Get the whole API file
    url_base = ovh_url.split('/')
    base_api_data = requests.get(ovhcloud.OVH_API_URL + "/" + url_base[1] + ".json")

    # For some reason, OVH doesn't always sends an API named
    # by the first part of the url, so we also have to check
    # the second (eg : https://api.ovh.com/1.0/hosting/web.json)
    if (base_api_data.status_code == 404):
        base_api_data = requests.get("%s/%s/%s.json" % (ovhcloud.OVH_API_URL, url_base[1], url_base[2]))

    return base_api_data.json()


def OVH_allApis():
    # Get the list of primary OVH API's
    request_data = requests.get(url=ovhcloud.OVH_API_URL)
    return json.loads(request_data.text)
