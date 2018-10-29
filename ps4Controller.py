#!/usr/bin/env python3

"""
Use a PS4 controller in Python

Hardware:
- tested with the official PS4 USB dongle and a PS4 controller

Software:
- dependencies as below

Instructions:
- Initialise a new controller:
    ps4 = PS4Controller()
- in your update loop, update the controller state with:
    ps4.update()
- then feel free to access anything you like
    - for buttons:
        if ps4.button_data(PS4_BUTTON_CIRCLE) is True:
            (whatever)
    - for the axes, a value is returned between -1 and 1 with zero the centre:
        left_x_stick = ps4.axis_data[PS4_AXIS_LEFT_X]
    - for the D-pad, returns a tuple with the first value being left (-1) and
        right(1), and the second value being down (-1) and up (1)
        <need to check the above is correct>:
            D_pad = ps4.hat_data(PS4_HAT_D_PAD)
- when run, this module prints the raw values from the PS4 controller (far too
    fast)

"""

import os
import pygame
import pprint

# Button definitions
PS4_BUTTON_X = 0
PS4_BUTTON_CIRCLE = 1
PS4_BUTTON_TRIANGLE = 2
PS4_BUTTON_SQUARE = 3
PS4_BUTTON_L1 = 4
PS4_BUTTON_R1 = 5
PS4_BUTTON_L2 = 6
PS4_BUTTON_R2 = 7
PS4_BUTTON_SHARE = 8
PS4_BUTTON_OPTIONS = 9
PS4_BUTTON_PS = 10
PS4_BUTTON_LEFT_STICK_PRESS = 11
PS4_BUTTON_RIGHT_STICK_PRESS = 12
PS4_BUTTON_TOUCHPAD = 13

PS4_AXIS_LEFT_X = 0
PS4_AXIS_LEFT_Y = 1
PS4_AXIS_L2 = 2
PS4_AXIS_RIGHT_X = 3
PS4_AXIS_RIGHT_Y = 4
PS4_AXIS_R2 = 5

PS4_HAT_D_PAD = 0


class PS4Controller:
    """

    """
    def __init__(self, controllerNumber=0):
        """

        """

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(controllerNumber)
        self.controller.init()

        self.axis_data = {}
        for i in range(self.controller.get_numaxes()):
            self.axis_data[i] = 0.0

        self.button_data = {}
        for i in range(self.controller.get_numbuttons()):
            self.button_data[i] = False

        self.hat_data = {}
        for i in range(self.controller.get_numhats()):
            self.hat_data[i] = (0, 0)

    def update(self):
        """

        """

        for event in pygame.event.get():
            if event.type is pygame.JOYAXISMOTION:
                self.axis_data[event.axis] = round(event.value, 2)
            elif event.type is pygame.JOYBUTTONDOWN:
                self.button_data[event.button] = True
            elif event.type is pygame.JOYBUTTONUP:
                self.button_data[event.button] = False
            elif event.type is pygame.JOYHATMOTION:
                self.hat_data[event.hat] = event.value

    def printController(self):
        """

        """

        os.system('clear')
        pprint.pprint(self.button_data)
        pprint.pprint(self.axis_data)
        pprint.pprint(self.hat_data)


if __name__ == "__main__":
    ps4 = PS4Controller()
    while(True):
        ps4.update()
        ps4.printController()
