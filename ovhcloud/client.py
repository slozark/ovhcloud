import argparse
import os
import ovh
import ovhcloud
from api_handler import OVH_Request
from errors import ArgumentError, InternalError

class Launcher(object):
    def __init__(self, conf_dir=None, conf_ovh=None):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if conf_dir is None else conf_dir

        self._configuration_file = ovhcloud.DEFAULT_CONFIGURATION_DIR + '/ovh.conf' \
            if conf_ovh is None else conf_ovh

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
    parser.add_argument('-d', '--conf-dir', dest='conf_dir')
    parser.add_argument('-c', '--conf-ovh', dest='conf_ovh')
    args = parser.parse_args()

    # Ensure REST method validity
    if (args.rest_method is None or (args.rest_method).lower() not in ovhcloud.REST_METHODS):
        raise ArgumentError('method')
    # Ensure conf file validity
    # TODO
    if (False and not os.path.isfile(args.conf_ovh)):
        raise ArgumentError('conf-ovh')
    # Ensure conf dir is a path
    # TODO
    if (False and args.conf_dir != None and not os.path.exists(os.path.expanduser(args.conf_dir))):
        raise ArgumentError('conf-dir')

    return args


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='rest', choices=ovhcloud.REST_METHODS, nargs='?')

    args = parser.parse_args()
    test = ''

    if args.rest is None:
        test = 'get'
    elif args.rest.lower() in ovhcloud.REST_METHODS:
        test = args.rest

    print('RESULTAT PARSER : %s' % test)


def main():
    from cache_manager import CacheManager

    try:
        args = parse_args()
        exit(0)
        
        args = check_args()
        client = Launcher(args.conf_dir, args.conf_ovh)
        request = OVH_Request(args.cli_req, args.rest_method, args.req_data)

        cache = CacheManager(client)
        cache.checkCache(request)

    except ArgumentError as e:
        print("Invalid argument \"%s\", aborting." % (e.value))
        exit(1)
    except InternalError as e:
        print("Internal Error.  Message : %s" % (e.value))
        exit(1)


if __name__ == '__main__':
    main()
