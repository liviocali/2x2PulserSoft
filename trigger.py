#!/usr/bin/env python
from signal import signal, SIGINT
from sys import exit
import argparse

import time

import pigpio

GPIO=13
WIDTH=10

parser = argparse.ArgumentParser(description='2x2 Pulser trigger script')
parser.add_argument('-p','--period',type=int, help='Period [ms]',default=10)
parser.add_argument('-d','--duration',type=int, help='Duriation [s]',default=60)
args = parser.parse_args()

def ctrlc_handler(signal_received, frame):
    pi.wave_tx_stop()
    pi.wave_delete(wid)
    pi.stop()
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__=='__main__':
   signal(SIGINT, ctrlc_handler)
   square = []
   period_us = int(args.period*1000)

   #                          ON       OFF      MICROS
   square.append(pigpio.pulse(1<<GPIO, 0,       WIDTH))
   square.append(pigpio.pulse(0,       1<<GPIO, period_us))

   pi = pigpio.pi() # connect to local Pi

   pi.set_mode(GPIO, pigpio.OUTPUT)

   pi.wave_add_generic(square)

   wid = pi.wave_create()

   if wid >= 0:
      pi.wave_send_repeat(wid)
      time.sleep(args.duration)
      pi.wave_tx_stop()
      pi.wave_delete(wid)

   pi.stop()