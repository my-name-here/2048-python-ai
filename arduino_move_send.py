#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:58:59 2022

@author: christopherbrower
"""


import serial
from time import sleep
class Arduino:
    def __init__(self, port):
        self.dev = serial.Serial(port, baudrate=19200)
        sleep(1)

    def query(self, message):
        self.dev.write(message.encode('ascii'))
        line = self.dev.readline().decode('ascii').strip()
        return line
ard = Arduino("/dev/cu.usbmodem114101")
sleep(1)

def send_move_to_arduino(move):
    ard.query(move)