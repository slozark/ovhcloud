import json
import os

import ovhcloud
from api_handler import Ovh_Request, Api_Handler
from client import Launcher


class CacheManager(object):
    def __init__(self, client: Launcher):
        self._client = client

    def checkCache(self, request: Ovh_Request):

        #Bypass cache verification process or not
        if (self._client.isCached):
            self.useCache()
        else:
            self.launchRequest(request)


    def launchRequest(self, request):
        api_handler = Api_Handler(self._client.ovhClient, request)
        api_handler.request()


    def useCache(self):
        from api_handler import OVH_AllApis

        # Check if the requested url exists in the cache
        # Check if a cache exists, create if not
        new_cache = False
        try:
            if not os.path.exists(self._client.configurationDir):
                os.makedirs(self._client.configurationDir)
                new_cache = True
            else:
                if not os.path.exists(self._client.configurationDir + ovhcloud.CACHE_FILE):
                    new_cache = True
        except Exception as e:
            print(e)

        if new_cache:
            # We need to make a new file and store the existing APIs in it
            with open(self._client.configurationDir + ovhcloud.CACHE_FILE, 'w') as outfile:
                json.dump(OVH_AllApis(ovhcloud.OVH_API_URL), outfile)
        else:
            # Check if url user requested exists
            json_data = open(self._client.configurationDir + ovhcloud.CACHE_FILE).read()
            cache_data = json.loads(json_data)

            api_handler = None
            '''
            for api in cache_data["apis"]:

                # We get the primary part of the urls and compare them
                # Ex : /me/foo/thing -> /me
                # TODO



                if (api["path"] == request.url):
                    api_handler = Api_Handler(self._client.ovhApi, request)
                    continue

            if api_handler is None:
                print("This API does not exist.")
                exit(1)

            api_handler.request()
            '''
