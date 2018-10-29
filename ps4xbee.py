#!/usr/bin/env python3

"""
Control an Interbotix PhantomX mk3 AX12 hexapod using a PS4 controller

Harware:
- Interbotix hexapod running the standard Hexapod_Mark_II.ino firmware
- a PS4 controller paired to a...
- USB PS4 dongle
- the UartSBee that came with the Interbotix kit, with the paired XBee inserted

Software:
- this file
- the dependencies (which may be tricky, since I coded one of them...)

Instructions:
- plug UartSBee into USB port. Confirm this is on '/dev/ttyUSB0', or insert
    the correct port into the code below
- attach PS4 dongle, ensure blue light appears
- power on paired PS4 controller
- turn on hexapod
- run script from terminal

Notes:
- there appears to be a bug in the hexapod firmware, where pushing up on the
    left stick causes the robot to move backwards. I don't think I messed
    this up, but there's always a chance. I have inverted the interpolation
    to make up for this
- I have only implemented 3 on the gaits, because I ran out of buttons on the
    PS4 controller that made sense, but you can easily add your own. Just
    reference (http://learn.trossenrobotics.com/10-interbotix/crawlers/phantomx
    -hexapod/98-phantomx-hexapod-wireless-control-arbotix-commander.html)
    for details on which buttons map to what
"""
import time

import serial
from numpy import interp

from ps4Controller import *

# setup
ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 38400
ser.timeout = 0.5
ser.open()

ps4 = PS4Controller()

# loop
while(True):
    # the original arbotix commander uses range of 3-253 with neutral at 128
    right_V = interp(ps4.axis_data[PS4_AXIS_RIGHT_Y], [-1.0, 1.0], [3, 253])
    right_H = interp(ps4.axis_data[PS4_AXIS_RIGHT_X], [-1.0, 1.0], [3, 253])
    left_V = interp(ps4.axis_data[PS4_AXIS_LEFT_Y], [-1.0, 1.0], [253, 3])
    left_H = interp(ps4.axis_data[PS4_AXIS_LEFT_X], [-1.0, 1.0], [3, 253])

    # buttons
    ps4.update()
    buttons = 0
    if ps4.button_data[PS4_BUTTON_CIRCLE] is True:
        buttons += 16   # = L5, tripod, normal speed
    if ps4.button_data[PS4_BUTTON_TRIANGLE] is True:
        buttons += 2    # = R2, smooth amble
    if ps4.button_data[PS4_BUTTON_SQUARE] is True:
        buttons += 4    # = R3, smooth ripple gait

    ser.write(bytes([0xff]))
    ser.write(bytes([int(right_V)]))
    ser.write(bytes([int(right_H)]))
    ser.write(bytes([int(left_V)]))
    ser.write(bytes([int(left_H)]))
    ser.write(bytes([buttons]))
    ser.write(bytes([0]))
    ser.write(bytes([255 - (int(right_V) + int(right_H) + int(left_V) +
                    int(left_H) + buttons) % 256]))

    time.sleep(1.0/30.0)    # 30 Hz
