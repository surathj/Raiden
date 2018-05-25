from tkinter import *
import os
import game


#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)

def start_mp_game():
	mygame = game.Game()
	game.gameloop()


class Raiden_Game_UI:
	def __init__(self, master):
	
		self.embed = Frame(root, width = 850, height = 650)
		self.embed.grid(columnspan = (600), rowspan = 500)
		self.embed.pack(side = RIGHT)
		
		os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
		os.environ['SDL_VIDEODRIVER'] = 'windib'
	
		self.canvas=Canvas(root, width=850, height=650, background='white')
		self.canvas.grid(row=4,column=2, sticky=E)
		
		self.button_create = Button(root, text="Create Game", fg="red")
		self.label_create = Label(root, text="Create Game Description")
		
		self.button_start_mp = Button(root, text="Play Multiplayer", fg="red", command=start_mp_game)
		self.label_start_mp = Label(root, text="Multiplayer Description")
		
		self.button_start_sp = Button(root, text="Play Single Player", fg="red")
		self.label_start_sp = Label(root, text="Single Player Description")
		
		self.button_exit = Button(root, text="Exit", fg="red", command=frame.quit)
		self.label_exit = Label(root, text="Click to Exit")
		
		self.button_create.grid(row=0, sticky=E+N)
		self.label_create.grid(row=0, column=1, sticky=W+N)
		
		self.button_start_mp.grid(row=1, sticky=E+N)
		self.label_start_mp.grid(row=1, column=1, sticky=W+N)
		
		self.button_start_sp.grid(row=2, sticky=E+N)
		self.label_start_sp.grid(row=2, column=1, sticky=W+N)
		
		self.button_exit.grid(row=3, sticky=E+N)
		self.label_exit.grid(row=3, column=1, sticky=W+N)

#button_start_mp.pack(side=LEFT)
#button_start_sp.pack(side=LEFT)
#button_exit.pack(side=BOTTOM)

root = Tk() #init tkinter object creates blank window
game_ui = Raiden_Game_UI(root)

root.mainloop()

