from colorama import init, Fore, Back, Style

colormap = {
    0: Back.BLACK,
    1: Back.MAGENTA,
    2: Back.RED,
    3: Back.YELLOW,
    9: Back.WHITE
}


class Brick():
    def __init__(self, x, y):
        self.__xposition = x
        self.__yposition = y
        self._base_activated = 1

    def getXposition(self):
        return self.__xposition

    def getYposition(self):
        return self.__yposition

    def getActivated(self):
        return self._base_activated

    def setActivated(self):
        self._base_activated = 0
        return

class nakli_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__strength = 1
        self.__color = colormap[self.__strength]
        return

    def collision(self, screen,paddle):
        paddle.setScore()
        self.__strength -= 1
        self.__color = colormap[self.__strength]
        if(self.__strength <= 0):
            self._base_activated = 0
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

    def collision(self, screen,paddle):
        paddle.setScore()
        self.__strength -= 1
        self.__color = colormap[self.__strength]
        if(self.__strength <= 0):
            self._base_activated = 0
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

    def collision(self, screen,paddle):
        paddle.setScore()
        self.__strength -= 1
        self.__color = colormap[self.__strength]
        if(self.__strength <= 0):
            self._base_activated = 0
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
