import json
import os
import requests
import ovh
import sys

import ovhcloud


class Launcher(object):

    def __init__(self, args, _configuration_dir=None):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if _configuration_dir is None else _configuration_dir

        #Uses ovh.conf file
        self._ovh_client = ovh.Client()

    @property
    def configuration_dir(self):
        return self._configuration_dir

    @property
    def cache_file(self):
        return self._cache_file

    @property
    def ovh_client(self):
        return self._ovhclient





def main():
    client = Launcher(sys.argv[1:])
    #client.action()

    client.ovh_client.


if __name__ == '__main__':
    main()
