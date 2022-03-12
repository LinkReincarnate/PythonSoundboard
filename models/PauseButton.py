import pygame

class PauseButton:
    # Called for keyboard events (KEYUP, KEYDOWN)
    def on_key_event(self, event):
        pass

    # Called for joystick events (JOYBUTTONDOWN, JOYBUTTONUP)
    def on_joy_event(self, event):
        from main import get_pause, set_pause
        if event.type == pygame.JOYBUTTONDOWN:
            set_pause(not get_pause()) # Toggle pause mode
