import TrueRandomAttack as TRA
import random
import GameObject


gameObject = GameObject.GameObject()

class AttackUnitMover:
	def initialize(self, obj):
		self.obj = obj

	def move(self):
		if(isinstance(self.obj, TRA.AttackBlock)):
			if(self.obj.isActive == True):
				if(self.obj.direction == "top"):
					if(self.obj.top_side_attack_config[1] == self.obj.end_y):
						#self.obj = None
						#self.obj.top_side_attack_config[1] = 0
						#self.top_reset_recursion()
						pass
					else:
						self.obj.lead_top_attack_change = self.obj.speed
						self.obj.top_side_attack_config[1] += self.obj.lead_top_attack_change
						self.obj.x = self.obj.top_side_attack_config[0]
						self.obj.y = self.obj.top_side_attack_config[1]
				elif(self.obj.direction == "left"):
					if(self.obj.left_side_attack_config[0] == self.obj.end_x):
						#self.obj = None
						#self.obj.left_side_attack_config[0] = 0
						#self.left_reset_recursion()
						pass
					else:
						self.obj.lead_left_attack_change = self.obj.speed
						self.obj.left_side_attack_config[0] += self.obj.lead_left_attack_change
						self.obj.x = self.obj.left_side_attack_config[0]
						self.obj.y = self.obj.left_side_attack_config[1]
				elif(self.obj.direction == "bottom"):
					if(self.obj.bottom_side_attack_config[1] == self.obj.end_y):
						#self.obj = None
						#self.obj.bottom_side_attack_config[1] = gameObject.display_height
						#self.bottom_reset_recursion()
						pass
					else:
						self.obj.lead_bottom_attack_change = self.obj.speed
						self.obj.bottom_side_attack_config[1] -= self.obj.lead_bottom_attack_change
						self.obj.x = self.obj.bottom_side_attack_config[0]
						self.obj.y = self.obj.bottom_side_attack_config[1]
				else:
					if(self.obj.right_side_attack_config[0] == self.obj.end_x):
						#self.obj = None
						#self.obj.right_side_attack_config[0] = gameObject.display_width
						#self.right_reset_recursion()
						pass
					else:
						self.obj.lead_right_attack_change = self.obj.speed
						self.obj.right_side_attack_config[0] -= self.obj.lead_right_attack_change
						self.obj.x = self.obj.right_side_attack_config[0]
						self.obj.y  =self.obj.right_side_attack_config[1]

	'''def reset_attack_unit(self):
		if(self.obj.direction == "top"):
			self.obj.top_side_attack_config[1] = 0
			self.top_reset_recursion()
		elif(self.obj.direction == "bottom"):
			self.obj.bottom_side_attack_config[1] = gameObject.display_height
			self.bottom_reset_recursion()
		elif(self.obj.direction == "left"):
			self.obj.left_side_attack_config[0] = 0
			self.left_reset_recursion()
		else:
			self.obj.right_side_attack_config[0] = gameObject.display_width
			self.right_reset_recursion()'''

	def top_reset_recursion(self):
		x = random.choice(range(-100, 100))
		if(self.obj.top_side_attack_config[0] + x >= gameObject.display_width or self.obj.top_side_attack_config[0] + x <= 0):
			self.top_reset_recursion()
		else:
			self.obj.top_side_attack_config[0] += x
			#print(self.obj.top_side_attack_config[0])

	def bottom_reset_recursion(self):
		x = random.choice(range(-100, 100))
		if(self.obj.bottom_side_attack_config[0] + x >= gameObject.display_width or self.obj.bottom_side_attack_config[0] + x <= 0):
			self.bottom_reset_recursion()
		else:
			self.obj.bottom_side_attack_config[0] += x

	def left_reset_recursion(self):
		x = random.choice(range(-100, 100))
		if(self.obj.left_side_attack_config[1] + x >= gameObject.display_height or self.obj.left_side_attack_config[1] + x <= 0):
			self.left_reset_recursion()
		else:
			self.obj.left_side_attack_config[1] += x

	def right_reset_recursion(self):
		x = random.choice(range(-100, 100))
		if(self.obj.right_side_attack_config[1] + x >= gameObject.display_height or self.obj.right_side_attack_config[1] + x <= 0):
			self.right_reset_recursion()
		else:
			self.obj.right_side_attack_config[1] += x