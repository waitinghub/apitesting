from configparser import ConfigParser
from common.handle_path import CONF_FILE

def config_handler():
    '''读取ini文件'''
    config = ConfigParser()
    config.read(CONF_FILE, encoding='utf8')
    return config

read_config = config_handler()