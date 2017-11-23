import json
import os
import ovhcloud

import requests
from client import Launcher

CACHE_FILE = 'api_cache.json'

class CacheManager(object):
    def __init__(self, client: Launcher):
        self._client = client

    @property
    def client(self):
        return self._client

    def checkCache(self, cli_req):
        from api_handler import OVH_AllApis, Api_Handler

        #Check if the requested url exists in the cache
        #Check if a cache exists, create if not
        new_cache = False
        try:
            if not os.path.exists(self.client.configuration_dir):
                os.makedirs(self.client.configuration_dir)
                new_cache = True
            else :
                if not os.path.exists(self.client.configuration_dir + CACHE_FILE):
                    new_cache = True
        except Exception as e:
            print(e)


        if new_cache:
            #We need to make a new file and store the existing APIs in it
            with open(self.client.configuration_dir + CACHE_FILE, 'w') as outfile:
                json.dump(OVH_AllApis(), outfile)
        else:
            #Check if url user requested exists
            json_data = open(self.client.configuration_dir + CACHE_FILE).read()
            cache_data = json.loads(json_data)

            api_handler = None
            for api in cache_data["apis"]:
                if(api["path"] == cli_req):
                    api_handler = Api_Handler(api, self.client.ovhApi)
                    continue

            if api_handler is None:
                print("This API does not exist.")
                exit(1)

            api_handler.request()