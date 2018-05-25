from tkinter import *
import pygame
import random
import os
import game


root = Tk()
embed = Frame(root, width=800, height=600)
embed.grid(row=0,column=2)
root.update()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
#pygame.display.init()
#screen = pygame.display.set_mode((640,480))
#pygame.display.flip()
#while True:
    #your code here
    #screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    #pygame.display.flip()
myg = game.Game()
myg.gameloop()
root.mainloop()