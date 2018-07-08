class Alien:
	def __init__(self,hw,hw1,alien_image):
		self.x = hw
		self.y = hw1
		self.hit = False
		self.hit1 = False
		self.image = alien_image
	def display(self,screen):
		screen.blit(self.image,(self.x,self.y))
