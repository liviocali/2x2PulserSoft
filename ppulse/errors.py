import sys
from ppulse import config

ERRORS = {
        -1:  {"name": "YAML_ERROR", "description": "ERROR: server_config.yaml file not found! Check the path!"},
        -2:  {"name": "IP_ADDRESS", "description": "ERROR: Wrong IP or PORT! Please check config.yaml (Examples: 'localhost:5000' or '159.93.127.19:5001')"},
        -3:  {"name": "SERVER_CONNECTED", "description": "ERROR: Server disconected!"},
        -4:  {"name": "CHANNEL_ERROR", "description": "ERROR: Channel not existing"},
        -5:  {"name": "VALUE_ERROR", "description": "ERROR: Attenuator value not in 0-255"},
        -6:  {"name": "VALUE_ERROR", "description": "ERROR: Serial attenuator needs to be set to 0 to use parallel attenuator"},
        -7:  {"name": "FILE_ERROR", "description": "ERROR: Not all channels found in file"},
        -8:  {"name": "CONFIG_ERROR", "description": "ERROR: config file not found! Check the path!"},
        -9:  {"name": "PERIOD_ERROR", "description": "ERROR: Input trigger period out of range 3-3000 ms"},
        -10: {"name": "CONFIG_ERROR", "description": "ERROR: Input trigger duration out of range 1-600 sec"},
        }

def error_control(*mistakes):
    for mistake in mistakes:
        if isinstance(mistake, dict):
            continue
        if mistake in ERRORS:
            print(ERRORS[mistake]["description"])
            sys.exit()

def check_channel(channel):
    if 1<channel>config.NCHAN:
        return -4

def check_values(at_ser,at_par):
    if 0<at_ser>255:
        return -5
    if 0<at_par>255:
        return -5
    if at_par>0 and at_ser<0:
        return -6

def check_period(period):
    if period < 3 or period > 3000:
        return -9

def check_duration(duration):
    if duration < 1 or duration > 600:
        return -10
