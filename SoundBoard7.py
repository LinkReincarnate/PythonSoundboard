import sys

import pygame

from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


#Load the sounds
button00Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Kick2_4bar_BANDLAB.wav')
button01Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Hats_4bar_BANDLAB.wav')
button02Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Clap_4bar_BANDLAB.wav')
button03Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Percs5_4bar_BANDLAB.wav')
button04Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Shaker_4bar_BANDLAB.wav')
button05Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Lead_4bar_BANDLAB.wav')
button06Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Bass2_4bar_BANDLAB.wav')
button07Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Bass_4bar_BANDLAB.wav')
button08Sound = mixer.Sound('Loops/120BPM/Malarkey_123_Am_Piano1_4bar_BANDLAB.wav')
button09Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Piano_4bar_BANDLAB.wav')

button10Sound = mixer.Sound('Loops/120BPM/Cartridge_Drums_03_BANDLAB.wav')
button11Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_VoxChop_4bar_BANDLAB.wav')
button12Sound = mixer.Sound('Loops/120BPM/Cartridge_Chords_05_Chords_120BPM_Aminor_BANDLAB.wav')
button13Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Lead2_4bar_BANDLAB.wav')
button14Sound = mixer.Sound('Loops/120BPM/PensiveMoments_Strings_121bpm_B_BANDLAB.wav')
button15Sound = mixer.Sound('Loops/120BPM/BigBrassBand_Chords_150bpm_Bbmin_BANDLAB.wav')
button16Sound = mixer.Sound('Loops/120BPM/looperman-l-5321594-0278489-justice-andy-hulse.wav')
button17Sound = mixer.Sound('Loops/120BPM/DNC_DNC_Brass_BANDLAB.wav')
button18Sound = mixer.Sound('Loops/120BPM/Country_Trap_Keys_20_BANDLAB.wav')
button19Sound = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Piano3_4bar_BANDLAB.wav')

button20Sound = mixer.Sound('Loops/120BPM/BarrelProofBreaks_Break05_Loop05_100bpm_BANDLAB.wav')
button21Sound = mixer.Sound('Loops/120BPM/BarrelProofBreaks_Break05_Loop08_100bpm_BANDLAB.wav')
button22Sound = mixer.Sound('Loops/120BPM/Malarkey_124_Percs_4bar_BANDLAB.wav')
button23Sound = mixer.Sound('Loops/120BPM/looperman-l-2509817-0239771-wheezy-x-gunna-x-nav-x-traviscott-x-tm88-666.wav')
button24Sound = mixer.Sound('Loops/120BPM/looperman-l-2687909-0259887-underground-shit-17.wav')
button25Sound = mixer.Sound('Loops/120BPM/Malarkey_125_Uplifter_4bar_BANDLAB.wav')
button26Sound = mixer.Sound('Loops/120BPM/Malarkey_110_Am_VoxChop_4bar_BANDLAB.wav')
button27Sound = mixer.Sound('Loops/120BPM/Malarkey_122_D#m_Lead_4bar_BANDLAB.wav')
button28Sound = mixer.Sound('Loops/120BPM/looperman-l-2687909-0174396-gangsta-shit.wav')
#button29Sound = mixer.Sound('')

button30Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_Pad_BANDLAB.wav')
button31Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_Bass_BANDLAB.wav')
button32Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_Kick_BANDLAB.wav')
button33Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_Vocals_BANDLAB.wav')
button34Sound = mixer.Sound('Loops/120BPM/MotiveChords_116bpm_Amin_BANDLAB.wav')
button35Sound = mixer.Sound('Loops/120BPM/Motive_Harp_Arp_116bpm_Am_BANDLAB.wav')
button36Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_Keys_BANDLAB.wav')
button37Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_GrandPiano_BANDLAB.wav')
button38Sound = mixer.Sound('Loops/120BPM/LovePain_136_Am_HighKeys_BANDLAB.wav')
#button39Sound = mixer.Sound('')

