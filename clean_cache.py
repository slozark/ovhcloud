import os
import ovhcloud



def checkCache(api_data):

    #Create the directory if doesn't exist
    try:
        if not os.path.exists(ovhcloud.CACHE_PATH):
            os.makedirs(ovhcloud.CACHE_PATH)
    except Exception as e:
        print(e)

    #
    for url in api_data[u'apis']:
        filename = url[u'path'] + ".json"

        #Download json data and store it as a file when not cached yet
        if not os.path.exists(ovhcloud.CACHE_PATH + filename):

            '''
            request_data = requests.get(url=OVH_URL + '/1.0' + filename);
            json_data = json.loads(request_data.text)

            #with open(os.path.join(path, filename), 'wb') as temp_file:
            with open(ovhcloud.CACHE_PATH + filename, 'wb') as temp_file:
                temp_file.write(json_data)
                temp_file.close
            '''

folder = ".ovhcache"
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)