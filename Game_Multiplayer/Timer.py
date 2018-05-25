from time import sleep
from multiprocessing import Process, Value, Lock
import pygame as pg

class Timer():
	def __init__(self, initval=0):
		self.val = Value('i', initval)
		self.lock = Lock()

	def count_down(self):
		with self.lock:
			self.val.value -=1
			print("from counter1 thread: ", self.val.value)

	def value(self):
		with self.lock:
			return self.val.value
			
display_width = 500
display_height = 500

class Pipe():
	def __init__(self, timer):
		self.timer = timer

	def print_timer_val(self):
		gameDisplay = pg.display.set_mode((display_width, display_height)) 
		pg.display.set_caption('Block Hunger Games')
		gameDisplay.fill((255,255,255))
		pg.display.update()
		self.num = self.timer.value()
		if(self.num < 10):
			print("Timer value has reached milestone: ", self.timer.value())

def dec_func(timer):
	for i in range(0,20):
		timer.count_down()
		sleep(1)

def pipe_val(pipe):
	for i in range(0,20):
		pipe.print_timer_val()
		sleep(1)

if __name__ == '__main__':
	timer = Timer(20)
	pipe = Pipe(timer)
	p1 = Process(target=dec_func, args=(timer,))
	p2 = Process(target=pipe_val, args=(pipe,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()

