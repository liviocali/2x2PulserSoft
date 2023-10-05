import spidev
import time
import sys

import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)

class MAX528:
    def __init__(self,device,cepin):
        self.device = device
        self.cepin = cepin      #board select pin
        self.spi = spidev.SpiDev(0,self.device)
        self.spi.max_speed_hz = 10000
        self.spi.mode = 0

        GPIO.setup(self.cepin,GPIO.OUT)
        GPIO.output(self.cepin,GPIO.HIGH)

    def set_channel(self,channel,value):
        GPIO.output(self.cepin,GPIO.LOW) #activate chip select
        bytechannel= 2**channel
        bytevalue = value
        time.sleep(0.1)
        self.spi.writebytes([bytechannel,bytevalue]) #write DAC value
        time.sleep(0.1)
        GPIO.output(self.cepin,GPIO.HIGH)
        time.sleep(0.5)

    def scan_channel(self,channel):
        for i in range(0,255,5):
            self.set_channel(channel,i)

    def __del__(self):
        self.spi.close()
        GPIO.cleanup(self.cepin)









    
