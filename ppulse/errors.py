import sys

ERRORS = {
        -1:  {"name": "YAML_ERROR", "description": "ERROR: server_config.yaml file not found! Check the path!"},
        -2:  {"name": "IP_ADDRESS", "description": "ERROR: Wrong IP or PORT! Please check config.yaml (Examples: 'localhost:5000' or '159.93.127.19:5001')"},
        -3:  {"name": "SERVER_CONNECTED", "description": "ERROR: Server disconected!"},
        -4:  {"name": "CHANNEL_ERROR", "description": "ERROR: Channel not existing"},
        -5:  {"name": "VALUE_ERROR", "description": "ERROR: Attenuator value not in 0-255"},
        -6:  {"name": "VALUE_ERROR", "description": "ERROR: Serial attenuator needs to be set to 0 to use parallel attenuator"},
        -7:  {"name": "FILE_ERROR", "description": "ERROR: Not all channels found in file"},
        -8:  {"name": "CONFIG_ERROR", "description": "ERROR: config file not found! Check the path!"},
        }

def error_control(*mistakes):
    for mistake in mistakes:
        if isinstance(mistake, dict):
            continue
        if mistake in ERRORS:
            print(ERRORS[mistake]["description"])
            sys.exit()
