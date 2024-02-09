#!/usr/bin/env python
from signal import signal, SIGINT
from sys import exit
import argparse
import time
import pigpio

PWM_GPIO=13
WIDTH=10

class trigger:
   def __init__(self, period=10):
      self.square = []
      self.period_us = int(period*1000)
      #                               ON           OFF          MICROS
      self.square.append(pigpio.pulse(1<<PWM_GPIO, 0,           WIDTH))
      self.square.append(pigpio.pulse(0,           1<<PWM_GPIO, self.period_us))
      self.pi = pigpio.pi()
      self.pi.set_mode(PWM_GPIO, pigpio.OUTPUT)

      self.pi.wave_add_generic(self.square)

      self.wid = self.pi.wave_create()

   def run(self, duration):
      if self.wid >= 0:
         self.pi.wave_send_repeat(self.wid)
         time.sleep(duration)
         self.pi.wave_tx_stop()
         #pi.wave_delete(wid)

      #self.pi.stop()

   def reset_period(self,period):
      self.pi.wave_delete(self.wid)
      self.period_us = int(period*1000)
      #                               ON           OFF          MICROS
      self.square[0] = pigpio.pulse(1<<PWM_GPIO, 0,           WIDTH)
      self.square[1] = pigpio.pulse(0,           1<<PWM_GPIO, self.period_us)

      self.pi.wave_add_generic(self.square)
      self.wid = self.pi.wave_create()