#set sound attributes
button00IsMutable = True
button01IsMutable = True
button02IsMutable = True
button03IsMutable = True
button04IsMutable = True
button05IsMutable = True
button06IsMutable = True
button07IsMutable = True
button08IsMutable = True
button09IsMutable = True
button10IsMutable = True
button11IsMutable = True
button12IsMutable = True
button13IsMutable = True
button14IsMutable = True
button15IsMutable = True
button16IsMutable = True
button17IsMutable = True
button18IsMutable = True
button19IsMutable = True
button20IsMutable = True
button21IsMutable = True
button22IsMutable = True
button23IsMutable = True
button24IsMutable = True
button25IsMutable = True
button26IsMutable = True
button27IsMutable = True
button28IsMutable = True
#button29IsMutable = True
button30IsMutable = True
button31IsMutable = True
button32IsMutable = True
button33IsMutable = True
button34IsMutable = True
button35IsMutable = True
button36IsMutable = True
button37IsMutable = True
button38IsMutable = True
#button39IsMutable = False

# -1 for infinite looping any other int for that number of loops plus one
button00NumLoops = -1
button01NumLoops = -1
button02NumLoops = -1
button03NumLoops = -1
button04NumLoops = -1
button05NumLoops = -1
button06NumLoops = -1
button07NumLoops = -1
button08NumLoops = -1
button09NumLoops = -1
button10NumLoops = -1
button11NumLoops = -1
button12NumLoops = -1
button13NumLoops = -1
button14NumLoops = -1
button15NumLoops = -1
button16NumLoops = -1
button17NumLoops = -1
button18NumLoops = -1
button19NumLoops = -1
button20NumLoops = -1
button21NumLoops = -1
button22NumLoops = -1
button23NumLoops = -1
button24NumLoops = -1
button25NumLoops = -1
button26NumLoops = -1
button27NumLoops = -1
button28NumLoops = -1
button29NumLoops = -1
button30NumLoops = -1
button31NumLoops = -1
button32NumLoops = -1
button33NumLoops = -1
button34NumLoops = -1
button35NumLoops = -1
button36NumLoops = 0
button37NumLoops = 0
button38NumLoops = 0
#button39NumLoops = 0

#if hold is True button only plays when held down

