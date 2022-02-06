import sys

import pygame

from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

button0Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button1Sound = mixer.Sound('Assets/Gun+Silencer.mp3')
button2Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button3Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button4Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button5Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button6Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button7Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button8Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')
button9Sound = mixer.Sound('Assets/emotional-damage-meme.mp3')


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
                button0Sound.stop()
                button0Sound.play()

            if event.button == 1 and event.instance_id == 0:
                button1Sound.stop()
                button1Sound.play()

            if event.button == 2 and event.instance_id == 0:
                button2Sound.stop()
                button2Sound.play()

            if event.button == 3 and event.instance_id == 0:
                button3Sound.stop()
                button3Sound.play()

            if event.button == 4 and event.instance_id == 0:
                button4Sound.stop()
                button4Sound.play()

            if event.button == 5 and event.instance_id == 0:
                button5Sound.stop()
                button5Sound.play()

            if event.button == 6 and event.instance_id == 0:
                button6Sound.stop()
                button6Sound.play()

            if event.button == 7 and event.instance_id == 0:
                button7Sound.stop()
                button7Sound.play()

            if event.button == 8 and event.instance_id == 0:
                button8Sound.stop()
                button8Sound.play()

            if event.button == 9 and event.instance_id == 0:
                button9Sound.stop()
                button9Sound.play()

            

        if event.type == JOYBUTTONUP:
            print(event)
        if event.type == JOYAXISMOTION:
            print(event)
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