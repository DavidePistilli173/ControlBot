from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

import time
import numpy as np

class KeyCombinations:
    MAXIMISE_WINDOW = np.array([Key.cmd, Key.up])

class ControlBot:
    # Constants
    INPUT_DELAY = 0.005 # Standard input delay in s.

    ### Initialisation
    def __init__(self):
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        
    ### Methods
    ### Keyboard
    # Single key press
    def k_single_press(self, key):
        self.keyboard.press(key)
        time.sleep(self.INPUT_DELAY)
        self.keyboard.release(key)
        time.sleep(self.INPUT_DELAY)
    # Repeated key press
    def k_repeat_presss(self, key, repetitions):
        for x in range(repetitions):
            self.k_single_press(key)
        time.sleep(self.INPUT_DELAY)
    # Press a key
    def k_hold(self, key):
        self.keyboard.press(key)
        time.sleep(self.INPUT_DELAY)
    # Release a key
    def k_release(self, key):
        self.keyboard.release(key)
        time.sleep(self.INPUT_DELAY)
    # Key combination
    def k_combination(self, keys):
        for key in keys:
            self.k_hold(key)
        for key in keys:
            self.k_release(key)
        time.sleep(self.INPUT_DELAY)
    # Type a sequence of characters
    def k_type(self, msg):
        for char in msg:
            self.k_single_press(char)
        time.sleep(self.INPUT_DELAY)

    ### Mouse
    # Immediately move to a fixed point or by a translation vector
    def m_move_now(self, vec, absolute=True):
        if not absolute:
            self.mouse.move(vec[0], vec[1])       
        else:
            pos = np.array([self.mouse.position[0], self.mouse.position[1]])
            diff = vec - pos
            self.m_move_now(diff, False)
        time.sleep(self.INPUT_DELAY)
    # Left click
    def m_left_click(self):
        self.mouse.click(Button.left)
        time.sleep(self.INPUT_DELAY)
