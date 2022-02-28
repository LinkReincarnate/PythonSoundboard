from ast import match_case
from email.policy import default
import sys

import pygame
import pprint

from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

from dataclasses import dataclass

buttons = [[None] * 100  , [None] * 100  , [None] * 100  , [None] * 100  ]

# IsPlaying toggles sound if looping is true and hold is false
# if Hold is True, button only plays when held down
# -1 for infinite looping any other int for that number of loops plus one
@dataclass
class Button:
    Sound : ...
    State : bool = False     # If the sound is being played
    IsMuteable : bool = True 
    NumLoops : int = -1
    Toggle : bool = False

    def __init__(self, soundPath):
        self.Sound = mixer.Sound(soundPath)


buttons = [
    [
        Button('Loops/130BPM/ET_130_C_UKGSnareLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        Button('Loops/130BPM/ET_130_C_UKGPercLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        Button('Loops/130BPM/ET_130_C_UKGKickLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        Button('Loops/130BPM/ET_130_C_UKGHatLoop_4bars_Beats_130BPM_BANDLAB.wav'),
        Button('Loops/130BPM/Gold_108_Emin_SynthPad01_4bar_BANDLAB.wav'),
        Button('Loops/130BPM/Gold_108_Emin_LeadPad_4bar_BANDLAB.wav'),
        Button('Loops/130BPM/Gold_108_Emin_SubBass1_4bar_BANDLAB.wav'),
        Button('Loops/130BPM/ts_128_Em_Pad_LoFi_8bars_BANDLAB.wav'),
        Button('Loops/130BPM/Chill03_85_Em_EPChords6_8bar_BANDLAB.wav'),
        Button('Loops/130BPM/Chill04_90_Em_VinylNoise_4bar_Fx_BANDLAB.wav'),
    ],
    [
        Button('Loops/130BPM/YouBrokeMe_130_Fm_Kick_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_RetroSnare_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_Bass_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_Strings_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_NylonGuitar_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_HighNylon_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_MoonGuitar_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_LowFlute_BANDLAB.wav'),
        Button('Loops/130BPM/YouBrokeMe_130_Fm_HighFlute_BANDLAB.wav'),
        Button('Loops/120BPM/Malarkey_120_Am_Piano3_4bar_BANDLAB.wav'),
    ],
    [
        Button('Loops/130BPM/Toxic_130_Gm_Trumpet_BANDLAB.wav'),
        Button('Loops/130BPM/Toxic_130_Gm_LongTrumpet_BANDLAB.wav'),
        Button('Loops/130BPM/Toxic_130_Gm_Saxophone_BANDLAB.wav'),
        Button('Loops/130BPM/Toxic_130_Gm_RetroPiano_BANDLAB.wav'),
        Button('Loops/130BPM/Toxic_130_Gm_LeadKey_BANDLAB.wav'),
        Button('Loops/130BPM/Toxic_130_Gm_GrandPiano_BANDLAB.wav'),
        Button('Loops/130BPM/Vox_BB_127_Emin_pluck_vocal_8_4_4_BANDLAB.wav'),
        Button('Loops/130BPM/Synth_BB_120_Emin_synth_4_BANDLAB.wav'),
        Button('Loops/130BPM/Keys_BB_140_Fmin_keys_synth_8_4_4_BANDLAB.wav'),
    ],
    [
        Button('Loops/130BPM/PT_135_Cm_Arp_04_8bars_BANDLAB.wav'),
        Button('Loops/130BPM/Kit2_LeadChords3_C_128_8bar_BANDLAB.wav'),
        Button('Loops/130BPM/Kit2_LeadChords2_C_128_8bar_BANDLAB.wav'),
        Button('Loops/130BPM/Kit2_LeadChords1_C_128_8bar_BANDLAB.wav'),
        Button('Loops/130BPM/Kit2_LeadChords_C_128_4bar_BANDLAB.wav'),
        Button('Loops/130BPM/Kit2_LeadSynth1_C_128_8bar_BANDLAB.wav'),
        Button('Loops/130BPM/Kit2_FilterChords_C_128_4bar_BANDLAB.wav'),
        Button('Loops/130BPM/NM_Mux_Kick_124_BANDLAB.wav'),
        Button('Loops/130BPM/DMH_Kit_01_DR_TopLoop_01_126bpm_BANDLAB.wav'),
    ]
]

# If the toggle mode is on right now
in_toggle_mode = False

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

print("joysticks:")
pprint.pprint(joysticks)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30) 

while True:
    screen.fill((0, 0, 0))
    screen.blit(font.render(f"in_toggle_mode: {in_toggle_mode}", True, (255, 255, 255)), (0,0))
    for event in pygame.event.get():
        match event.type:
            case pygame.JOYBUTTONDOWN | pygame.JOYBUTTONUP:
                print(event)

                button_state = event.type == pygame.JOYBUTTONDOWN # Now, `button_state` is going to be `True`` if the button was pressed down, otherwise `False`.

                match (event.button, event.instance_id): 
                    case (9, 2):  # Pause/unpause mixer
                        if button_state:
                            pygame.mixer.pause()
                        else:
                            pygame.mixer.unpause()

                    case (9, 3): # Mute/Unmute all
                        for row in buttons:
                            for button in row:
                                if button.IsMuteable:
                                    button.Sound.set_volume(1 if button_state else 0)

                    case (9, 0): # Toggle mode enable - TODO: Change back instance id to 1
                        in_toggle_mode = button_state

                    case _: # Handle it as a button
                        button = buttons[event.instance_id][event.button]
                        if in_toggle_mode: # In toggle mode just toggle state
                            if button_state: # Ignore button up
                                button.State = not button.State # Flip state
                                if button.State: 
                                    button.Sound.play(button.NumLoops)
                                else: 
                                    button.Sound.stop()
                        else:
                            button.State = button_state
                            button.Sound.stop()
                            if button.State:
                                button.Sound.play(button.NumLoops)

            case pygame.JOYDEVICEADDED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in joysticks:
                    print(joystick.get_name())

            case pygame.JOYDEVICEREMOVED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

            case pygame.QUIT:
                pygame.quit()
                sys.exit()

            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    pygame.display.update()
    clock.tick(60)