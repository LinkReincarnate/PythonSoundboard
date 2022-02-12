import sys

import pygame

from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

button00Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-arp.mp3')
button01Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-bass.mp3')
button02Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-bass (1).mp3')
button03Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-bass (2).mp3')
button04Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-bass (3).mp3')
button05Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-bassfill.mp3')
button06Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-hat.mp3')
button07Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-kick.mp3')
button08Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-snare.mp3')
button09Sound = mixer.Sound('Assets/hey_listen.mp3')

button10Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-arp.mp3')
button11Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-bass.mp3')
button12Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-bass (1).mp3')
button13Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-bass (2).mp3')
button14Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-bass (3).mp3')
button15Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-bassfill.mp3')
button16Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-hat.mp3')
button17Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-kick.mp3')
button18Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-snare.mp3')
button19Sound = mixer.Sound('Assets/parkour.mp3')

button20Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-piano.mp3')
button21Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-stab.mp3')
button22Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-stab.mp3')
button23Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-stab (1).mp3')
button24Sound = mixer.Sound('DubstepDrumKit/dubstep-club-b-lead.mp3')
button25Sound = mixer.Sound('DubstepDrumKit/dubstep-club-a-vox.mp3')
button26Sound = mixer.Sound('DubstepDrumKit/ewig-11-hihat.mp3')
button27Sound = mixer.Sound('DubstepDrumKit/ewig-10-kick.mp3')
button28Sound = mixer.Sound('DubstepDrumKit/ewig-12-snare.mp3')
button29Sound = mixer.Sound('Assets/bruh.mp3')

button30Sound = mixer.Sound('Assets/metalGearAlert.mp3')
button31Sound = mixer.Sound('DubstepDrumKit/ewig-01-chords.mp3')
button32Sound = mixer.Sound('DubstepDrumKit/ewig-02-chords.mp3')
button33Sound = mixer.Sound('DubstepDrumKit/ewig-03-chords.mp3')
button34Sound = mixer.Sound('DubstepDrumKit/ewig-09-fallbss.mp3')
button35Sound = mixer.Sound('DubstepDrumKit/ewig-04-vocal.mp3')
button36Sound = mixer.Sound('DubstepDrumKit/ewig-05-autobss.mp3')
button37Sound = mixer.Sound('DubstepDrumKit/ewig-08-autobss.mp3')
button38Sound = mixer.Sound('DubstepDrumKit/ewig-06-glidebss.mp3')
button39Sound = mixer.Sound('DubstepDrumKit/ewig-07-reesebss.mp3')



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
                button01Sound.play()

            if event.button == 2 and event.instance_id == 0:
                button02Sound.stop()
                button02Sound.play()

            if event.button == 3 and event.instance_id == 0:
                button03Sound.stop()
                button03Sound.play()

            if event.button == 4 and event.instance_id == 0:
                button04Sound.stop()
                button04Sound.play()

            if event.button == 5 and event.instance_id == 0:
                button05Sound.stop()
                button05Sound.play()

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
                button09Sound.play()

            if event.button == 0 and event.instance_id == 1:
                button10Sound.stop()
                button10Sound.play()

            if event.button == 1 and event.instance_id == 1:
                button11Sound.stop()
                button11Sound.play()

            if event.button == 2 and event.instance_id == 1:
                button12Sound.stop()
                button12Sound.play()

            if event.button == 3 and event.instance_id == 1:
                button13Sound.stop()
                button13Sound.play()

            if event.button == 4 and event.instance_id == 1:
                button14Sound.stop()
                button14Sound.play()

            if event.button == 5 and event.instance_id == 1:
                button15Sound.stop()
                button15Sound.play()

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
                button20Sound.play()

            if event.button == 1 and event.instance_id == 2:
                button21Sound.stop()
                button21Sound.play()

            if event.button == 2 and event.instance_id == 2:
                button22Sound.stop()
                button22Sound.play()

            if event.button == 3 and event.instance_id == 2:
                button23Sound.stop()
                button23Sound.play()

            if event.button == 4 and event.instance_id == 2:
                button24Sound.stop()
                button24Sound.play()

            if event.button == 5 and event.instance_id == 2:
                button25Sound.stop()
                button25Sound.play()

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
                button30Sound.play()

            if event.button == 1 and event.instance_id == 3:
                button31Sound.stop()
                button31Sound.play()

            if event.button == 2 and event.instance_id == 3:
                button32Sound.stop()
                button32Sound.play()

            if event.button == 3 and event.instance_id == 3:
                button33Sound.stop()
                button33Sound.play()

            if event.button == 4 and event.instance_id == 3:
                button34Sound.stop()
                button34Sound.play()

            if event.button == 5 and event.instance_id == 3:
                button35Sound.stop()
                button35Sound.play()

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
                button39Sound.stop()
                button39Sound.play()



        if event.type == JOYBUTTONUP:
            print(event)
            
            if event.button == 0 and event.instance_id == 0:
                button00Sound.stop()
                
        
        if event.type == JOYHATMOTION:
            print(event)
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