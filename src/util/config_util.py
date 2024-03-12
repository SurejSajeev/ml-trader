import configparser
import os
from os.path import dirname, abspath

def get_config():
    FILE_DIR = abspath((dirname(__file__)))
    CONFIG_FILE = os.path.join(FILE_DIR, 'config', 'resources.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config