from tkinter.ttk import setup_master
import pygame
from models.SoundButton import SoundButton

class MuteButton:
    # Called for keyboard events (KEYUP, KEYDOWN)
    def on_key_event(self, event):
        pass

    # Called for joystick events (JOYBUTTONDOWN, JOYBUTTONUP)
    def on_joy_event(self, event):
        from main import get_muted, set_muted
        if event.type == pygame.JOYBUTTONDOWN:
            set_muted(not get_muted())