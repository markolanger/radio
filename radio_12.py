import pygame, datetime, os, subprocess, sys, time
pygame.display.set_caption("Radiosteuerung")
screen = pygame.display.set_mode((520, 300))
pygame.font.init()
font = pygame.font.SysFont("lato", 15, 1, 0)
font_color = (   0,   0,   0)
pygame.init()
running = 1

while running:
  subprocess.call('sudo service mpd restart' , shell=True)
  subprocess.call('mpc stop' , shell=True)
  subprocess.call('mpc play' , shell=True)
  screen.fill(white) #change the colours if needed
	font=pygame.font.Font(None,30)
	title_font=pygame.font.Font(None,150)
	station_font=pygame.font.Font(None,40)

	current_time = datetime.datetime.now().strftime('%d.%m.%Y')
	current_clock = datetime.datetime.now().strftime('%H:%M:%S')
	clock_label = title_font.render(current_clock, 1, (grey))
	time_label = font.render(current_time, 1, (black))
	station_name=station_font.render(line1, 1, (black))
	additional_data=station_font.render(line2, 1, (blue))
	station_label=font.render(station_status, 1, (status_font))
	pygame.draw.rect(screen, (black), (0,62,820,42), 3)
	pygame.draw.rect(screen, (black), (0,293,820,37), 1)
	screen.blit(time_label,   (690, 300))
	screen.blit(station_label,(255,300))
	screen.blit(station_name,(260,66))
	screen.blit(additional_data,(255,105))
	screen.blit(clock_label,  (400, 155))
  ######## add volume number
	volume = subprocess.check_output("mpc volume", shell=True )
	volume = volume[8:]
	volume = volume[:-1]
	volume_tag=font.render(volume, 1, (black))
	screen.blit(volume_tag,(440,300))
  
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            pygame.event.post(pygame.event.Event(pygame.QUIT))           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    pygame.display.flip()
