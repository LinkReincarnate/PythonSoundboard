from dataclasses import dataclass
import pygame 

# IsPlaying toggles sound if looping is true and hold is false
# if Hold is True, button only plays when held down
# -1 for infinite looping any other int for that number of loops plus one
@dataclass
class SoundButton:
    Sound : ...
    State   : bool = False     # If the sound is being played
    Toggled : bool = False     # Was the sound toggled on - If so `State = True` until it's toggled back off
    IsMuteable : bool = True 
    NumLoops : int = -1
    Toggle : bool = False

    def __init__(self, soundPath):
        self.Sound = pygame.mixer.Sound(soundPath)

    # Called for keyboard events (KEYUP, KEYDOWN)
    def on_key_event(self, event):
        pass

    # Called for joystick events (JOYBUTTONDOWN, JOYBUTTONUP)
    def on_joy_event(self, event):
        from main import get_toggle_mode

        is_down = event.type == pygame.JOYBUTTONDOWN
        if get_toggle_mode(): # In toggle mode just toggle state
            if is_down: # Ignore button up
                self.State = not self.State # Flip state
                if self.State: 
                    self.Sound.stop()
                else: 
                    self.Sound.play(self.NumLoops)
        else:
            self.State = is_down
            self.Sound.stop()
            if self.State:
                self.Sound.play(self.NumLoops)

    def set_muted(self, state):
        self.Sound.set_volume(0 if state else 1)
