#!/usr/bin/env python
import pygame
import time
import sys
import random
import linecache
from pygame.locals import *

#fo = open("ziehung.txt", "rw+")

wheel0 =[3,5,7,2,4,8,6,9,0,1]
wheel1 =[7,2,4,8,6,9,0,1,3,5]
wheel2 =[9,0,1,3,5,7,2,4,8,6]
wheel3 =[3,5,7,2,4,8,6,9,0,1]


def rot_center(image, angle):
    # rotieren; center und size behalten
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def wait():
    while True:
        for event in pygame.event.get():
	    # der event bezieht sich auf das Fenster !!!
	    # ist die Bash der Focus, funktioniert es nicht
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
		pygame.quit()
		sys.exit()
	    if event.type == pygame.KEYDOWN:
                return
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    return

            

pygame.init()
text=pygame.font.Font('freesansbold.ttf',115)
white = [255, 255, 255]
black = [0,0,0]
display_surf = pygame.display.set_mode((1200, 600))
display_surf.fill(white)
pygame.mixer.init(44100,-16,2,2048)
pygame.mixer.music.load("wheel.mp3")

wait()

while True:
  image_surf0 = pygame.image.load("./wheel2.jpg").convert()
  image_surf1 = pygame.image.load("./wheel4.jpg").convert()
  image_surf2 = pygame.image.load("./wheel5.jpg").convert()
  image_surf3 = pygame.image.load("./wheel2.jpg").convert()
  surf0=rot_center(image_surf0, 0)
  surf1=rot_center(image_surf1, 0)
  surf2=rot_center(image_surf2, 0)
  surf3=rot_center(image_surf3, 0)


  angle = 0
  moves = 0

  pygame.display.flip()
  start = time.time()
  new = time.time()
  spin = 15
  rotates = 0

  winner = random.randint(1,1494)
  win_str = str(winner)
  if len(win_str) == 3:
	win_str = '0' + win_str
  if len(win_str) == 2:
        win_str = '00' + win_str
 
  
  pygame.mixer.music.play()

  while True:
    end = time.time()
    if  end - new  > 0.05:

        new = time.time()
        # drehen
        angle += 12
        # maximaler Winkel 360 Grad
	angle %= 360
        moves = angle // 36
	rotates += 1
	if rotates > 30:
		if number3 == int(win_str[3]):
			spin = 14
	if rotates > 60:
		if number2 == int(win_str[2]):
			spin = 12
	if rotates > 90:
		if number1 == int(win_str[1]):
			spin = 8
 	if rotates > 120:
		if number0 == int(win_str[0]):
			spin = 0
			pygame.mixer.music.stop()
			break

        if spin & 8:
		 surf0=rot_center(image_surf0, angle)
		 number0=wheel0[moves]
	if spin & 4:
		surf1=rot_center(image_surf1, angle)
		number1=wheel1[moves]
	if spin & 2:
		surf2=rot_center(image_surf2, angle)
		number2=wheel2[moves]
	if spin & 1:
		surf3=rot_center(image_surf3, angle)
		number3=wheel3[moves]
	#print number0, number1, number2, number3, moves

        # blit it to the screen
        display_surf.blit(surf0, (20, 140))
        display_surf.blit(surf1, (290,140))
        display_surf.blit(surf2, (550, 140))
	display_surf.blit(surf3, (820, 140))
	pygame.display.flip()

  # Zahl anzeigen
  TextSurf = text.render(win_str, True, black)
  TextRect = TextSurf.get_rect()
  TextRect.center = (550,80)
  display_surf.blit(TextSurf, TextRect)
  line = linecache.getline("ziehung.txt", winner)
  line = line[:-1]
  print line	 
  NameSurf = text.render(line, True, black)
  NameRect = NameSurf.get_rect()
  NameRect.center = (550,450) 
  display_surf.blit(NameSurf, NameRect)
  pygame.display.flip()
  wait()
  display_surf.fill(white)

print "bye"

