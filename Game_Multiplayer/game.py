'''core modules'''
import pygame as pg
import time
import random
from multiprocessing import Process, freeze_support
from time import sleep
from timeit import Timer

'''custome modules'''
import GameObject
import Player
import TrueRandomAttack as tra
import AttackWaves as atw
import ClassPack as cp
import Timer
import Socket_Client as socket

pg.init()
pg.font.init()
display_width = 800
display_height = 600

gameObject = GameObject.GameObject()
colors = GameObject.Colors()

#display x,y
#gameDisplay = pg.display.set_mode((display_width, display_height)) 
#pg.display.set_caption('Block Hunger Games')

#socket_client object
sc = socket.Sock_Con()


font = pg.font.SysFont(None, 25)


def message_to_screen(msg, color, gameDisplay):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [gameObject.display_width/2, gameObject.display_height/2])

def load_message(load_perc, gameDisplay):
	screen_text = font.render("Please wait while the game loads...", True, (255,0,0))
	screen_text2 = font.render(load_perc, True, (255,0,0))
	gameDisplay.blit(screen_text, [gameObject.display_width/2, gameObject.display_height/3])
	gameDisplay.blit(screen_text2, [gameObject.display_width/2, gameObject.display_height/2])

def find_percentage(base, amount):
	percentage = (100*amount)/base
	return percentage

def connect_and_register(player, register_flag, gameDisplay):
	gameDisplay.fill(colors.white)
	message_to_screen("Connecting to Server", colors.red)
	pg.display.update()
	if(register_flag == False):
		status = player.register_with_server(sc)
		if(status == int(80)):
			register_flag = True
			print(register_flag)
	#sc.register_client();

def end_level(player_profile, gameDisplay):
	gameDisplay.fill(colors.white)
	message_to_screen("Please wait while the next level starts with new player settings..", colors.red, gameDisplay)
	pg.display.update()
	sc.send_player_profile(player_profile)

	

now = time.time()
future = now + 2

waves = []


def preload_resources(gameDisplay):
	print("preloading")
	num = 5
	#for i in range(3):
	#	loading_str = "Loading Resources: "
	#	perc = find_percentage(3,i)
	#	perc = int(perc)
	#	percentage = str(perc)
	#	percentage += "%"
	#	loading_str += percentage 
	gameDisplay.fill(colors.white)
	message_to_screen("Connecting to Server...", colors.red, gameDisplay)
	pg.display.update()
	time.sleep(3)
	gameDisplay.fill(colors.white)
	message_to_screen("Downloading data...", colors.red, gameDisplay)
	pg.display.update()
	#	load_message(str(loading_str))
	pg.display.update()
	new_atw = atw.Attack_Wave(pg, gameDisplay, colors.red, 5)#random.choice(range(2,5))
	server_ok = new_atw.generate_wave()
	if(server_ok == True):
		waves.append(new_atw)
		'''for i in range(5):
			gameDisplay.fill(colors.white)
			pg.display.update()
			message_to_screen("Game starting in " + str(num) + " seconds...", colors.red, gameDisplay)
			pg.display.update()
			time.sleep(1)
			num -= 1'''
	else:
		message_to_screen("Error starting game", colors.red, gameDisplay)
	#waves.append(new_atw)


