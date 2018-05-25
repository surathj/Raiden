#all static data

class GameObject(object):
	display_width = 800
	display_height = 600
	FPS = 30
	player_block_height = 10
	player_block_width = 10
	attack_block_width = 10
	attack_block_height = 10
	damage_point = 10


class Colors(object):
	red = (255,0,0)
	white = (255,255,255)
	black = (0,0,0)
	dark_violet = (148, 0, 211)

class AttackParent(object):
	def __init__(self):
		pass


