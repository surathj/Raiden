from timeit import Timer
import AttackWaves as atw
import pygame as pg
import random
import TrueRandomAttack as tra

pg.init()
gameDisplay = pg.display.set_mode((200, 300)) 

def testlist():
	ilist = [1,2,3,4,5,6,5,5,55,5,5,5,5,5,5,55,5,5,4,3,5,6,7,8,6,5,4,3]
	ilist.sort()

waves = []

def preload_resources():
	for p in range(5):
		new_atw = atw.Attack_Wave(pg, gameDisplay, (255,255,255), random.choice(range(2,5)))
		new_atw.generate_wave()
		waves.append(new_atw)

		print(p)
attack_block_list = []
def generate_wave():
		for i in range(10):
			attack_unit = tra.AttackBlock("top", 5)
			attack_block_list.append(attack_unit)

if __name__=='__main__':
	#insert_timer = Timer("preload_resources()", "from __main__ import preload_resources")
	#insert_speed = insert_timer.timeit(loop_range)

	t = Timer('generate_wave()', "from __main__ import generate_wave")
	#elapsed = (10 * t.timeit(number=1))
	#print("Function preload_resources() takes %0.3f microseconds/pass" % elapsed)
	print(str(t.timeit(number=1)))
	
