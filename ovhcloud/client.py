import argparse
import os
import ovh
import ovhcloud
from api_handler import Ovh_Request
from errors import ArgumentError, InternalError


class Launcher(object):
    def __init__(self, conf_dir=None, conf_ovh=None, caching=False):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if conf_dir is None else conf_dir

        self._configuration_file = ovhcloud.DEFAULT_CONFIGURATION_DIR + '/ovh.conf' \
            if conf_ovh is None else conf_ovh

        self._ovhClient = ovh.Client(config_file=self.configurationFile)
        self._isCached = caching

    @property
    def configurationDir(self):
        return self._configuration_dir

    @property
    def configurationFile(self):
        return self._configuration_file

    @property
    def ovhClient(self):
        return self._ovhClient

    @property
    def isCached(self):
        return self._isCached


class ParsedArgs(object):
    def __init__(self, args, extra, params=None):
        self._args = args
        self._extra = extra
        self._params = params

    @property
    def args(self):
        return self._args

    @property
    def extra(self):
        return self._extra

    @property
    def params(self):
        return self._params


def check_args(parsedArgs: ParsedArgs):
    # Ensure REST method validity
    if (parsedArgs.args.rest_type is None or (parsedArgs.args.rest_type).lower() not in ovhcloud.REST_METHODS):
        raise ArgumentError('rest-type')
    # Ensure conf file validity
    if (False and not os.path.isfile(parsedArgs.args.conf_ovh)):
        raise ArgumentError('conf-ovh')
    # Ensure conf dir is a path
    if (False and parsedArgs.args.conf_dir != None and not os.path.exists(os.path.expanduser(parsedArgs.args.conf_dir))):
        raise ArgumentError('conf-dir')


def parse_args():
    parser = argparse.ArgumentParser()
    # Allows for a custom config
    parser.add_argument('-d', '--conf-dir', dest='conf_dir')
    parser.add_argument('-c', '--conf-ovh', dest='conf_ovh')

    # This arg displays information regarding the provided url
    parser.add_argument('-i', '--info', action="store_true", dest="show_info")

    # Gets the REST Method : 'get' by default or must specify {get,post,put,delete}
    parser.add_argument(dest='rest_type', choices=ovhcloud.REST_METHODS, nargs='?', default='get')

    # Put other args in a var so we can process them
    args, extras = parser.parse_known_args()

    # Process extra args to differentiate URL parts and post/put parameters
    # We use the '=' character to get those parameters and remove them from extras
    params = [s for s in extras if "=" in s]
    extras = [s for s in extras if s not in params]

    return ParsedArgs(args, extras, params)


def main():
    from cache_manager import CacheManager

    try:
        parsedArgs = parse_args()
        check_args(parsedArgs)

        # In client we store values needed for an OVH connection object
        client = Launcher(parsedArgs.args.conf_dir, parsedArgs.args.conf_ovh)
        # In request we store values related to the request itself
        request = Ovh_Request(parsedArgs.extra, parsedArgs.args.rest_type, parsedArgs.params)

        # Cachemanager handles requesting
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
