import argparse
import ovh
import ovhcloud

class ArgumentError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Launcher(object):
    def __init__(self, _args=None):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if _args.conf_dir is None else _args.conf_dir

        self._configuration_file = ovhcloud.DEFAULT_CONFIGURATION_DIR + '/ovh.conf' \
            if _args.conf_ovh is None else _args.conf_ovh

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

    @property
    def requestUrl(self):
        return self._requestUrl


'''
    def start(self):
        cache = CacheManager(self)
        cache.checkCache()
'''


def check_args():
    # Should I add an arg to force cache cleaning ?

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--conf-dir', dest="conf_dir")
    parser.add_argument('-c', '--conf-ovh', dest='conf_ovh')
    parser.add_argument('-a', '--api', dest='cli_req')
    parser.add_argument('-m', '--method', dest='rest_method')
    args = parser.parse_args()

    #if (True):
     #   raise ArgumentError('test')

    return args


def main():
    from cache_manager import CacheManager

    try:
        args = check_args()
        client = Launcher(args)

        cache = CacheManager(client)
        cache.checkCache(args.cli_req)

    except ArgumentError as e:
        print("Invalid argument %s, aborting." % (e.value))
        exit(1)


if __name__ == '__main__':
    main()
