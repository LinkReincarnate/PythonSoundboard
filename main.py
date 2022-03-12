import sys
from models.MuteButton import MuteButton
from models.PauseButton import PauseButton
from models.SoundButton import SoundButton
from models.ToggleButton import ToggleButton
from models.RecordButton import RecordButton
import pygame
import pprint
from pygame.locals import *
from dataclasses import dataclass

# Init pygame stuff
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

print("joysticks:")
pprint.pprint(joysticks)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30) 

# All buttons are defined here.
sound_buttons = [
    [ # Joy 0
        SoundButton('Loops/130BPM/ET_130_C_UKGSnareLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        SoundButton('Loops/130BPM/ET_130_C_UKGPercLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        SoundButton('Loops/130BPM/ET_130_C_UKGKickLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        SoundButton('Loops/130BPM/ET_130_C_UKGHatLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Gold_108_Emin_SynthPad01_4bar_BANDLAB.wav'),

        SoundButton('Loops/130BPM/Gold_108_Emin_LeadPad_4bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Gold_108_Emin_SubBass1_4bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/ts_128_Em_Pad_LoFi_8bars_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Chill03_85_Em_EPChords6_8bar_BANDLAB.wav'),
        #SoundButton('Loops/130BPM/Chill04_90_Em_VinylNoise_4bar_Fx_BANDLAB.wav'),
        ToggleButton()
    ],
    [ # Joy 1
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_Kick_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_RetroSnare_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_Bass_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_Strings_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_NylonGuitar_BANDLAB.wav'),

        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_HighNylon_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_MoonGuitar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_LowFlute_BANDLAB.wav'),
        SoundButton('Loops/130BPM/YouBrokeMe_130_Fm_HighFlute_BANDLAB.wav'),
        RecordButton()
        #SoundButton('Loops/120BPM/Malarkey_120_Am_Piano3_4bar_BANDLAB.wav'),
    ],
    [ # Joy 2
        SoundButton('Loops/130BPM/Toxic_130_Gm_Trumpet_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Toxic_130_Gm_LongTrumpet_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Toxic_130_Gm_Saxophone_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Toxic_130_Gm_RetroPiano_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Toxic_130_Gm_LeadKey_BANDLAB.wav'),

        SoundButton('Loops/130BPM/Toxic_130_Gm_GrandPiano_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Vox_BB_127_Emin_pluck_vocal_8_4_4_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Synth_BB_120_Emin_synth_4_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Keys_BB_140_Fmin_keys_synth_8_4_4_BANDLAB.wav'),
        PauseButton()
    ],
    [ # Joy 3
        SoundButton('Loops/130BPM/PT_135_Cm_Arp_04_8bars_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Kit2_LeadChords3_C_128_8bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Kit2_LeadChords2_C_128_8bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Kit2_LeadChords1_C_128_8bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Kit2_LeadChords_C_128_4bar_BANDLAB.wav'),

        SoundButton('Loops/130BPM/Kit2_LeadSynth1_C_128_8bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/Kit2_FilterChords_C_128_4bar_BANDLAB.wav'),
        SoundButton('Loops/130BPM/NM_Mux_Kick_124_BANDLAB.wav'),
        SoundButton('Loops/130BPM/DMH_Kit_01_DR_TopLoop_01_126bpm_BANDLAB.wav'),
        MuteButton()
    ]
]

#
# Wrappers for some state variables (TODO: There probably is a better way to do this..)
#

# If the toggle mode is on right now
in_toggle_mode = False
def get_toggle_mode():
    global in_toggle_mode
    return in_toggle_mode

def set_toggle_mode(enabled):
    global in_toggle_mode
    in_toggle_mode = enabled


# If the mixer is paused right now
is_mixer_paused = False
def get_pause():
    global is_mixer_paused
    return is_mixer_paused

def set_pause(paused):
    global is_mixer_paused
    is_mixer_paused = paused
    if paused:
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()


is_muted = False
def get_muted():
    global is_muted
    return is_muted

def set_muted(muted):
    global is_muted
    is_muted = muted
    for row in sound_buttons:
        for button in row:
            if isinstance(button, SoundButton):
                button.set_muted(muted)

def get_all_buttons():
    return sound_buttons

def get_all_sound_buttons():
    return filter(lambda v: isinstance(v, SoundButton), get_all_buttons())

def is_any_sound_button_active():
    return any(v.State for v in get_all_sound_buttons())

def handle_joy_button_event(event):
    try:
        sound_buttons[event.instance_id][event.button].on_joy_event(event)
    except IndexError:
        print(f"Button {event.button} [instance_id: {event.instance_id}] not yet implemented!")

# Main loop
def main():
    selected_inst_id = None

    # Main render loop
    while True:
        # Render toggle mode text
        screen.fill((0, 0, 0))
        screen.blit(font.render(f"in_toggle_mode: {in_toggle_mode}", True, (255, 255, 255)), (0,0))

        # Process pygame events
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP: # Process button event
                handle_joy_button_event(event)
                
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                # Map keyboard to joystick - It's buggy, but good enough for testing purposes (without joysticks)

                # Keys F1-F12 are the joy selector keys
                # Numpad keys 0 - 9 are mapped to joy buttons
                
                joy_selector_mapping = (
                        pygame.K_F1,
                        pygame.K_F2,
                        pygame.K_F3,
                        pygame.K_F4,
                        pygame.K_F5,
                        pygame.K_F6,
                        pygame.K_F7,
                        pygame.K_F8,
                        pygame.K_F9,
                        pygame.K_F10,
                        pygame.K_F11,
                        pygame.K_F12,
                )
                # Figure out selected joy
                if event.type == pygame.KEYDOWN:
                    if event.key in joy_selector_mapping:
                        selected_inst_id = joy_selector_mapping.index(event.key)
                        return
                else:
                    selected_inst_id = None
                
                if not selected_inst_id: # Issue here: If F key is released before the numpad buttons the button release is never going to be registered for the mapped joy button
                    return

                joy_button_mapping = (
                    pygame.K_KP0,
                    pygame.K_KP1,
                    pygame.K_KP2,
                    pygame.K_KP3,
                    pygame.K_KP4,
                    pygame.K_KP5,
                    pygame.K_KP6,
                    pygame.K_KP7,
                    pygame.K_KP8,
                    pygame.K_KP9,
                )
                if event.key not in joy_button_mapping:
                    return

                event.type = pygame.JOYBUTTONDOWN if event.type == pygame.KEYDOWN else pygame.JOYBUTTONUP
                event.instance_id = selected_inst_id
                event.button = joy_button_mapping.index(event.key)

                print(f"keyboard => joy: {event.button}, {event.instance_id}")

                # Now dispatch it as a joy event
                handle_joy_button_event(event)

            elif event.type == pygame.JOYDEVICEADDED or event.type == pygame.JOYDEVICEREMOVED: # Update joysticks
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                
            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # Quit if event is QUIT or if ESCAPE is pressed
                pygame.quit()
                sys.exit()

        # Update pygame
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()