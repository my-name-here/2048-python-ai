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
    def send_message(self,message):
        self.dev.write(str(message).encode("ascii"))
    def query(self, message):
        self.dev.write(bytes(str(message),"ascii"))
        line = self.dev.readline().decode('ascii').strip()
        return line

ard = Arduino("/dev/cu.usbmodem114101")
sleep(1)


d = {0:"u",1:"r",2:"d",3:"l"}

def send_move_to_arduino(move):
    ard.send_message(move)
