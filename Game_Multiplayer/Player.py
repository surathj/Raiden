import pygame as pg
import Renderer


class Player():
	def __init__(self):
		self.player_class = 0
		self.player_id = None
		self.player_x = 300
		self.player_y = 300
		self.player_lead_x_change = 0
		self.player_lead_y_change  =0

		self.previous_x = 0
		self.previous_y = 0

		#Server response flag
		self.is_registered = False
		#self.ammo = ammo

		self.time_lasted = 0
		self.average_performance = 0

		#Feature variables
		self.health = 100
		self.score = 0			#measures endurance against remaining health
		self.class_packs = 0	#measures agility
		self.out_of_bounds_OR_game_over = 0
		
		#apply game rules, violation of which will cost something
		#resourcefulness
		#ammo and shields
		self.renderer = Renderer.Renderer()


	def draw_player_block(self, pgm, gameDisplay, color, config_list):
		self.renderer.initialize(self, pgm, gameDisplay, color, config_list, None)
		self.renderer.render_object()

	def has_moved(self):
		if(self.previous_x != self.player_x or self.previous_y != self.player_y):
			return True
		else:
			return False

	def check_health(self):
		print(self.health)
		if(self.health == 0):
			return 1

	def get_score(self):
		return self.score

	def register_with_server(self, sc):
		sc.register_client()
		player_status = sc.data_list['is_registered']
		game_status = sc.data_list['game_ready']
		return int(game_status)