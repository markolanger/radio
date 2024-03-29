import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
import glob
import datetime
pygame.init()

subprocess.call('mpc play' , shell=True)
running = True

def refresh_menu_screen():
	print "refresh_menu_screen"
	#set up the fixed items on the menu
	screen.fill(white) #change the colours if needed
	font=pygame.font.Font(None,20)
	title_font=pygame.font.Font(None,20)
	station_font=pygame.font.Font(None,20)
	###### display the station name and split it into 2 parts : 
	station = subprocess.check_output("mpc current", shell=True )
	lines=station.split(":")
	length = len(lines) 
	if length==1:
		line1 = lines[0]
		line1 = line1[:-1]
		line2 = "No additional info: "
	else:
		line1 = lines[0]
		line2 = lines[1]

	line2 = line2[:42]
	line2 = line2[:-1]
	#trap no station data
	if line1 =="":
		line2 = "Press PLAY or REFRESH"
		station_status = "stopped"
		status_font = red
	else:
		station_status = "playing"
		status_font = black
	current_time = datetime.datetime.now().strftime('%H:%M:%S  %d.%m.%Y')
	time_label = font.render(current_time, 1, (black))
	station_name=station_font.render(line1, 1, (black))
	additional_data=station_font.render(line2, 1, (blue))
	station_label=font.render(station_status, 1, (status_font))
	pygame.draw.rect(screen, (black), (0,17,519,24), 2)
	screen.blit(time_label,   (360,  0))
	screen.blit(station_label,(5,0))
	screen.blit(station_name,(5,22))
	screen.blit(additional_data,(0,42))
	######## add volume number
	volume = subprocess.check_output("mpc volume", shell=True )
	volume = volume[8:]
	volume = volume[:-1]
	volume_tag=font.render(volume, 1, (black))
	screen.blit(volume_tag,(85,0))
	####### check to see if the Radio is connected to the internet
	IP = subprocess.check_output("hostname -I", shell=True )
	IP=IP[:3]
	if IP =="192":
		network_status = "online"
		status_font = black

	else:
		network_status = "offline"
		status_font = red

	network_status_label = font.render(network_status, 1, (status_font))
	screen.blit(network_status_label, (260,0))
	pygame.display.flip()

def main():
	print "main"
        while 1:
                for event in pygame.event.get():
			print "3"
			time.sleep(0.2)
			pygame.display.update()
			pygame.display.flip()
			refresh_menu_screen()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                print "screen pressed" #for debugging purposes
                                pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                print pos #for checking
                                pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
                                on_click()

	#ensure there is always a safe way to end the program if the touch screen fails
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
					sys.exit()


#################### EVERTHING HAS NOW BEEN DEFINED ###########################

#set size of the screen
size = width, height = 520,300
screen = pygame.display.set_mode(size)

#define colours
blue = 26, 0, 255
cream = 254, 255, 25
black = 0, 0, 0
white = 255, 255, 255
yellow = 255, 255, 0
red = 255, 0, 0
green = 0, 255, 0
print "1"
refresh_menu_screen()  #refresh the menu interface 
print "2"
main() #check for key presses and start emergency exit
#station_name()
