import requests
from ppulse import config
from ppulse import errors
import json

def get_server_url():
    server = config.get_server_address()
    return f'http://{server["host"]}:{server["port"]}'

def server_status():
    url = get_server_url()
    try:
        r = requests.head(url)
        return True
    except:
        return False

def available_server():
    status = server_status()
    if not status:
        return -3

def cli_server_status():
    status = server_status()
    if status:
        print('Server available!')
    else:
        print('Server is not available!')

def set_channel(channel, at_ser, at_par):
    errors.error_control(available_server(),errors.check_channel(channel),errors.check_values(at_ser,at_par))
    data = {'ch': channel, 'at_ser': at_ser, 'at_par': at_par}
    server_url = get_server_url()
    url = f'{server_url}/set_channel'
    print('Set channel %02d to (%03d, %03d)'%(channel,at_ser,at_par))
    with requests.post(url,json=data) as resp:
        answ = resp.json()
        return answ

def set_channels_file(filename):
    setv_s, setv_p = load_file(filename)
    errors.error_control(available_server())
    if len(setv_s) != config.NCHAN:
        errors.error_control(-7)
    for ch in range(config.NCHAN):
        errors.error_control(check_values(setv_s[ch], setv_p[ch]))
        print('Set channel %02d to (%03d, %03d)'%(ch+1,setv_s[ch], setv_p[ch]))
    data = {'at_ser_list': setv_s, 'at_par_list': setv_p}
    server_url = get_server_url()
    url = f'{server_url}/set_channels'
    with requests.post(url,json=data) as resp:
        answ = resp.json()
        return answ

def load_file(filename):
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
            setv_s = []
            setv_p = []
            for ch in config["channels"]:
                setv_s.append(config["channels"][ch][0])
                setv_p.append(config["channels"][ch][1])
        return setv_s, setv_p
    except:
        errors.error_control(-8)

def set_trig(period):
    errors.error_control(available_server(),errors.check_period(period))
    data = {'period': period}
    server_url = get_server_url()
    url = f'{server_url}/set_trig'
    print('Set trigger period to %d ms' % period)
    with requests.post(url,json=data) as resp:
        answ = resp.json()
        return answ


def run_trig(duration):
    errors.error_control(available_server(),errors.check_duration(duration))
    data = {'duration': duration}
    server_url = get_server_url()
    url = f'{server_url}/run_trig'
    print('Run trigger for %d s' % duration)
    with requests.post(url,json=data) as resp:
        answ = resp.json()
        return answ
