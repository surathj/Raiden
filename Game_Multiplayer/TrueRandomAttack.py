import GameObject
import random
import time
import Block
import Renderer
import AttackUnitMover as AUM
import Socket_Client as sock

socket_data = sock.Sock_Con()

gameObject = GameObject.GameObject()
red = (255,0,0)
display_width = 800
display_height = 600

class AttackBlock(Block.Block):
	def __init__(self, direction, speed, socket_data_list):
		self.socket_data_list = socket_data_list
		self.color = red
		self.direction = direction
		self.speed = speed
		self.damage_point = gameObject.damage_point

		self.top_attack_startx = 0
		self.bottom_attack_startx = 0
		self.left_attack_starty = 0
		self.right_attack_starty = 0

		self.x = 0
		self.y = 0
		self.end_x = 0
		self.end_y = 0
		self.isActive = True
		self.renderer = Renderer.Renderer()
		self.aum = AUM.AttackUnitMover()
		self.aum.initialize(self)

		self.top_side_attack_config = []	#configuration for top attack
		self.left_side_attack_config = []	#configuration for left attack
		self.bottom_side_attack_config = []	#configuration for bottom attack
		self.right_side_attack_config = []	#configuration for right attack

		self.create_attack_start_list()		#initializes attack data from server
		self.create_attack_config()			#populates attack config lists

	def create_attack_config(self):
		if(self.direction == "top"):
			self.top_side_attack_config = [self.create_top_attack(), 0, 10, 10]
			self.end_x = self.top_side_attack_config[0]
			self.end_y = gameObject.display_height
		elif(self.direction == "left"):
			self.left_side_attack_config = [0, self.create_left_attack(), 10, 10]
			self.end_x = gameObject.display_width
			self.end_y = self.left_side_attack_config[1]
		elif(self.direction == "bottom"):
			self.bottom_side_attack_config = [self.create_bottom_attack(), gameObject.display_height-10, 10, 10]
			self.end_x = self.bottom_side_attack_config[0]
			self.end_y = self.bottom_side_attack_config[1] - gameObject.display_height -10
		else:
			self.right_side_attack_config = [gameObject.display_width-10, self.create_right_attack(), 10 , 10]
			self.end_x = self.right_side_attack_config[0] - gameObject.display_width - 10
			self.end_y = self.right_side_attack_config[1]

	

	def create_attack_start_list(self):
		self.top_a = 0
		self.left_a = 0
		self.bottom_a = 0
		self.right_a = 0

		#socket_data.get_attack()
		self.top_a = self.socket_data_list #socket_data.data_list[0]
		self.left_a = self.socket_data_list #socket_data.data_list[1]
		self.bottom_a = self.socket_data_list#socket_data.data_list[2]
		self.right_a = self.socket_data_list #socket_data.data_list[3]

	def create_top_attack(self):
		self.top_attack_startx = self.top_a #random.randrange(0, gameObject.display_width)
		return self.top_attack_startx

	def create_bottom_attack(self):
		self.bottom_attack_startx = self.bottom_a #random.randrange(0, gameObject.display_width)
		return self.bottom_attack_startx

	def create_left_attack(self):
		self.left_attack_starty = self.left_a #random.randrange(0, gameObject.display_height)
		return self.left_attack_starty

	def create_right_attack(self):
		self.right_attack_starty = self.right_a #random.randrange(0, gameObject.display_height)
		return self.right_attack_starty

	def update_attack_block_coordinates(self):
		#self.aum.initialize(self)
		self.aum.move()

	#create/update new attack block position 
	def update_attack_block_position(self, pgm, gameDisplay, color):
		self.renderer.initialize(self, pgm, gameDisplay, color, None, None)
		self.renderer.render_object()

	def damage(self, player):
		if(self.isActive == True):
			if(player.player_x > self.x and player.player_x < self.x + 10 or player.player_x + 10 > self.x and player.player_x + 10 < self.x + 10):
				if(player.player_y > self.y and player.player_y < self.y + 10):
					player.health -= self.damage_point
					print(player.player_x, " ", self.x, " ", player.player_y, " ", self.y, " : ", player.health)
					print("Player Health: ", player.health)
				elif(player.player_y + 10 > self.y and player.player_y + 10 < self.y + 10):
					player.health -= self.damage_point
					print(player.player_x, " ", self.x, " ", player.player_y, " ", self.y, " : ", player.health)
					print("Player Health: ", player.health)




