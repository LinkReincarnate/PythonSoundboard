import pygame

class ToggleButton:
    # Called for keyboard events (KEYUP, KEYDOWN)
    def on_key_event(self, event):
        pass

    # Called for joystick events (JOYBUTTONDOWN, JOYBUTTONUP)
    def on_joy_event(self, event):
        from main import set_toggle_mode, get_toggle_mode
        if event.type == pygame.JOYBUTTONDOWN:
            set_toggle_mode(not get_toggle_mode())
