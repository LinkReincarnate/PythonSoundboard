import sys

import pygame

from pygame.locals import *
from pygame import mixer
pygame.init()
pygame.display.set_caption('Soundboard')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

buttons = [[None] * 100  , [None] * 100  , [None] * 100  , [None] * 100  ]


#Load the sounds

# IsPlaying toggles sound if looping is true and hold is false
# if Hold is True, button only plays when held down
# -1 for infinite looping any other int for that number of loops plus one

buttons[0][0] = {}
buttons[0][0]["IsPlaying"] = False
buttons[0][0]["Hold"] = False
buttons[0][0]["IsMutable"] = True
buttons[0][0]["NumLoops"] = -1 
buttons[0][0]["Toggle"] = True
buttons[0][0]["Sound"] = mixer.Sound('Loops/130BPM/ET_130_C_UKGSnareLoop_4bars_Beats_130BPM_BANDLAB.wav')
buttons[0][0]["Sound"].set_volume(1)



buttons[0][1] = {}
buttons[0][1]["IsPlaying"] = False
buttons[0][1]["Hold"] = False
buttons[0][1]["IsMutable"] = True
buttons[0][1]["NumLoops"] = -1 
buttons[0][1]["Toggle"] = True
buttons[0][1]["Sound"] = mixer.Sound('Loops/130BPM/ET_130_C_UKGPercLoop_4bars_Beats_130BPM_BANDLAB.wav')
buttons[0][1]["Sound"].set_volume(1)


buttons[0][2] = {}
buttons[0][2]["IsPlaying"] = True
buttons[0][2]["Hold"] = False
buttons[0][2]["IsMutable"] = True
buttons[0][2]["NumLoops"] = -1 
buttons[0][2]["Toggle"] = True
buttons[0][2]["Sound"] = mixer.Sound('Loops/130BPM/ET_130_C_UKGKickLoop_4bars_Beats_130BPM_BANDLAB.wav')


buttons[0][3] = {}
buttons[0][3]["IsPlaying"] = False
buttons[0][3]["Hold"] = False
buttons[0][3]["IsMutable"] = True
buttons[0][3]["NumLoops"] = -1 
buttons[0][3]["Toggle"] = True
buttons[0][3]["Sound"] = mixer.Sound('Loops/130BPM/ET_130_C_UKGHatLoop_4bars_Beats_130BPM_BANDLAB.wav')


buttons[0][4] = {}
buttons[0][4]["IsPlaying"] = False
buttons[0][4]["Hold"] = False
buttons[0][4]["IsMutable"] = True
buttons[0][4]["NumLoops"] = -1 
buttons[0][4]["Toggle"] = True
buttons[0][4]["Sound"] = mixer.Sound('Loops/130BPM/Gold_108_Emin_SynthPad01_4bar_BANDLAB.wav')

buttons[0][5] = {}
buttons[0][5]["IsPlaying"] = False
buttons[0][5]["Hold"] = False
buttons[0][5]["IsMutable"] = True
buttons[0][5]["NumLoops"] = -1 
buttons[0][5]["Toggle"] = True
buttons[0][5]["Sound"] = mixer.Sound('Loops/130BPM/Gold_108_Emin_LeadPad_4bar_BANDLAB.wav')

buttons[0][6] = {}
buttons[0][6]["IsPlaying"] = False
buttons[0][6]["Hold"] = False
buttons[0][6]["IsMutable"] = True
buttons[0][6]["NumLoops"] = -1 
buttons[0][6]["Toggle"] = True
buttons[0][6]["Sound"] = mixer.Sound('Loops/130BPM/Gold_108_Emin_SubBass1_4bar_BANDLAB.wav')

buttons[0][7] = {}
buttons[0][7]["IsPlaying"] = False
buttons[0][7]["Hold"] = False
buttons[0][7]["IsMutable"] = True
buttons[0][7]["NumLoops"] = -1 
buttons[0][7]["Toggle"] = True
buttons[0][7]["Sound"] = mixer.Sound('Loops/130BPM/ts_128_Em_Pad_LoFi_8bars_BANDLAB.wav')

buttons[0][8] = {}
buttons[0][8]["IsPlaying"] = False
buttons[0][8]["Hold"] = False
buttons[0][8]["IsMutable"] = True
buttons[0][8]["NumLoops"] = -1 
buttons[0][8]["Toggle"] = True
buttons[0][8]["Sound"] = mixer.Sound('Loops/130BPM/Chill03_85_Em_EPChords6_8bar_BANDLAB.wav')

