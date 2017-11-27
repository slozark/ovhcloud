import argparse
import os
import ovh
import ovhcloud
from api_handler import OVH_Request


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
    def ovhApi(self):
        return self._ovhApi

def check_args():
    # Should I add an arg to force cache cleaning ?

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--conf-dir', dest="conf_dir")
    parser.add_argument('-c', '--conf-ovh', dest='conf_ovh')
    parser.add_argument('-a', '--api', dest='cli_req')
    parser.add_argument('-m', '--method', dest='rest_method')
    parser.add_argument('-r', '--request-data', dest='req_data')
    args = parser.parse_args()

    if ((args.rest_method).lower() not in ovhcloud.REST_METHODS):
        raise ArgumentError('method')
    if (not os.path.exists(os.path.expanduser(args.conf_ovh))):
        raise ArgumentError('conf-ovh')
    if (args.conf_dir != None and not os.path.exists(os.path.expanduser(args.conf_dir))):
        raise ArgumentError('conf-dir')

    return args


def main():
    from cache_manager import CacheManager

    try:
        args = check_args()
        client = Launcher(args)
        request = OVH_Request(args.cli_req, args.rest_method, args.req_data)

        cache = CacheManager(client)
        cache.checkCache(request)

    except ArgumentError as e:
        print("Invalid argument %s, aborting." % (e.value))
        exit(1)


if __name__ == '__main__':
    main()
