class Spaceship:
	def __init__(self,image,x,y):
		self.image = image
		self.x = x
		self.y = y
	def change(self,height):
		if self.y + self.image.get_height() >= height:
			self.y = self.y-50
		elif self.y <= 0:
			self.y=self.y+50
	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))