button00Hold = True
button01Hold = True
button02Hold = True
button03Hold = True
button04Hold = True
button05Hold = True
button06Hold = True
button07Hold = True
button08Hold = True
button09Hold = True
button10Hold = True
button11Hold = True
button12Hold = True
button13Hold = True
button14Hold = True
button15Hold = True
button16Hold = True
button17Hold = True
button18Hold = True
button19Hold = True
button20Hold = True
button21Hold = True
button22Hold = True
button23Hold = True
button24Hold = True
button25Hold = True
button26Hold = True
button27Hold = True
button28Hold = True
#button29Hold = True
button30Hold = True
button31Hold = True
button32Hold = True
button33Hold = True
button34Hold = True
button35Hold = True
button36Hold = False
button37Hold = False
button38Hold = False
#button39Hold = True


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
                button00Sound.play(button00NumLoops)

            if event.button == 1 and event.instance_id == 0:
                button01Sound.stop()
                button01Sound.play(button01NumLoops)

            if event.button == 2 and event.instance_id == 0:
                button02Sound.stop()
                button02Sound.play(button02NumLoops)

            if event.button == 3 and event.instance_id == 0:
                button03Sound.stop()
                button03Sound.play(button03NumLoops)

            if event.button == 4 and event.instance_id == 0:
                button04Sound.stop()
                button04Sound.play(button04NumLoops)

            if event.button == 5 and event.instance_id == 0:
                button05Sound.stop()
                button05Sound.play(button05NumLoops)

            if event.button == 6 and event.instance_id == 0:
                button06Sound.stop()
                button06Sound.play(button06NumLoops)

            if event.button == 7 and event.instance_id == 0:
                button07Sound.stop()
                button07Sound.play(button07NumLoops)

            if event.button == 8 and event.instance_id == 0:
                button08Sound.stop()
                button08Sound.play(button08NumLoops)

            if event.button == 9 and event.instance_id == 0:
                button09Sound.stop()
                button09Sound.play(button09NumLoops)

            if event.button == 0 and event.instance_id == 1:
                button10Sound.stop()
                button10Sound.play(button10NumLoops)

            if event.button == 1 and event.instance_id == 1:
                button11Sound.stop()
                button11Sound.play(button11NumLoops)

            if event.button == 2 and event.instance_id == 1:
                button12Sound.stop()
                button12Sound.play(button12NumLoops)

            if event.button == 3 and event.instance_id == 1:
                button13Sound.stop()
                button13Sound.play(button13NumLoops)

            if event.button == 4 and event.instance_id == 1:
                button14Sound.stop()
                button14Sound.play(button14NumLoops)

            if event.button == 5 and event.instance_id == 1:
                button15Sound.stop()
                button15Sound.play(button15NumLoops)

            if event.button == 6 and event.instance_id == 1:
                button16Sound.stop()
                button16Sound.play(button16NumLoops)

            if event.button == 7 and event.instance_id == 1:
                button17Sound.stop()
                button17Sound.play(button17NumLoops)

            if event.button == 8 and event.instance_id == 1:
                button18Sound.stop()
                button18Sound.play(button18NumLoops)

            if event.button == 9 and event.instance_id == 1:
                button19Sound.stop()
                button19Sound.play(button19NumLoops)

            if event.button == 0 and event.instance_id == 2:
                button20Sound.stop()
                button20Sound.play(button20NumLoops)

            if event.button == 1 and event.instance_id == 2:
                button21Sound.stop()
                button21Sound.play(button21NumLoops)

            if event.button == 2 and event.instance_id == 2:
                button22Sound.stop()
                button22Sound.play(button22NumLoops)

            if event.button == 3 and event.instance_id == 2:
                button23Sound.stop()
                button23Sound.play(button23NumLoops)

            if event.button == 4 and event.instance_id == 2:
                button24Sound.stop()
                button24Sound.play(button24NumLoops)

            if event.button == 5 and event.instance_id == 2:
                button25Sound.stop()
                button25Sound.play(button25NumLoops)

            if event.button == 6 and event.instance_id == 2:
                button26Sound.stop()
                button26Sound.play(button26NumLoops)

            if event.button == 7 and event.instance_id == 2:
                button27Sound.stop()
                button27Sound.play(button27NumLoops)

            if event.button == 8 and event.instance_id == 2:
                button28Sound.stop()
                button28Sound.play(button28NumLoops)

            if event.button == 9 and event.instance_id == 2:
               # button29Sound.stop()
                #button29Sound.play(button29NumLoops)
                pygame.mixer.pause()

            if event.button == 0 and event.instance_id == 3:
                button30Sound.stop()
                button30Sound.play(button30NumLoops)

            if event.button == 1 and event.instance_id == 3:
                button31Sound.stop()
                button31Sound.play(button31NumLoops)

            if event.button == 2 and event.instance_id == 3:
                button32Sound.stop()
                button32Sound.play(button32NumLoops)

            if event.button == 3 and event.instance_id == 3:
                button33Sound.stop()
                button33Sound.play(button33NumLoops)

            if event.button == 4 and event.instance_id == 3:
                button34Sound.stop()
                button34Sound.play(button34NumLoops)

            if event.button == 5 and event.instance_id == 3:
                button35Sound.stop()
                button35Sound.play(button35NumLoops)

            if event.button == 6 and event.instance_id == 3:
                button36Sound.stop()
                button36Sound.play(button36NumLoops)

            if event.button == 7 and event.instance_id == 3:
                button37Sound.stop()
                button37Sound.play(button37NumLoops)

            if event.button == 8 and event.instance_id == 3:
                button38Sound.stop()
                button38Sound.play(button38NumLoops)

            if event.button == 9 and event.instance_id == 3:
                if button00IsMutable:
                    button00Sound.set_volume(0)
                if button01IsMutable:
                    button01Sound.set_volume(0)
                if button02IsMutable:
                    button02Sound.set_volume(0)
                if button03IsMutable:
                    button03Sound.set_volume(0)
                if button04IsMutable:
                    button04Sound.set_volume(0)
                if button05IsMutable:
                    button05Sound.set_volume(0)
                if button06IsMutable:
                    button06Sound.set_volume(0)
                if button07IsMutable:
                    button07Sound.set_volume(0)
                if button08IsMutable:
                    button08Sound.set_volume(0)
                if button09IsMutable:
                    button09Sound.set_volume(0)
                if button10IsMutable:
                    button10Sound.set_volume(0)
                if button11IsMutable:
                    button11Sound.set_volume(0)
                if button12IsMutable:
                    button12Sound.set_volume(0)
                if button13IsMutable:
                    button13Sound.set_volume(0)
                if button14IsMutable:
                    button14Sound.set_volume(0)
                if button15IsMutable:
                    button15Sound.set_volume(0)
                if button16IsMutable:
                    button16Sound.set_volume(0)
                if button17IsMutable:
                    button17Sound.set_volume(0)
                if button18IsMutable:
                    button18Sound.set_volume(0)
                if button19IsMutable:
                    button19Sound.set_volume(0)
                if button20IsMutable:
                    button20Sound.set_volume(0)
                if button21IsMutable:
                    button21Sound.set_volume(0)
                if button22IsMutable:
                    button22Sound.set_volume(0)
                if button23IsMutable:
                    button23Sound.set_volume(0)
                if button24IsMutable:
                    button24Sound.set_volume(0)
                if button25IsMutable:
                    button25Sound.set_volume(0)
                if button26IsMutable:
                    button26Sound.set_volume(0)
                if button27IsMutable:
                    button27Sound.set_volume(0)
                if button28IsMutable:
                    button28Sound.set_volume(0)
                #if button29IsMutable:
                   # button29Sound.set_volume(0)
                if button30IsMutable:
                    button30Sound.set_volume(0)
                if button31IsMutable:
                    button31Sound.set_volume(0)
                if button32IsMutable:
                    button32Sound.set_volume(0)
                if button33IsMutable:
                    button33Sound.set_volume(0)
                if button34IsMutable:
                    button34Sound.set_volume(0)
                if button35IsMutable:
                    button35Sound.set_volume(0)
                if button36IsMutable:
                    button36Sound.set_volume(0)
                if button37IsMutable:
                    button37Sound.set_volume(0)
                if button38IsMutable:
                    button38Sound.set_volume(0)
                
        if event.type == JOYBUTTONUP:
            print(event)
            
            if event.button == 0 and event.instance_id == 0:
                if button00Hold:
                    button00Sound.stop()
                
            if event.button == 1 and event.instance_id == 0:
                if button01Hold:    
                    button01Sound.stop()
                

            if event.button == 2 and event.instance_id == 0:
                if button02Hold:
                    button02Sound.stop()
                

            if event.button == 3 and event.instance_id == 0:
                if button03Hold:
                    button03Sound.stop()
                

            if event.button == 4 and event.instance_id == 0:
                if button04Hold:
                    button04Sound.stop()
                

            if event.button == 5 and event.instance_id == 0:
                if button05Hold:
                    button05Sound.stop()
                

            if event.button == 6 and event.instance_id == 0:
                if button06Hold:
                    button06Sound.stop()
                

            if event.button == 7 and event.instance_id == 0:
                if button07Hold:
                    button07Sound.stop()
                

            if event.button == 8 and event.instance_id == 0:
                if button08Hold:
                    button08Sound.stop()
                

            if event.button == 9 and event.instance_id == 0:
                if button09Hold:
                    button09Sound.stop()
                

            if event.button == 0 and event.instance_id == 1:
                if button10Hold:
                    button10Sound.stop()
                

            if event.button == 1 and event.instance_id == 1:
                if button11Hold:
                    button11Sound.stop()
                

            if event.button == 2 and event.instance_id == 1:
                if button12Hold:
                    button12Sound.stop()
                

            if event.button == 3 and event.instance_id == 1:
                if button13Hold:
                    button13Sound.stop()
                

            if event.button == 4 and event.instance_id == 1:
               if button14Hold:
                    button14Sound.stop()
                

            if event.button == 5 and event.instance_id == 1:
                if button15Hold:    
                    button15Sound.stop()
                

            if event.button == 6 and event.instance_id == 1:
                if button16Hold:
                    button16Sound.stop()
                

            if event.button == 7 and event.instance_id == 1:
                if button17Hold:
                    button17Sound.stop()
                

            if event.button == 8 and event.instance_id == 1:
                if button18Hold: 
                    button18Sound.stop()
                

            if event.button == 9 and event.instance_id == 1:
                if button19Hold:
                    button19Sound.stop()
               

            if event.button == 0 and event.instance_id == 2:
                if button20Hold:
                    button20Sound.stop()
                

            if event.button == 1 and event.instance_id == 2:
                if button21Hold:
                    button21Sound.stop()
                

            if event.button == 2 and event.instance_id == 2:
                if button22Hold:
                    button22Sound.stop()
                

            if event.button == 3 and event.instance_id == 2:
                if button23Hold:
                    button23Sound.stop()
                

            if event.button == 4 and event.instance_id == 2:
                if button24Hold:
                    button24Sound.stop()
                

            if event.button == 5 and event.instance_id == 2:
                if button25Hold:
                    button25Sound.stop()
                

            if event.button == 6 and event.instance_id == 2:
                if button26Hold:
                    button26Sound.stop()
                

            if event.button == 7 and event.instance_id == 2:
                if button27Hold:
                    button27Sound.stop()
                

            if event.button == 8 and event.instance_id == 2:
                if button28Hold:
                    button28Sound.stop()
                

            if event.button == 9 and event.instance_id == 2:
               pygame.mixer.unpause()
               
                #if button29Hold:
                   # button29Sound.stop()
                

            if event.button == 0 and event.instance_id == 3:
                if button30Hold:
                    button30Sound.stop()
                

            if event.button == 1 and event.instance_id == 3:
                if button31Hold:
                    button31Sound.stop()
                

            if event.button == 2 and event.instance_id == 3:
                if button32Hold:
                    button32Sound.stop()
                

            if event.button == 3 and event.instance_id == 3:
                if button33Hold:
                    button33Sound.stop()
                

            if event.button == 4 and event.instance_id == 3:
                if button34Hold:
                    button34Sound.stop()
                

            if event.button == 5 and event.instance_id == 3:
                if button35Hold:
                    button35Sound.stop()
                

            if event.button == 6 and event.instance_id == 3:
                if button36Hold:
                    button36Sound.stop()
                

            if event.button == 7 and event.instance_id == 3:
                if button37Hold:
                    button37Sound.stop()
                

            if event.button == 8 and event.instance_id == 3:
                if button38Hold:
                    button38Sound.stop()
                

            if event.button == 9 and event.instance_id == 3:
                button00Sound.set_volume(1)
                button01Sound.set_volume(1)
                button02Sound.set_volume(1)
                button04Sound.set_volume(1)
                button05Sound.set_volume(1)
                button06Sound.set_volume(1)
                button07Sound.set_volume(1)
                button08Sound.set_volume(1)
                button09Sound.set_volume(1)
                button10Sound.set_volume(1)
                button11Sound.set_volume(1)
                button12Sound.set_volume(1)
                button14Sound.set_volume(1)
                button15Sound.set_volume(1)
                button16Sound.set_volume(1)
                button17Sound.set_volume(1)
                button18Sound.set_volume(1)
                button19Sound.set_volume(1)
                button20Sound.set_volume(1)
                button21Sound.set_volume(1)
                button22Sound.set_volume(1)
                button24Sound.set_volume(1)
                button25Sound.set_volume(1)
                button26Sound.set_volume(1)
                button27Sound.set_volume(1)
                button28Sound.set_volume(1)
             #   button29Sound.set_volume(1)
                button30Sound.set_volume(1)
                button31Sound.set_volume(1)
                button32Sound.set_volume(1)
                button34Sound.set_volume(1)
                button35Sound.set_volume(1)
                button36Sound.set_volume(1)
                button37Sound.set_volume(1)
                button38Sound.set_volume(1)
               
                
        
        
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