buttons[0][9] = {}
buttons[0][9]["IsPlaying"] = False
buttons[0][9]["Hold"] = False
buttons[0][9]["IsMutable"] = True
buttons[0][9]["NumLoops"] = -1 
buttons[0][9]["Toggle"] = True
buttons[0][9]["Sound"] = mixer.Sound('Loops/130BPM/Chill04_90_Em_VinylNoise_4bar_Fx_BANDLAB.wav')


buttons[1][0] = {}
buttons[1][0]["IsPlaying"] = False
buttons[1][0]["Hold"] = False
buttons[1][0]["IsMutable"] = True
buttons[1][0]["NumLoops"] = -1 
buttons[1][0]["Toggle"] = True
buttons[1][0]["Sound"] = mixer.Sound('Loops/130BPM/Chill03_85_Drumloop4_8bar_BANDLAB.wav')

buttons[1][1] = {}
buttons[1][1]["IsPlaying"] = False
buttons[1][1]["Hold"] = False
buttons[1][1]["IsMutable"] = True
buttons[1][1]["NumLoops"] = -1 
buttons[1][1]["Toggle"] = True
buttons[1][1]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_120_Am_VoxChop_4bar_BANDLAB.wav')

buttons[1][2] = {}
buttons[1][2]["IsPlaying"] = False
buttons[1][2]["Hold"] = False
buttons[1][2]["IsMutable"] = True
buttons[1][2]["NumLoops"] = -1 
buttons[1][2]["Toggle"] = True
buttons[1][2]["Sound"] = mixer.Sound('Loops/120BPM/Cartridge_Chords_05_Chords_120BPM_Aminor_BANDLAB.wav')

buttons[1][3] = {}
buttons[1][3]["IsPlaying"] = False
buttons[1][3]["Hold"] = False
buttons[1][3]["IsMutable"] = True
buttons[1][3]["NumLoops"] = -1 
buttons[1][3]["Toggle"] = True
buttons[1][3]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Lead2_4bar_BANDLAB.wav')

buttons[1][4] = {}
buttons[1][4]["IsPlaying"] = False
buttons[1][4]["Hold"] = False
buttons[1][4]["IsMutable"] = True
buttons[1][4]["NumLoops"] = -1 
buttons[1][4]["Toggle"] = True
buttons[1][4]["Sound"] = mixer.Sound('Loops/120BPM/PensiveMoments_Strings_121bpm_B_BANDLAB.wav')

buttons[1][5] = {}
buttons[1][5]["IsPlaying"] = False
buttons[1][5]["Hold"] = False
buttons[1][5]["IsMutable"] = True
buttons[1][5]["NumLoops"] = -1 
buttons[1][5]["Toggle"] = True
buttons[1][5]["Sound"] = mixer.Sound('Loops/120BPM/BigBrassBand_Chords_150bpm_Bbmin_BANDLAB.wav')

buttons[1][6] = {}
buttons[1][6]["IsPlaying"] = False
buttons[1][6]["Hold"] = False
buttons[1][6]["IsMutable"] = True
buttons[1][6]["NumLoops"] = -1 
buttons[1][6]["Toggle"] = True
buttons[1][6]["Sound"] = mixer.Sound('DubstepDrumKit/dubstep-club-a-hat.mp3')

buttons[1][7] = {}
buttons[1][7]["IsPlaying"] = False
buttons[1][7]["Hold"] = False
buttons[1][7]["IsMutable"] = True
buttons[1][7]["NumLoops"] = -1 
buttons[1][7]["Toggle"] = True
buttons[1][7]["Sound"] = mixer.Sound('DubstepDrumKit/dubstep-club-a-kick.mp3')

buttons[1][8] = {}
buttons[1][8]["IsPlaying"] = False
buttons[1][8]["Hold"] = False
buttons[1][8]["IsMutable"] = True
buttons[1][8]["NumLoops"] = -1 
buttons[1][8]["Toggle"] = True
buttons[1][8]["Sound"] = mixer.Sound('DubstepDrumKit/dubstep-club-a-snare.mp3')

buttons[1][9] = {}
buttons[1][9]["IsPlaying"] = False
buttons[1][9]["Hold"] = False
buttons[1][9]["IsMutable"] = True
buttons[1][9]["NumLoops"] = -1 
buttons[1][9]["Toggle"] = True
buttons[1][9]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_120_Am_Piano3_4bar_BANDLAB.wav')


