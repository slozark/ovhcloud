import logging
import os


#from pkg_resources import get_distribution, resource_filename
#__version__ = get_distribution('ovhcloud').version

DEFAULT_CONFIGURATION_DIR = os.path.expanduser('~/.ovhcloud/')

logging.getLogger(__name__).addHandler(logging.NullHandler())