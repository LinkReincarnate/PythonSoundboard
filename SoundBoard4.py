import sys

import pygame

from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

button00Sound = mixer.Sound('JSR/530_COOK.WAV')
button01Sound = mixer.Sound('JSR/583_COOK.WAV')
button02Sound = mixer.Sound('JSR/619_COOK.WAV')
button03Sound = mixer.Sound('JSR/Bang the Drums.wav')
button04Sound = mixer.Sound('JSR/bold king.wav')
button05Sound = mixer.Sound('JSR/boom.wav')
button06Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-hat.mp3')
button07Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-kick.mp3')
button08Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-snare.mp3')
button09Sound = mixer.Sound('JSR/classic fill.wav')

button10Sound = mixer.Sound('JSR/drum fill rocky.wav')
button11Sound = mixer.Sound('JSR/Drums_Options Menu_Sonic Adventure 2.wav')
button12Sound = mixer.Sound('JSR/Funky drum.wav')
button13Sound = mixer.Sound('JSR/Punchy drums.wav')
button14Sound = mixer.Sound('JSR/Funky Guitar.wav')
button15Sound = mixer.Sound('JSR/Guitar Scat_Eggman Boss_Sonic CD.wav')
button16Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-hat.mp3')
button17Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-kick.mp3')
button18Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-snare.mp3')
button19Sound = mixer.Sound('JSR/Hit Shot.wav')

button20Sound = mixer.Sound('JSR/80s Dance Bass Synth 07.wav')
button21Sound = mixer.Sound('JSR/80s Dance Bass Synth 08.wav')
button22Sound = mixer.Sound('JSR/80s Dance Bass Synth 09.wav')
button23Sound = mixer.Sound('JSR/acoustic guitar.wav')
button24Sound = mixer.Sound('JSR/Edgy Rock_Get Edgy.wav')
button25Sound = mixer.Sound('JSR/Edgy Synth_Get Edgy.wav')
button26Sound = mixer.Sound('DubstepDrumKit/ewig-11-hihat.mp3')
button27Sound = mixer.Sound('DubstepDrumKit/ewig-10-kick.mp3')
button28Sound = mixer.Sound('DubstepDrumKit/ewig-12-snare.mp3')
button29Sound = mixer.Sound('JSR/Horn Hit.wav')

button30Sound = mixer.Sound('JSR/scratch that.wav')
button31Sound = mixer.Sound('JSR/Modern Rock Guitar 26_What U Need.wav')
button32Sound = mixer.Sound('JSR/Pop Rock Guitar 01.wav')
button33Sound = mixer.Sound('JSR/Pop Rock Guitar 02.wav')
button34Sound = mixer.Sound('JSR/scratch me.wav')
button35Sound = mixer.Sound('JSR/Synth Array 16.wav')
button36Sound = mixer.Sound('JSR/crash cymbal.wav')
button37Sound = mixer.Sound('JSR/Guru Guru Onsen 2 Kick 1.wav')
button38Sound = mixer.Sound('JSR/Guru Guru Onsen 2 Snare 1.wav')
button39Sound = mixer.Sound('JSR/rolling drums.wav')




pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())



