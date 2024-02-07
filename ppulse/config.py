import yaml
from os.path import abspath
from ppulse import errors

REPOSITORY_NAME = f'ppulse'
CONFIG = f'ppulse/server_config.yaml'
NCHAN = 16

def get_app_path():
    path = abspath(__file__)
    path_split = path.split('/')
    app_path = ''
    for word in path_split:
        if word == REPOSITORY_NAME:
            break
        app_path += word
        app_path += '/'
    return app_path

def parse_yaml(path_to_config):
    try:
        with open(path_to_config, "r") as stream:
            data = yaml.safe_load(stream)
            return data
    except:
        return -1

def get_config_path():
    app_path = get_app_path()
    path_to_config = app_path + CONFIG
    return path_to_config

def get_server_address():
    path_to_config = get_config_path()
    data = parse_yaml(path_to_config)
    errors.error_control(data)
    host = data['Host']
    port = data['Port']
    return {'host': host, 'port': port}
