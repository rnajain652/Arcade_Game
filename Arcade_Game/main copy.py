import time

import os
from colorama import init, Fore, Back, Style

colormap = {
    1: Back.MAGENTA,
    2: Back.RED,
    3: Back.BLACK,
    9: Back.WHITE
}

grid = [[1, 3, 2, 9, 2, 3, 1, 2],
        [2, 1, 3, 2, 3, 2, 3, 1],
        [1, 9, 2, 9, 1, 9, 1, 2],
        [2, 1, 3, 2, 3, 2, 3, 1],
        [1, 3, 2, 9, 2, 3, 1, 2],
        [2, 1, 3, 2, 3, 2, 3, 1],
        ]

size = os.get_terminal_size()


class Brick():
    def __init__(self, x, y):
        self.__xposition = x
        self.__yposition = y

    def getXposition(self):
        return self.__xposition

    def getYposition(self):
        return self.__yposition


class nakli_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__strength = 1
        self.__color = colormap[self.__strength]
        return

    def getStrength(self):
        return self.__strength

    def getColor(self):
        return self.__color


class sasti_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__strength = 2
        self.__color = colormap[self.__strength]
        return

    def getStrength(self):
        return self.__strength

    def getColor(self):
        return self.__color


class birla_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__strength = 3
        self.__color = colormap[self.__strength]
        return

    def getStrength(self):
        return self.__strength

    def getColor(self):
        return self.__color


class ambuja_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__strength = 9
        self.__color = colormap[self.__strength]
        return

    def getStrength(self):
        return self.__strength

    def getColor(self):
        return self.__color


display_width = size[0]
display_height = size[1]

if(display_height % 2 != 0):
    display_height -= 1

if(display_width % 2 != 0):
    display_width -= 1

live = 3
score = 10
timetaken = 1
start_paddle = display_width/2
game = []

current_row = " "
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + current_row.center(display_width))
current_row = "ARCADE GAME : Player1"
print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
      current_row.center(display_width)+Style.RESET_ALL)

current_row = " "
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + current_row.center(display_width))

current_row = "Lives: " + \
    str(live) + " | " + "Score: " + str(score) + \
    " | " + "Time: " + str(timetaken)
print(Fore.WHITE + Back.RED + Style.BRIGHT +
      current_row.center(display_width) + Style.RESET_ALL)
print(Back.BLACK + Back.RESET)

row_layout = len(grid)
col_layout = len(grid[0])

brick_height = 2
brick_width = int(display_width / col_layout)

# for i in range(brick_height):
#     for j in range(brick_width):
#         print(Back.RED + " ", end ='')
#     print(Back.BLACK + Back.RESET)
# print(Back.BLACK + Back.RESET)

bricks = []
for i in range(row_layout):
    for j in range(col_layout):
        if(grid[i][j] == 1):
            bricks += [nakli_brick(i, j)]
        if(grid[i][j] == 2):
            bricks += [sasti_brick(i, j)]
        if(grid[i][j] == 3):
            bricks += [birla_brick(i, j)]
        if(grid[i][j] == 9):
            bricks += [ambuja_brick(i, j)]

x = 0
while x < len(bricks):
    for j in range(brick_width):
        print(bricks[x].getColor() + " ", end='')
        print(Back.BLACK + Back.RESET, end='')
    print(Back.BLACK + Back.RESET, end='')
    x += 1
    if(x % col_layout == 0):
        print('\n', end='')
        print(Back.BLACK + Back.RESET, end='')
        num = x-col_layout
        while num < x:
            for j in range(brick_width):
                print(bricks[num].getColor() + " ", end='')
                print(Back.BLACK + Back.RESET, end='')
            print(Back.BLACK + Back.RESET, end='')
            num += 1
        print('\n', end='')
        print(Back.BLACK + Back.RESET, end='')
print(Back.BLACK + Back.RESET)

# print(display_height)
# print(row_layout)
# print(brick_height)
# print(row_layout * brick_height)
for i in range(display_height - (row_layout * brick_height) - 6):
    print(Back.BLACK + Back.RESET)

for i in range(display_width - 9):
    if (i != start_paddle):
        print(Back.BLACK + " ", end="")
    else:
        for j in range(10):
            print(Back.CYAN + " ", end="")

print(Back.BLACK + Back.RESET)