level_count = 0
#parameterize for level, units_per_wave
class Game(object):
	def __init__(self):		
		#self.gameDisplay = pg.display.set_mode((display_width, display_height)) 
		#pg.display.set_caption('Block Hunger Games')
		
		self.game_ready = False
		self.player = Player.Player()
		#connect_and_register(self.player, self.game_ready)
		
		self.session_players = []
		
		#this.level = level
		self.time1 = int(time.time())
		self.end1 = self.time1 + 4
		self.reset1 = False
		self.end2 = self.end1 + 4
		self.reset2 = False
		self.end3 = self.end2 + 4
		self.reset3 = False
		self.end4 = self.end3 + 4
		self.reset4 = False
		self.end5 = self.end4 + 4
		self.reset5 = False
		self.end6 = self.end5 + 4
		self.reset6 = False
		self.end7 = self.end6 + 4
		self.reset7 = False
		self.end8 = self.end7 + 4
		self.reset8 = False
		self.end9 = self.end8 + 4
		self.reset9 = False
		global level_count
		level_count += 1

	

	def gameloop(self):
		self.gameDisplay = pg.display.set_mode((display_width, display_height)) 
		pg.display.set_caption('Block Hunger Games')

		preload_resources(self.gameDisplay)

		#pg.display.update()
		gameExit = False
		gameOver = False

		clock = pg.time.Clock()
		FPS = 30

		#creating player object
		

		#creating singleton classpack
		classPack = cp.ClassPack(pg, self.gameDisplay, self.player)

		pg.mouse.set_visible(False)
		pg.event.set_blocked(pg.MOUSEMOTION)
		pg.event.set_blocked(pg.MOUSEBUTTONDOWN)
		pg.event.set_blocked(pg.MOUSEBUTTONUP)
		
		'''
		The Game loop starts here
		'''
		#game loop
		while not gameExit:
			#update block positions to simulate movement
			#self.print_timer_val()

			#####################################################################################
			#validate time boundaries and reset attack waves
			if(int(time.time()) > self.time1 + 30):
				player_profile = (self.player.health, self.player.score, self.player.class_packs, self.player.out_of_bounds_OR_game_over)
				end_level(player_profile, self.gameDisplay)
				gameExit = True
				gameOver = False

			#####################################################################################

			for i in waves:
				i.update_wave_coordinates()
				i.reset_attack_wave()


			while gameOver == True:
				self.gameDisplay.fill(colors.white)
				message_to_screen("Game Over! Press C to play again or Q to quit!", colors.red, self.gameDisplay)
				pg.display.update()

				for event in pg.event.get():
					if event.type == pg.KEYDOWN:
						if event.key == pg.K_q:
							gameExit = True
							gameOver = False
						if event.key == pg.K_c:
							now = time.time()
							game = Game()
							game.gameloop()


			#game event loop
			for event in pg.event.get():
				if event.type == pg.QUIT:
					gameExit = True
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_LEFT:
						self.player.player_lead_x_change = -10
						#lead_y_change = 0	# to avoid diagonal movement
					elif event.key == pg.K_RIGHT:
						self.player.player_lead_x_change = 10
						#lead_y_change = 0
					elif event.key == pg.K_UP:
						self.player.player_lead_y_change = -10
						#lead_x_change = 0
					elif event.key == pg.K_DOWN:
						self.player.player_lead_y_change = 10
						#lead_x_change = 0
						
				#allow keyup to stop x,y movement
				if event.type == pg.KEYUP:
					if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
						self.player.player_lead_x_change = 0
					if event.key == pg.K_UP or event.key == pg.K_DOWN:
						self.player.player_lead_y_change = 0
					#print(event)

				#boudary logic
				if(self.player.player_x >= display_width or self.player.player_x < 0 or self.player.player_y >= display_height or self.player.player_y < 0):
					self.player.out_of_bounds_OR_game_over = 1
					player_profile = (self.player.health, self.player.score, self.player.class_packs, self.player.out_of_bounds_OR_game_over)
					end_level(player_profile, self.gameDisplay)
					gameOver = True

			#update preivous positions
			self.player.previous_x = self.player.player_x
			self.player.previous_y = self.player.player_y
			#update self.player position
			self.player.player_x += self.player.player_lead_x_change
			self.player.player_y += self.player.player_lead_y_change


			#for player location broadcasting
			has_moved = self.player.has_moved()
			if(has_moved == True):
				sc.player_moved(self.player.player_x, self.player.player_y)


			for i in sc.other_player_locations:
				pg.draw.rect(self.gameDisplay, colors.dark_violet, [i[0], i[1], gameObject.player_block_width, gameObject.player_block_height])
				pg.display.update()

			self.gameDisplay.fill(colors.white)

			#self.player block
			self.player.draw_player_block(pg, self.gameDisplay, colors.black, [self.player.player_x, self.player.player_y, gameObject.player_block_width, gameObject.player_block_height])
			classPack.draw_cpack()


			for i in waves:
				i.update_wave_positions()
				result = i.damage_player(self.player)
				if(result == 1):
					self.player.out_of_bounds_OR_game_over = 1
					end_level(player_profile)
					gameOver = True
					print(gameOver)


			pg.display.update()
		
			
			#increase amount of pixels moved and reduce fps clocking
			#balance fps and x,y _change
			#current: 30 fps, 10 px/s
			clock.tick(gameObject.FPS)
		
		'''message_to_screen("You Lose", red)
		pg.display.update()
		time.sleep(2)'''		
		#pg.quit()
		quit()


if __name__ == '__main__':
	game = Game()
	game.gameloop()
	

	

