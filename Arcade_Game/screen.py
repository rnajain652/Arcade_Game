import numpy as np
from colorama import init, Fore, Back, Style
from bricks import Brick, nakli_brick, sasti_brick, birla_brick, ambuja_brick
from ball import Ball

grid = [[1, 3, 2, 9, 2, 3, 1, 2],
        [2, 1, 3, 2, 3, 2, 3, 1],
        [1, 9, 2, 9, 1, 9, 1, 2],
        [2, 1, 3, 2, 3, 2, 3, 1],
        [1, 3, 2, 9, 2, 3, 1, 2],
        [2, 1, 3, 2, 3, 2, 3, 1],
        ]

row_layout = len(grid)
col_layout = len(grid[0])


class Screen():

    def __init__(self, display_width, display_height):
        self.__displaywidth = display_width
        self.__displayheight = display_height

        if display_width % 2 == 0:
            self.__gamewidth = display_width
        else:
            self.__gamewidth = display_width - 1

        self.__gameheight = display_height - 7
        self.__game = []
        self.bricks = []

    def getDisplaywidth(self):
        return self.__displaywidth

    def getDisplayheight(self):
        return self.__displayheight

    def getGamewidth(self):
        return self.__gamewidth

    def getGameheight(self):
        return self.__gameheight

    def setGamescreen(self, x, y, ch):
        self.__game[x][y] = ch
        return

    def initializeGamescreen(self):
        brick_width = int(self.__gamewidth / 8)

        for i in range(row_layout):
            for j in range(col_layout):
                if(grid[i][j] == 1):
                    self.bricks += [nakli_brick(i * 2, j * brick_width)]
                if(grid[i][j] == 2):
                    self.bricks += [sasti_brick(i * 2, j * brick_width)]
                if(grid[i][j] == 3):
                    self.bricks += [birla_brick(i * 2, j * brick_width)]
                if(grid[i][j] == 9):
                    self.bricks += [ambuja_brick(i * 2, j * brick_width)]

        for i in range(self.__gameheight):
            curr_row = []
            for j in range(self.__gamewidth):
                curr_row.append(Back.BLACK)
            self.__game += [curr_row]
        self.__game = np.asarray(self.__game)
        return

    def getGame(self):
        return self.__game

    def printScreen(self, ball, paddle):
        # header
        current_row = "ARCADE GAME : Player1"
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
              current_row.center(self.__displaywidth)+Style.RESET_ALL)
        current_row = " "
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
              current_row.center(self.__displaywidth))

        # scorecard
        current_row = ("Lives: " + str(paddle.getLives()) + " | " + "Score: " +
                       str(paddle.getScore()) + " | " + "Time: " + str(paddle.getTimetaken()))
        print(Fore.WHITE + Back.RED + Style.BRIGHT +
              current_row.center(self.__displaywidth) + Style.RESET_ALL)
        # print(Back.BLACK + Back.RESET)
        
        for i in range(self.__displaywidth):
            print(Back.BLACK + " ", end='')

        # bricks layout
        brick_width = int(self.__displaywidth / 8)

        x = 0
        while x < len(self.bricks):
            for i in range(brick_width):
                for b in range(brick_width):
                    if self.bricks[x].getStrength() <= 0:
                        self.__game[self.bricks[x].getXposition(
                        )][self.bricks[x].getYposition() + b] = Back.BLACK
                        self.__game[self.bricks[x].getXposition(
                        ) + 1][self.bricks[x].getYposition() + b] = Back.BLACK
                    else:
                        self.__game[self.bricks[x].getXposition(
                        )][self.bricks[x].getYposition() + b] = self.bricks[x].getColor()
                        self.__game[self.bricks[x].getXposition(
                        ) + 1][self.bricks[x].getYposition() + b] = self.bricks[x].getColor()
            x += 1

        # ball
        self.__game[ball.getXposition()][ball.getYposition()] ='O'

        # paddle line
        x = paddle.getStartpaddle()
        while x < paddle.getStartpaddle() + paddle.getLength():
            self.__game[self.__gameheight-1][x] = Back.CYAN
            x += 1

        # print
        for i in range(self.__gameheight):
            num = self.__gamewidth
            if(i==ball.getXposition() and i != self.__gameheight -1 ):
                num = self.__gamewidth -1
            for j in range(num):
                print(self.__game[i][j] + " ", end='')


        # footer
        print(Back.WHITE + Fore.RED + Style.BRIGHT +
              "A: left | D: right | <space>: release ball | X: quit" + Style.RESET_ALL)

        return

    def gameover(self):
        print("\033[2J")
        print('Game over')
        exit()
        return