buttons[2][0] = {}
buttons[2][0]["IsPlaying"] = False
buttons[2][0]["Hold"] = False
buttons[2][0]["IsMutable"] = True
buttons[2][0]["NumLoops"] = -1 
buttons[2][0]["Toggle"] = True
buttons[2][0]["Sound"] = mixer.Sound('Loops/120BPM/BarrelProofBreaks_Break05_Loop05_100bpm_BANDLAB.wav')

buttons[2][1] = {}
buttons[2][1]["IsPlaying"] = False
buttons[2][1]["Hold"] = False
buttons[2][1]["IsMutable"] = True
buttons[2][1]["NumLoops"] = -1 
buttons[2][1]["Toggle"] = True
buttons[2][1]["Sound"] = mixer.Sound('Loops/120BPM/BarrelProofBreaks_Break05_Loop08_100bpm_BANDLAB.wav')

buttons[2][2] = {}
buttons[2][2]["IsPlaying"] = False
buttons[2][2]["Hold"] = False
buttons[2][2]["IsMutable"] = True
buttons[2][2]["NumLoops"] = -1 
buttons[2][2]["Toggle"] = True
buttons[2][2]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_124_Percs_4bar_BANDLAB.wav')

buttons[2][3] = {}
buttons[2][3]["IsPlaying"] = False
buttons[2][3]["Hold"] = False
buttons[2][3]["IsMutable"] = True
buttons[2][3]["NumLoops"] = -1 
buttons[2][3]["Toggle"] = True
buttons[2][3]["Sound"] = mixer.Sound('Loops/120BPM/looperman-l-2509817-0239771-wheezy-x-gunna-x-nav-x-traviscott-x-tm88-666.wav')

buttons[2][4] = {}
buttons[2][4]["IsPlaying"] = False
buttons[2][4]["Hold"] = False
buttons[2][4]["IsMutable"] = True
buttons[2][4]["NumLoops"] = -1 
buttons[2][4]["Toggle"] = True
buttons[2][4]["Sound"] = mixer.Sound('Loops/120BPM/looperman-l-2687909-0259887-underground-shit-17.wav')

buttons[2][5] = {}
buttons[2][5]["IsPlaying"] = False
buttons[2][5]["Hold"] = False
buttons[2][5]["IsMutable"] = True
buttons[2][5]["NumLoops"] = -1 
buttons[2][5]["Toggle"] = True
buttons[2][5]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_125_Uplifter_4bar_BANDLAB.wav')

buttons[2][6] = {}
buttons[2][6]["IsPlaying"] = False
buttons[2][6]["Hold"] = False
buttons[2][6]["IsMutable"] = True
buttons[2][6]["NumLoops"] = -1 
buttons[2][6]["Toggle"] = True
buttons[2][6]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_110_Am_VoxChop_4bar_BANDLAB.wav')

buttons[2][7] = {}
buttons[2][7]["IsPlaying"] = False
buttons[2][7]["Hold"] = False
buttons[2][7]["IsMutable"] = True
buttons[2][7]["NumLoops"] = -1 
buttons[2][7]["Toggle"] = True
buttons[2][7]["Sound"] = mixer.Sound('Loops/120BPM/Malarkey_122_D#m_Lead_4bar_BANDLAB.wav')

buttons[2][8] = {}
buttons[2][8]["IsPlaying"] = False
buttons[2][8]["Hold"] = False
buttons[2][8]["IsMutable"] = True
buttons[2][8]["NumLoops"] = -1 
buttons[2][8]["Toggle"] = True
buttons[2][8]["Sound"] = mixer.Sound('Loops/120BPM/looperman-l-2687909-0174396-gangsta-shit.wav')

buttons[3][0] = {}
buttons[3][0]["IsPlaying"] = False
buttons[3][0]["Hold"] = False
buttons[3][0]["IsMutable"] = True
buttons[3][0]["NumLoops"] = -1 
buttons[3][0]["Toggle"] = True
buttons[3][0]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_Pad_BANDLAB.wav')

buttons[3][1] = {}
buttons[3][1]["IsPlaying"] = False
buttons[3][1]["Hold"] = False
buttons[3][1]["IsMutable"] = True
buttons[3][1]["NumLoops"] = -1 
buttons[3][1]["Toggle"] = True
buttons[3][1]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_Bass_BANDLAB.wav')

