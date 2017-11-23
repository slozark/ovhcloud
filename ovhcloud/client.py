import argparse
import ovh

import ovhcloud


class Launcher(object):
    def __init__(self, _configuration_dir=None, _configuration_file=None):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if _configuration_dir is None else _configuration_dir

        self._configuration_file = ovhcloud.DEFAULT_CONFIGURATION_DIR + '/ovh.conf' \
            if _configuration_file is None else _configuration_file

        self._ovhApi = ovh.Client(config_file=self.configuration_file)

    @property
    def configuration_dir(self):
        return self._configuration_dir

    @property
    def configuration_file(self):
        return self._configuration_file

    @property
    def cache_file(self):
        return self._cache_file

    @property
    def ovhApi(self):
        return self._ovhApi

'''
    def start(self):
        cache = CacheManager(self)
        cache.checkCache()
'''

def main():
    from cache_manager import CacheManager

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--conf-dir', dest="conf_dir")
    parser.add_argument('-c', '--conf-ovh', dest='conf_ovh')
    parser.add_argument('-a', '--api', dest='cli_req')
    args = parser.parse_args()

    # Should I add an arg to force cache cleaning ?

    client = Launcher(_configuration_dir=args.conf_dir, _configuration_file=args.conf_ovh)

    cache = CacheManager(client)
    cache.checkCache(args.cli_req)


if __name__ == '__main__':
    main()
