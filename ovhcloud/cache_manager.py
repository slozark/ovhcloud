import json
import os
import ovhcloud

import requests


class CacheManager(object):

    # TODO Find a way to ref client as a Launcher
    def __init__(self, client):
        self._client = client

    @property
    def client(self):
        return self._client

    def checkCache(self):

        # Create the directory if doesn't exist
        try:
            if not os.path.exists(self.client):
                os.makedirs(self.client.configuration_dir)
        except Exception as e:
            print(e)

        request_data = requests.get(url=ovhcloud.OVH_API_URL);
        json_data = json.loads(request_data.text)

        print(json_data)

        '''
        for url in api_data[u'apis']:
            filename = url[u'path'] + ".json"

            #Download json data and store it as a file when not cached yet
            if not os.path.exists(client.CACHE_PATH + filename):

                
                request_data = requests.get(url=OVH_URL + '/1.0' + filename);
                json_data = json.loads(request_data.text)
    
                #with open(os.path.join(path, filename), 'wb') as temp_file:
                with open(ovhcloud.CACHE_PATH + filename, 'wb') as temp_file:
                    temp_file.write(json_data)
                    temp_file.close
                

folder = ".ovhcache"
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)'''
