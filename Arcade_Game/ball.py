from colorama import init, Fore, Back, Style
from random import randint


class Ball():
    def __init__(self, x, y):
        self.__xposition = x
        self.__yposition = y
        self.__xvelocity = 1
        self.__yvelocity = 1
        self.__speed = 0.25
        self.__free = 0

    def getfree(self):
        return self.__free

    def getXposition(self):
        return self.__xposition

    def getYposition(self):
        return self.__yposition

    def getXvelocity(self):
        return self.__xvelocity

    def getYvelocity(self):
        return self.__yvelocity

    def getSpeed(self):
        return self.__speed

    def initializeBall(self, screen, inp):
        self.removeBall(screen)
        if(inp == 'a' or inp == 'A'):
            self.__yposition -= 1
        elif(inp == 'd' or inp == 'D'):
            self.__yposition += 1
        screen.setGamescreen(self.__xposition, self.__yposition, 'O')

    def setBall(self, screen, x, y):
        screen.setGamescreen(x, y, 'O')
        return

    def removeBall(self, screen):
        screen.setGamescreen(self.__xposition, self.__yposition, Back.BLACK)
        return

    def CollisionwithWall(self, paddle, screen, ch):
        # k1 = min(self.__xposition, self.__xposition + self.__xvelocity)
        # k2 = max(self.__xposition, self.__xposition + self.__xvelocity)
        # k3 = min(self.__yposition, self.__yposition + self.__yvelocity)
        # k4 = max(self.__yposition, self.__yposition + self.__yvelocity)
        # for i in range(k1, k2):
        #     for j in range(k3, k4):
        #         if(j >= screen.getGamewidth() -1):
        #             self.__yvelocity = -self.__yvelocity
        #             break
        #         elif(j <= 0):
        #             self.__yvelocity = -self.__yvelocity
        #             break
        #         elif(i <= 0):
        #             self.__xvelocity = -1 * self.__xvelocity
        #             break
        #         if( j != k4):
        #             break

        if(ch == 'd'):
            paddle.setLive()
            paddle.removepaddle(screen)
            paddle.setStartpaddle(int(screen.getGamewidth()/2))
            if(paddle.getLives() <= 0):
                screen.gameover()
            x = paddle.getStartpaddle() 
            y = paddle.getStartpaddle() + paddle.getLength() -1
            # mid = int((x + y)/2)
            self.__free = 0
            self.__xposition = screen.getGameheight()-2
            self.__yposition = randint(x, y)
            self.__xvelocity = 1
            self.__yvelocity = 1

        if(ch == 'u'):
            self.__xvelocity = -self.__xvelocity
            self.__xposition = self.__xposition + self.__xvelocity

        if(ch == 'r'):
            self.__yvelocity = -self.__yvelocity
            self.__yposition = self.__yposition + self.__yvelocity
        # print('\nchanged:')
        # print(self.__xposition)
        # print(self.__yposition)
        if(ch == 'l'):
            self.__yvelocity = -self.__yvelocity
            self.__yposition = self.__yposition + self.__yvelocity        
        return

    def collisionCheck(self, screen, paddle):
        # print('\nin:')
        # print(self.__xposition)
        # print(self.__yposition)
        if(self.__xposition < 0):
            self.CollisionwithWall(paddle, screen, 'u')
        if(self.__xposition >= screen.getGameheight()):
            self.CollisionwithWall(paddle, screen, 'd') 
        if(self.__yposition >= screen.getGamewidth()):
            self.CollisionwithWall(paddle, screen, 'r')
        if(self.__yposition <= 0):
            self.CollisionwithWall(paddle, screen, 'l')
        return

    def release(self, screen, paddle):
        x = paddle.getStartpaddle()
        l = paddle.getLength()
        mid = int((x + (x+l))/2)

        self.__xvelocity = -1 * self.__xvelocity
        if(self.__yposition < mid):
            self.__yvelocity = -1 * self.__yvelocity
        else:
            self.__yvelocity = self.__yvelocity
        
        self.__free = 1
        # print('release')
        # print(self.__xposition)
        # print(self.__yposition)
        return

    def movement(self, screen, paddle):
        self.removeBall(screen)
        self.__xposition += self.__xvelocity
        self.__yposition += self.__yvelocity
        # print('move')
        # print(self.__xposition)
        # print(self.__yposition)
        self.collisionCheck(screen, paddle)
        self.setBall(screen, self.__xposition, self.__yposition)
       
        return