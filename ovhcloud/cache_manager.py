import json
import os
import ovhcloud

from api_handler import OVH_Request
from client import Launcher



class CacheManager(object):
    def __init__(self, client: Launcher):
        self._client = client

    @property
    def client(self):
        return self._client

    def checkCache(self, request: OVH_Request):
        from api_handler import OVH_AllApis, Api_Handler

        # Check if the requested url exists in the cache
        # Check if a cache exists, create if not
        new_cache = False
        try:
            if not os.path.exists(self.client.configuration_dir):
                os.makedirs(self.client.configuration_dir)
                new_cache = True
            else:
                if not os.path.exists(self.client.configuration_dir + ovhcloud.CACHE_FILE):
                    new_cache = True
        except Exception as e:
            print(e)

        if new_cache:
            # We need to make a new file and store the existing APIs in it
            with open(self.client.configuration_dir + ovhcloud.CACHE_FILE, 'w') as outfile:
                json.dump(OVH_AllApis(ovhcloud.OVH_API_URL), outfile)
        else:
            # Check if url user requested exists
            json_data = open(self.client.configuration_dir + ovhcloud.CACHE_FILE).read()
            cache_data = json.loads(json_data)

            api_handler = None
            for api in cache_data["apis"]:
                if (api["path"] == request.url):
                    api_handler = Api_Handler(api, self.client.ovhApi)
                    continue

            if api_handler is None:
                print("This API does not exist.")
                exit(1)

            api_handler.request()
