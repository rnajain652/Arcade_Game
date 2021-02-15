from colorama import init, Fore, Back, Style
from random import randint


class Ball():
    def __init__(self, x, y):
        self.__xposition = x
        self.__yposition = y
        self.__xvelocity = 1
        self.__yvelocity = 1

    def getXposition(self):
        return self.__xposition

    def getYposition(self):
        return self.__yposition

    def getXvelocity(self):
        return self.__xvelocity

    def getYvelocity(self):
        return self.__yvelocity

    def initializeBall(self, screen, inp):
        self.removeBall(screen)
        if(inp == 'a' or inp == 'A'):
            self.__yposition -= 1
        elif(inp == 'd' or inp == 'D'):
            self.__yposition += 1        
        screen.setGamescreen(self.__xposition, self.__yposition,'O')

    def setBall(self, screen, x, y):
        screen.setGamescreen(x, y,'O')
        return

    def removeBall(self, screen):
        screen.setGamescreen(self.__xposition, self.__yposition, Back.BLACK)
        return

    def movement(self,screen):
        self.removeBall(screen)
        self.__xposition +=self.__xvelocity
        self.__yposition += self.__yvelocity
        self.setBall(screen, self.__xposition, self.__yposition)
        return

    def release(self,screen,paddle):
        x = paddle.getStartpaddle()
        l = paddle.getLength()
        mid = int((x + (x+l))/2)

        self.__xvelocity = -1 * self.__xvelocity
        if(self.__yposition < mid):
            self.__yvelocity = -1 * self.__yvelocity
        else:
            self.__yvelocity = self.__yvelocity
        return

    def CollisionwithPaddle(self, paddle):
        x = paddle.getStartpaddle()
        l = paddle.getLength()
        mid = int((x + (x+l))/2)
        
        return
        