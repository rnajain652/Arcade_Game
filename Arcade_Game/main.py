import os
import time
from time import sleep
from screen import Screen
from paddle import Paddle
from input import Get, input_to

size = os.get_terminal_size()

paddle = Paddle(int(size[0]/2))

screen = Screen(size[0], size[1])
screen.initializeGamescreen()

x = 0
ch = ''
prev_time = time.time()
print("\033[2J")

while True:
    curr_time = time.time()
    if(curr_time- prev_time >= 0.05):
        print("\033[0;0H")
        screen.printScreen(paddle)
        prev_time=curr_time
    inp = input_to(Get())
    if(inp == None):
        inp = ""
    # if (inp == 'r' or inp == 'R'):
        #ball release
    if (inp == 'a' or inp == 'A' or inp == 'd' or inp == 'D'):
        paddle.movement(screen, inp)
    if(inp == 'q' or inp == 'Q'):
        exit() 
    x += 1