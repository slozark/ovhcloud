import sys

import ovh

import ovhcloud


class Launcher(object):

    def __init__(self, args, _configuration_dir=None):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if _configuration_dir is None else _configuration_dir

        #Uses ovh.conf file
        self._ovhclient = ovh.Client(config_file='./ovh.conf3')

    @property
    def configuration_dir(self):
        return self._configuration_dir

    @property
    def cache_file(self):
        return self._cache_file

    @property
    def ovhclient(self):
        return self._ovhclient




def main():
    client = Launcher(sys.argv[1:])

    print(client.ovhclient.get('/me'))

if __name__ == '__main__':
    main()
