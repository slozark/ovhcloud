# -*- encoding: utf-8 -*-

import logging
import os

from pkg_resources import get_distribution, resource_filename

#__version__ = get_distribution('ovhcloud').version
__version__ = '0.1'


#Global values
DEFAULT_CONFIGURATION_DIR = os.path.expanduser('~/.ovhcloud/')
OVH_API_URL = 'https://api.ovh.com/1.0'
CACHE_FILE = 'api_cache.json'
REST_METHODS = ['get','put','post','delete']

#Logging
logging.getLogger(__name__).addHandler(logging.NullHandler())