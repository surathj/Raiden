import TrueRandomAttack as tra
import GameObject
import Timer
import time
import random
import Socket_Client


directions = ["top", "left", "bottom", "right"]
speeds = [7,8,9,10]
gameObject = GameObject.GameObject()

red = (255,0,0)

#Global functions
def select_random_direction():
	direction = random.choice(directions)
	return direction


def select_random_speed():
	speed = random.choice(speeds)
	return speed


class Attack_Wave():
	def __init__(self, pg, gameDisplay, color, units_per_wave):
		self.pg = pg
		self.gameDisplay = gameDisplay
		self.color = color
		self.wave_isActive = False
		self.units_per_wave = units_per_wave
		self.attack_block_list = []
		self.sc = Socket_Client.Sock_Con()

		print("inside an attack wave")

	def generate_wave(self):
		self.sc.get_attack()
		wave_size = len(self.sc.data_list)
		print(wave_size)
		for wave_number in range(0, wave_size):
			print("generating")
			for block_coordinate_index in range(0, len(self.sc.data_list[wave_number])):
				if(block_coordinate_index == 0):
					attack_unit =  tra.AttackBlock("top", select_random_speed(), self.sc.data_list[wave_number][block_coordinate_index])
					self.attack_block_list.append(attack_unit)
				elif(block_coordinate_index == 1):
					attack_unit =  tra.AttackBlock("left", select_random_speed(), self.sc.data_list[wave_number][block_coordinate_index])
					self.attack_block_list.append(attack_unit)
				elif(block_coordinate_index == 2):
					attack_unit =  tra.AttackBlock("bottom", select_random_speed(), self.sc.data_list[wave_number][block_coordinate_index])
					self.attack_block_list.append(attack_unit)
				elif(block_coordinate_index == 3):
					attack_unit =  tra.AttackBlock("right", select_random_speed(), self.sc.data_list[wave_number][block_coordinate_index])
					self.attack_block_list.append(attack_unit)
		return True

	def update_wave_coordinates(self):
			self.wave_isActive = True
			for i in self.attack_block_list:
					i.update_attack_block_coordinates()

	def update_wave_positions(self):
		if(self.wave_isActive):
			for i in self.attack_block_list:
					i.update_attack_block_position(self.pg, self.gameDisplay, self.color)

	def damage_player(self, player):
		for i in self.attack_block_list:						
			i.damage(player)
			if(player.health <= 0):
				return 1

	def reset_attack_wave(self, delta=None):
		#always change for attack configuration, not for instance variables
		for i in self.attack_block_list:
			if(i.direction == "top"):
				if(i.top_side_attack_config[1] == i.end_y):
					i.top_side_attack_config[1] = 0
				#self.top_reset_recursion(i)
			elif(i.direction == "bottom"):
				if(i.bottom_side_attack_config[1] == i.end_y):
					i.bottom_side_attack_config[1] = gameObject.display_height
				#self.bottom_reset_recursion(i)
			elif(i.direction == "left"):
				if(i.left_side_attack_config[0] == i.end_x):
					i.left_side_attack_config[0] = 0
				#self.left_reset_recursion(i)
			else:
				if(i.right_side_attack_config[0] == i.end_x):
					i.right_side_attack_config[0] = gameObject.display_width
				#self.right_reset_recursion(i)

	def top_reset_recursion(self, i):
		x = random.choice(range(-100, 100))
		if(i.top_side_attack_config[0] + x >= gameObject.display_width or i.top_side_attack_config[0] + x <= 0):
			self.top_reset_recursion(i)
		else:
			i.top_side_attack_config[0] += x

	def bottom_reset_recursion(self, i):
		x = random.choice(range(-100, 100))
		if(i.bottom_side_attack_config[0] + x >= gameObject.display_width or i.bottom_side_attack_config[0] + x <= 0):
			self.bottom_reset_recursion(i)
		else:
			i.bottom_side_attack_config[0] += x

	def left_reset_recursion(self, i):
		x = random.choice(range(-100, 100))
		if(i.left_side_attack_config[1] + x >= gameObject.display_height or i.left_side_attack_config[1] + x <= 0):
			self.left_reset_recursion(i)
		else:
			i.left_side_attack_config[1] += x

	def right_reset_recursion(self, i):
		x = random.choice(range(-100, 100))
		if(i.right_side_attack_config[1] + x >= gameObject.display_height or i.right_side_attack_config[1] + x <= 0):
			self.right_reset_recursion(i)
		else:
			i.right_side_attack_config[1] += x
