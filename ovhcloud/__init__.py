# -*- encoding: utf-8 -*-

import logging
import os

from pkg_resources import get_distribution

__version__ = get_distribution('ovhcloud').version

#Global values
DEFAULT_CONFIGURATION_DIR = os.path.expanduser('~/.ovhcloud/')
DEFAULT_CONFIGURATION_FILE = 'ovh.conf'
OVH_API_URL = 'https://api.ovh.com/1.0'
CACHE_FILE = 'api_cache.json'
REST_METHODS = ['get','put','post','delete']

#Logging
logging.getLogger(__name__).addHandler(logging.NullHandler())