while True:

    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 0 and event.instance_id == 0:
                button00Sound.stop()
                button00Sound.play(-1)

            if event.button == 1 and event.instance_id == 0:
                button01Sound.stop()
                button01Sound.play(-1)

            if event.button == 2 and event.instance_id == 0:
                button02Sound.stop()
                button02Sound.play(-1)

            if event.button == 3 and event.instance_id == 0:
                button03Sound.stop()
                button03Sound.play(-1)

            if event.button == 4 and event.instance_id == 0:
                button04Sound.stop()
                button04Sound.play(-1)

            if event.button == 5 and event.instance_id == 0:
                button05Sound.stop()
                button05Sound.play(-1)

            if event.button == 6 and event.instance_id == 0:
                button06Sound.stop()
                button06Sound.play()

            if event.button == 7 and event.instance_id == 0:
                button07Sound.stop()
                button07Sound.play()

            if event.button == 8 and event.instance_id == 0:
                button08Sound.stop()
                button08Sound.play()

            if event.button == 9 and event.instance_id == 0:
                button09Sound.stop()
                button09Sound.play(-1)

            if event.button == 0 and event.instance_id == 1:
                button10Sound.stop()
                button10Sound.play(-1)

            if event.button == 1 and event.instance_id == 1:
                button11Sound.stop()
                button11Sound.play(-1)

            if event.button == 2 and event.instance_id == 1:
                button12Sound.stop()
                button12Sound.play(-1)

            if event.button == 3 and event.instance_id == 1:
                button13Sound.stop()
                button13Sound.play(-1)

            if event.button == 4 and event.instance_id == 1:
                button14Sound.stop()
                button14Sound.play(-1)

            if event.button == 5 and event.instance_id == 1:
                button15Sound.stop()
                button15Sound.play(-1)

            if event.button == 6 and event.instance_id == 1:
                button16Sound.stop()
                button16Sound.play()

            if event.button == 7 and event.instance_id == 1:
                button17Sound.stop()
                button17Sound.play()

            if event.button == 8 and event.instance_id == 1:
                button18Sound.stop()
                button18Sound.play()

            if event.button == 9 and event.instance_id == 1:
                button19Sound.stop()
                button19Sound.play()

            if event.button == 0 and event.instance_id == 2:
                button20Sound.stop()
                button20Sound.play(-1)

            if event.button == 1 and event.instance_id == 2:
                button21Sound.stop()
                button21Sound.play(-1)

            if event.button == 2 and event.instance_id == 2:
                button22Sound.stop()
                button22Sound.play(-1)

            if event.button == 3 and event.instance_id == 2:
                button23Sound.stop()
                button23Sound.play(-1)

            if event.button == 4 and event.instance_id == 2:
                button24Sound.stop()
                button24Sound.play(-1)

            if event.button == 5 and event.instance_id == 2:
                button25Sound.stop()
                button25Sound.play(-1)

            if event.button == 6 and event.instance_id == 2:
                button26Sound.stop()
                button26Sound.play()

            if event.button == 7 and event.instance_id == 2:
                button27Sound.stop()
                button27Sound.play()

            if event.button == 8 and event.instance_id == 2:
                button28Sound.stop()
                button28Sound.play()

            if event.button == 9 and event.instance_id == 2:
                button29Sound.stop()
                button29Sound.play()

            if event.button == 0 and event.instance_id == 3:
                button30Sound.stop()
                button30Sound.play(-1)

            if event.button == 1 and event.instance_id == 3:
                button31Sound.stop()
                button31Sound.play(-1)

            if event.button == 2 and event.instance_id == 3:
                button32Sound.stop()
                button32Sound.play(-1)

            if event.button == 3 and event.instance_id == 3:
                button33Sound.stop()
                button33Sound.play(-1)

            if event.button == 4 and event.instance_id == 3:
                button34Sound.stop()
                button34Sound.play(-1)

            if event.button == 5 and event.instance_id == 3:
                button35Sound.stop()
                button35Sound.play(-1)

            if event.button == 6 and event.instance_id == 3:
                button36Sound.stop()
                button36Sound.play()

            if event.button == 7 and event.instance_id == 3:
                button37Sound.stop()
                button37Sound.play()

            if event.button == 8 and event.instance_id == 3:
                button38Sound.stop()
                button38Sound.play()

            if event.button == 9 and event.instance_id == 3:
                button00Sound.set_volume(0)



        if event.type == JOYBUTTONUP:
            print(event)
            
            if event.button == 0 and event.instance_id == 0:
                button00Sound.stop()
                
            if event.button == 1 and event.instance_id == 0:
                button01Sound.stop()
                

            if event.button == 2 and event.instance_id == 0:
                button02Sound.stop()
                

            if event.button == 3 and event.instance_id == 0:
                button03Sound.stop()
                

            if event.button == 4 and event.instance_id == 0:
                button04Sound.stop()
                

            if event.button == 5 and event.instance_id == 0:
                button05Sound.stop()
                

            if event.button == 6 and event.instance_id == 0:
                button06Sound.stop()
                

            if event.button == 7 and event.instance_id == 0:
                button07Sound.stop()
                

            if event.button == 8 and event.instance_id == 0:
                button08Sound.stop()
                

            if event.button == 9 and event.instance_id == 0:
                button09Sound.stop()
                

            if event.button == 0 and event.instance_id == 1:
                button10Sound.stop()
                

            if event.button == 1 and event.instance_id == 1:
                button11Sound.stop()
                

            if event.button == 2 and event.instance_id == 1:
                button12Sound.stop()
                

            if event.button == 3 and event.instance_id == 1:
                button13Sound.stop()
                

            if event.button == 4 and event.instance_id == 1:
                button14Sound.stop()
                

            if event.button == 5 and event.instance_id == 1:
                button15Sound.stop()
                

            if event.button == 6 and event.instance_id == 1:
                button16Sound.stop()
                

            if event.button == 7 and event.instance_id == 1:
                button17Sound.stop()
                

            if event.button == 8 and event.instance_id == 1:
                button18Sound.stop()
                

            #if event.button == 9 and event.instance_id == 1:
               # button19Sound.stop()
               

            if event.button == 0 and event.instance_id == 2:
                button20Sound.stop()
                

            if event.button == 1 and event.instance_id == 2:
                button21Sound.stop()
                

            if event.button == 2 and event.instance_id == 2:
                button22Sound.stop()
                

            if event.button == 3 and event.instance_id == 2:
                button23Sound.stop()
                

            if event.button == 4 and event.instance_id == 2:
                button24Sound.stop()
                

            if event.button == 5 and event.instance_id == 2:
                button25Sound.stop()
                

            if event.button == 6 and event.instance_id == 2:
                button26Sound.stop()
                

            if event.button == 7 and event.instance_id == 2:
                button27Sound.stop()
                

            if event.button == 8 and event.instance_id == 2:
                button28Sound.stop()
                

            if event.button == 9 and event.instance_id == 2:
                button29Sound.stop()
                

            if event.button == 0 and event.instance_id == 3:
                button30Sound.stop()
                

            if event.button == 1 and event.instance_id == 3:
                button31Sound.stop()
                

            if event.button == 2 and event.instance_id == 3:
                button32Sound.stop()
                

            if event.button == 3 and event.instance_id == 3:
                button33Sound.stop()
                

            if event.button == 4 and event.instance_id == 3:
                button34Sound.stop()
                

            if event.button == 5 and event.instance_id == 3:
                button35Sound.stop()
                

            if event.button == 6 and event.instance_id == 3:
                button36Sound.stop()
                

            if event.button == 7 and event.instance_id == 3:
                button37Sound.stop()
                

            if event.button == 8 and event.instance_id == 3:
                button38Sound.stop()
                

            if event.button == 9 and event.instance_id == 3:
                button00Sound.set_volume(1)
                
                
        
        
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)