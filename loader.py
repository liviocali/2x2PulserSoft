import json
#from MAX528 import MAX528

DAC1 = 22
DAC2 = 17
DAC3 = 27
DAC4 = 4

class loader:
    def __init__(self):
        self.channels = []
        self.dac_s = []
        self.dac_p = []
        #self.dac_s.append(MAX528(0,DAC1))
        #self.dac_s.append(MAX528(0,DAC2))
        #self.dac_p.append(MAX528(0,DAC3))
        #self.dac_p.append(MAX528(0,DAC4))


    def load_file(self, filename):
        with open(filename, 'r') as file:
            config = json.load(file)
            setv_s = []
            setv_p = []
            for ch in config["channels"]:
                setv_s.append(config["channels"][ch][0])
                setv_p.append(config["channels"][ch][1])
        return setv_s, setv_p

    def set_channel(self, channel, at_ser = 0, at_par = 0):
        """
        Set pulser output channel voltage
        - channel: output channel (1 to 16)
        - at_ser: Attenuator value serial (0-255) 0->lowest voltage 255-> highest voltage
        - at_par: Attenuator value parallel (0-255) 0->highest volate 255->lowest voltage (ONLY USE IF at_ser ALREADY AT 0)
        """
        dac_nr = (channel-1)//8
        dac_ch = (channel-1)%8
        #self.dac_s[dac_nr].set_dac_channel(dac_ch,at_ser)
        #self.dac_p[dac_nr].set_dac_channel(dac_ch,at_par)
        print("Set output channel %2d to (%3d,%3d)"%(channel, at_ser, at_par))
    
    def set_channels_file(self, filename):
        setv_s, setv_p = self.load_file(filename)
        for ch in range(16):
            self.set_channel(ch+1, setv_s[ch], setv_p[ch])


