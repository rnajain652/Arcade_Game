import os
import time
from time import sleep
from screen import Screen
from paddle import Paddle
from ball import Ball
from random import randint
from input import Get, input_to

size = os.get_terminal_size()

screen = Screen(size[0], size[1])
screen.initializeGamescreen()

paddle = Paddle(int(size[0]/2))

x = paddle.getStartpaddle() 
y = paddle.getStartpaddle() + paddle.getLength() -1
mid = int((x + y)/2)
ball = Ball(screen.getGameheight()-2,randint(x, y))

x = 0
ball_free = 0
prev_time = time.time()
p_ball_time = time.time()

print("\033[2J")
while True:
    curr_time = time.time()
    c_ball_time = time.time()

    if(curr_time - prev_time >= 0.05):
        print("\033[0;0H")
        screen.printScreen(ball, paddle)
        prev_time = curr_time

    if(ball_free == 1 and c_ball_time - p_ball_time >= 1):
        ball.movement(screen)
        p_ball_time = c_ball_time
        
    inp = input_to(Get())
    if(inp == None):
        inp = ""
    if (inp == 'r' or inp == 'R'):
        if(ball_free == 0):
            ball.release(screen,paddle)
            ball_free = 1
    if (inp == 'a' or inp == 'A' or inp == 'd' or inp == 'D'):
        if(paddle.getStartpaddle() > 0 and paddle.getStartpaddle() + paddle.getLength() < screen.getGamewidth()):
            if(ball_free == 0):
                ball.initializeBall(screen,inp)
        paddle.movement(screen, inp)
    if(inp == 'x' or inp == 'X'):
        exit()

    x += 1
