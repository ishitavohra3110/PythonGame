import time
import pygame
from pygame.locals import *
width=800
height=800
screen=pygame.display.set_mode((width,height))
class Missile:
        def __init__(self,x,y,bullet_image,pos):
	#               print("bullet")
	    self.bullet_x=x+pos
	    self.bullet_y=y
	    self.bullet_time=time.time()
	    self.bullet_used=False
	    self.bullet_image=bullet_image
	def display(self):
	    screen.blit(self.bullet_image,(self.bullet_x,self.bullet_y))
class fire_bullet(Missile):
	def __init__(self,x,y,image,pos):
	       Missile.__init__(self,x,y,image,pos)
class fire_bullet1(Missile):
	def __init__(self,x,y,image,pos):
		Missile.__init__(self,x,y,image,pos)
