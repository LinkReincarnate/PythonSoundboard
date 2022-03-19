from utility import AudioRecorder
import pygame

class RecordButton:
    # Called for keyboard events (KEYUP, KEYDOWN)
    def on_key_event(self, event):
        pass

    # Called for joystick events (JOYBUTTONDOWN, JOYBUTTONUP)
    def on_joy_event(self, event):
        from main import is_any_sound_button_active

        is_down = event.type == pygame.JOYBUTTONDOWN
        # If any sound button is pressed then already play recorded sound, otherwise record it for playback.
        if is_any_sound_button_active():
            if is_down:
                AudioRecorder.start_play()
            else:
                AudioRecorder.stop_play()
        else:
            if is_down:
                AudioRecorder.start_record()
            else:
                AudioRecorder.start_record()
