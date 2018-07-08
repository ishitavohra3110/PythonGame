import pygame
import sys
import time
import random
from missile import *
from Alien import *
from Spaceship import *
from pygame.locals import *
pygame.init()
width, height = 800, 800
acc = [False]
playerpos=[100,100]
count = 0
bullets = []
bullets1 = []
acc = [0, 0]
flag = 1
flag1 = 1 
got = 1
aliens = []
keys = [False, False]
alien_image = pygame.image.load("alien_happy.png")
screen = pygame.display.set_mode((width , height))
bullet_image = pygame.image.load("bullet.png")
bullet_image.set_colorkey((255,255,255))
bullet_image1 = pygame.image.load("bull1.png")
bullet_image1.set_colorkey((255,255,255))
player = pygame.image.load("ship.png")
bullet_change = pygame.image.load("alien_dead.png")
start = time.time()
clock = pygame.time.Clock()
space = Spaceship(player,100,100)
while 1:
    for event in pygame.event.get():
       		if event.type == pygame.KEYDOWN:
	   		if event.key == K_q:
				print(count)
				sys.exit()
		if event.type == pygame.KEYDOWN:
	   		if event.key == K_a:
				keys[0] = True
	   		elif event.key == K_d:
				keys[1] = True
		if event.type == pygame.KEYUP:
	   		if event.type == K_a:
	        		keys[0] = False
	   		elif event.type == K_d:
				keys[1] = False

	   	if keys[0]:
			space.y += 50
           	elif keys[1]:
			space.y -= 50
		keys = [False,False]
		if event.type == pygame.KEYDOWN:
	        	if event.key == K_s:
				y = fire_bullet1(space.x,space.y,bullet_image1,200)
	        		bullets1.append(y)
	 	        	flag1 = 0;
	        	if event.type == pygame.KEYDOWN:
		        	if event.key == pygame.K_SPACE:
		              		y = fire_bullet(space.x,space.y,bullet_image,100)
		              		bullets.append(y)
		              		flag = 0;
    screen.fill(0)
    present = time.time()
    m,s = divmod(present-start,60)
    if s >= 10:
    	hw=random.randrange(640,720)
	hw1=random.randrange(0,720)
	x=Alien(hw,hw1,alien_image)
	aliens.append(x)
	temp = s
	start = time.time()
    
    for alien in aliens:
    	    got = 1
	    for bullet in bullets:
	            h=alien.image.get_height()/2
		    w=alien.image.get_width()/2
		    if alien.x-w <= bullet.bullet_x <=alien.x+w and alien.y-h/2 <= bullet.bullet_y <= alien.y+h/2:
			    alien.hit=True
	    if alien.hit:
		        count = count+1
		        aliens.remove(alien)
		        bullets.pop()
 	    for bullet in bullets1:
 	    	    h=alien.image.get_height()/2
 	    	    w=alien.image.get_width()/2
		    if alien.x-w <= bullet.bullet_x <= alien.x + w and alien.y-h/2 <= bullet.bullet_y <= alien.y+h/2:
			    alien.hit1 = True
	    if alien.hit1:
		    got = 0
		    alien.image = bullet_change

    if flag == 0:
	for bullet in bullets:
		bullet.display()
		now = time.time()
		m2,s2 = divmod(now-bullet.bullet_time,60)
		if s2>=1:
			bullet_time = time.time()
		bullet.bullet_x = bullet.bullet_x + 1
    if flag1 == 0:
        for bullet in bullets1:
		bullet.display()
		now = time.time()
		m3,s3 = divmod(now-bullet.bullet_time,60)
		if s3 >= 2:
			bullet.bullet_time = time.time()
		bullet.bullet_x = bullet.bullet_x + 2
    for alien in aliens:
		alien.display(screen)
		cur = time.time()
		m1,s1 = divmod(cur-start,60)
		if s1 >= 8 and got == 1:
			aliens.remove(alien)
		if s1 >= 13 and got == 0:
			aliens.remove(alien)
    space.change(height)
    space.draw(screen)
    pygame.display.flip()
    clock.tick(60)
		
			
			
			
			
						
         
