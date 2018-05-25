import TrueRandomAttack as Tra
import Player
import ClassPack
import time
import random
import GameObject

gameObject = GameObject.GameObject()
rand_CPack_X = round(random.randrange(0, gameObject.display_width-10)/10.0) * 10.0
rand_CPack_Y = round(random.randrange(0, gameObject.display_height-10)/10.0) * 10.0

class Renderer(object):
	def initialize(self, obj, pgm, gameDisplay, color, config_list = None, player = None):
		self.obj = obj
		self.pgm = pgm
		self.gameDisplay = gameDisplay
		self.color = color
		if(config_list != None):
			self.config_list = config_list
		if(player != None):
			self.player = player

	def render_object(self):
		if(isinstance(self.obj, Tra.AttackBlock)):
			if(self.obj.isActive == True):
				if(self.obj != None):
					if(self.obj.direction == "top"):
						self.pgm.draw.rect(self.gameDisplay, self.color, self.obj.top_side_attack_config)
					elif(self.obj.direction == "left"):
						self.pgm.draw.rect(self.gameDisplay, self.color, self.obj.left_side_attack_config)
					elif(self.obj.direction == "bottom"):
						self.pgm.draw.rect(self.gameDisplay, self.color, self.obj.bottom_side_attack_config)
					else:
						self.pgm.draw.rect(self.gameDisplay, self.color, self.obj.right_side_attack_config)
				else:
					print(self.obj, " is None")
		elif(isinstance(self.obj, Player.Player)):
			self.pgm.draw.rect(self.gameDisplay, self.color, self.config_list)
		elif(isinstance(self.obj, ClassPack.ClassPack)):
			pass