buttons[3][2] = {}
buttons[3][2]["IsPlaying"] = False
buttons[3][2]["Hold"] = False
buttons[3][2]["IsMutable"] = True
buttons[3][2]["NumLoops"] = -1 
buttons[3][2]["Toggle"] = True
buttons[3][2]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_Kick_BANDLAB.wav')

buttons[3][3] = {}
buttons[3][3]["IsPlaying"] = False
buttons[3][3]["Hold"] = False
buttons[3][3]["IsMutable"] = True
buttons[3][3]["NumLoops"] = -1
buttons[3][3]["Toggle"] = True 
buttons[3][3]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_Vocals_BANDLAB.wav')

buttons[3][4] = {}
buttons[3][4]["IsPlaying"] = False
buttons[3][4]["Hold"] = False
buttons[3][4]["IsMutable"] = True
buttons[3][4]["NumLoops"] = -1 
buttons[3][4]["Toggle"] = True
buttons[3][4]["Sound"] = mixer.Sound('Loops/120BPM/MotiveChords_116bpm_Amin_BANDLAB.wav')

buttons[3][5] = {}
buttons[3][5]["IsPlaying"] = False
buttons[3][5]["Hold"] = False
buttons[3][5]["IsMutable"] = True
buttons[3][5]["NumLoops"] = -1 
buttons[3][5]["Toggle"] = True
buttons[3][5]["Sound"] = mixer.Sound('Loops/120BPM/Motive_Harp_Arp_116bpm_Am_BANDLAB.wav')

buttons[3][6] = {}
buttons[3][6]["IsPlaying"] = False
buttons[3][6]["Hold"] = False
buttons[3][6]["IsMutable"] = True
buttons[3][6]["NumLoops"] = -1 
buttons[3][6]["Toggle"] = True
buttons[3][6]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_Keys_BANDLAB.wav')

buttons[3][7] = {}
buttons[3][7]["IsPlaying"] = False
buttons[3][7]["Hold"] = False
buttons[3][7]["IsMutable"] = True
buttons[3][7]["NumLoops"] = -1 
buttons[3][7]["Toggle"] = True
buttons[3][7]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_GrandPiano_BANDLAB.wav')

buttons[3][8] = {}
buttons[3][8]["IsPlaying"] = False
buttons[3][8]["Hold"] = False
buttons[3][8]["IsMutable"] = True
buttons[3][8]["NumLoops"] = -1
buttons[3][8]["Toggle"] = True
buttons[3][8]["Sound"] = mixer.Sound('Loops/120BPM/LovePain_136_Am_HighKeys_BANDLAB.wav')

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
	print(joystick.get_name())



while True:

	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		
		if event.type == JOYBUTTONDOWN:
			print(event)
			button_id = event.button
			instance_id = event.instance_id
			if buttons[instance_id][button_id]["Toggle"]:
				if buttons[instance_id][button_id]["IsPlaying"]:
					buttons[instance_id][button_id]["Sound"].stop()
					buttons[instance_id][button_id]["IsPlaying"] = False
				else:
					buttons[instance_id][button_id]["Sound"].play(buttons[instance_id][button_id]["NumLoops"])
					buttons[instance_id][button_id]["IsPlaying"] = True
			elif button_id == 9 and instance_id == 2:
				pygame.mixer.pause()
			elif button_id == 9 and instance_id == 3:
				for i in range(len(buttons)):
					for j in range(len(buttons[i])):
						if buttons[i][j]["IsMutable"]:
							buttons[i][j]["Sound"].set_volume(0)
			else :
				buttons[instance_id][button_id]["Sound"].stop()
				buttons[instance_id][button_id]["Sound"].play(buttons[instance_id][button_id]["NumLoops"])
			

			
				
		if event.type == JOYBUTTONUP:
			print(event)
			button_id = event.button
			instance_id = event.instance_id
			if button_id == 9 and instance_id == 2:
			   pygame.mixer.unpause()
			elif button_id == 9 and instance_id == 3:
				for i in range(len(buttons)):
					for j in range(len(buttons[i])):
						if i == 1 or (i == 2 and j != 9) or (i == 3 and j != 9):
							buttons[i][j]["Sound"].set_volume(1)
			else :
				if buttons[instance_id][button_id]["Hold"]:
					buttons[instance_id][button_id]["Sound"].stop()
				

			
			   
				
		
		
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