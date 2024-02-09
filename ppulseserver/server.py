from flask import Flask, request, jsonify
from ppulse import config
from ppulseserver import loader, trigger
from waitress import serve


app = Flask(__name__)
LOADER = None
TRIG = None

def get_loader():
    global LOADER
    if LOADER is None:
        LOADER = loader.loader()
    return LOADER

def get_trig():
    global TRIG
    if TRIG is None:
        TRIG = trigger.trigger()
    return TRIG

def start_server():
    host = config.get_server_address()['host']
    port = config.get_server_address()['port']
    #app.run(host=host, port=port, debug=True)
    serve(app, host="0.0.0.0", port=port)

@app.route("/set_channel", methods=['POST'])
def set_channel():
    data = request.get_json()
    channel = int(data['ch'])
    at_ser = int(data['at_ser'])
    at_par = int(data['at_par'])
    get_loader().set_channel(channel,at_ser,at_par)
    return jsonify(None)

@app.route("/set_channels", methods=['POST'])
def set_channels_file():
    data = request.get_json()
    at_ser_list = data['at_ser_list']
    at_par_list = data['at_par_list']
    get_loader().set_channels(at_ser_list,at_par_list)
    return jsonify(None)

@app.route("/reset_channels", methods=['POST'])
def reset_channels():
    at_ser_list = [0]*16
    at_par_list = [0]*16
    get_loader().set_channels(ch,at_ser_list,at_par_list)
    return jsonify(None)

@app.route("/set_trig", methods=['POST'])
def set_trig():
    data = request.get_json()
    get_trig().reset_period(period=int(data['period']))
    return jsonify(None)

@app.route("/run_trig", methods=['POST'])
def run_trig():
    data = request.get_json()
    get_trig().run(duration=int(data['duration']))
    return jsonify(None)