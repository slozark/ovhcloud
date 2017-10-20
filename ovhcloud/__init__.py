import logging
import os


from pkg_resources import get_distribution, resource_filename

#__version__ = get_distribution('ovhcloud').version
__version__ = '0.1'


DEFAULT_CONFIGURATION_DIR = os.path.expanduser('~/.ovhcloud/')

logging.getLogger(__name__).addHandler(logging.NullHandler())