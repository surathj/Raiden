from socketIO_client import SocketIO, LoggingNamespace
import json
from multiprocessing import Process
from threading import Thread


 
socketIO = SocketIO('localhost', 3000)


class Sock_Con:
	def __init__(self):
		self.data_list = []
		self.player_ids = []
		self.attack_list = []
		self.other_player_locations = []
		self.num = 0


	def on_aaa_response(self, *args): #a string is returned
		self.data_list = args[0]
		print(self.data_list)
		print(len(self.data_list))
		#print(self.data_list['is_registered'])
		#print(self.data_list['game_ready'])

	def on_attack_response(self, *args):
		self.attack_list = args[0]
		#print(type(self.attack_list))

	def on_new_player(self, *args):
		new_player_id = args[0]
		self.player_ids.append(new_player_id)
		print(self.player_ids)

	def on_move_response(self, *args):
		self.other_player_locations.append(args[0])
		print(args[0])
		print(type(args[0]))
		self.num += 1
		print(self.num)



	#called first on program start
	def create_game(self):
		socketIO.emit('register', {'client_message' : 'rq_game'})
		socketIO.on('on_aaa_response', self.on_aaa_response)
		socketIO.wait(seconds=10)

	#register client for created game
	def register_client(self):
		socketIO.emit('register', {'client_token' : 'ABCD'})
		socketIO.on('reg_data', self.on_aaa_response)
		socketIO.on('on_attack_response', self.on_attack_response)
		socketIO.wait(seconds=1)

	#attack unit coordinates
	def get_attack(self):
		socketIO.emit('attack', {'client_message' : 'request for attack data'})
		socketIO.on('on_aaa_response', self.on_aaa_response)
		socketIO.on('new_player', self.on_new_player)
		socketIO.wait(seconds=1)

	#data for startup
	def get_config_data(self):
		socketIO.emit('config_data', {'client_message' : 'request for config data'})
		socketIO.on('on_aaa_response', self.on_aaa_response)
		socketIO.wait(seconds=1)

	#data from AI engine to update environ variables
	def update_environment(self):
		socketIO.emit('update_environment', {'client_message' : 'request to update environment'})
		socketIO.on('on_aaa_response', self.on_aaa_response)
		socketIO.wait(seconds=1)

	#push to broadcast player location
	def player_moved(self, vector_x, vector_y):
		socketIO.emit('player_moved', (vector_x, vector_y))
		socketIO.on('get_player_location', self.on_move_response)

	'''def get_player_locations(self):
		socketIO.on('get_player_location', self.on_move_response)'''

	def new_player(self):
		socketIO.on('new_player', self.on_new_player)
		socketIO.wait(seconds=1)

	def send_player_profile(self, player_profile):
		print(player_profile)
		socketIO.emit('player_profile', player_profile)

'''def main():
	sc = Sock_Con()
	t1 = Thread(target=sc.get_player_location)
	t1.start()
	#sc.register_client()
	#sc.get_attack()
	for i in range(200):
		sc.push_player_location(2,3)
		print("pushed ", sc.num)
		time.sleep(1)
	t1.join()

main()'''

