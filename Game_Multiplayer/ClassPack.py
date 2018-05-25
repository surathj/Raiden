import random
import time
import Block

red = (255,0,0)
display_width = 800
display_height = 600


rand_CPack_X = round(random.randrange(0, display_width-10)/10.0) * 10.0
rand_CPack_Y = round(random.randrange(0, display_height-10)/10.0) * 10.0

dark_violet = (148, 0, 211)
start_time = time.time()

def print_time(time):
	time.sleep(1)
	print(time)

class ClassPack(object):
	_instance = None
	def __new__(self, pgm, gameDisplay, player):
		self.pgm = pgm
		self.gameDisplay = gameDisplay
		self.player = player
		global start_time
		self.time = start_time

		if not self._instance:
			self._instance = super(ClassPack, self).__new__(self)
			self.agility = 5
		return self._instance

	def draw_cpack(self):
		global rand_CPack_X
		global rand_CPack_Y
		self.pgm.draw.rect(self.gameDisplay, dark_violet, [rand_CPack_X, rand_CPack_Y, 15, 15])
		elapsed = time.time() - self.time

		if((self.player.player_x > rand_CPack_X and self.player.player_x < rand_CPack_X + 15 or self.player.player_x + 10 > rand_CPack_X and 
			self.player.player_x + 10 < rand_CPack_X + 15)):
			self.time = time.time()
			if(elapsed > 0.6):
				#if time elapsed since last appearance is > 6 seconds
				rand_CPack_X = round(random.randrange(0, display_width-10)/10.0) * 10.0
				rand_CPack_Y = round(random.randrange(0, display_height-10)/10.0) * 10.0
			if(self.player.player_y > rand_CPack_Y and self.player.player_y < rand_CPack_Y + 15):
				self.player.class_packs += self.agility
				rand_CPack_X = round(random.randrange(0, display_width-10)/10.0) * 10.0
				rand_CPack_Y = round(random.randrange(0, display_height-10)/10.0) * 10.0
				print(self.player.class_packs)
			elif(self.player.player_y + 10 > rand_CPack_Y and self.player.player_y + 10 < rand_CPack_Y + 15):
				self.player.class_packs += self.agility
				rand_CPack_X = round(random.randrange(0, display_width-10)/10.0) * 10.0
				rand_CPack_Y = round(random.randrange(0, display_height-10)/10.0) * 10.0
				print(self.player.class_packs)



 