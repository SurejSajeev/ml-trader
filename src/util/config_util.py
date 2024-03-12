import configparser
import os
from os.path import dirname, abspath

def get_config():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    CONFIG_FILE = os.path.join(parent_directory, 'config', 'resources.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config