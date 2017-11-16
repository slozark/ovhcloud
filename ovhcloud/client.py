import argparse
import ovh
import ovhcloud


class Launcher(object):

    def __init__(self, args, _configuration_dir=None, _configuration_file=None):
        self._configuration_dir = ovhcloud.DEFAULT_CONFIGURATION_DIR \
            if _configuration_dir is None else _configuration_dir

        self._configuration_file = ovhcloud.DEFAULT_CONFIGURATION_DIR + '/ovh.conf' \
            if _configuration_file is None else _configuration_file


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
    def ovhclient(self):
        return self._ovhclient

    def start(self):
        self._ovhclient = ovh.Client(config_file=self.configuration_file)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--conf-dir', dest="conf_dir")
    parser.add_argument('-c', '--conf-ovh', dest='conf_ovh')
    parser.add_argument('-a', '--api', dest='ovh_com')
    args = parser.parse_args()

    client = Launcher(_configuration_dir=args.conf_dir,_configuration_file=args.conf_ovh)
    client.start()


    ovhcloud.checkCache(args.ovh_conf)



    test = client.ovhclient.get(_target="/me")
    print(test)

    '''
    json_ret = client.ovhclient.get(ovh_com)

    print(client.ovhclient.get('/me'))
    '''

if __name__ == '__main__':
    main()
