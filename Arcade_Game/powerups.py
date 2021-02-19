class Powerups():
    def __init(self,x,y):
        self.__moving = 0
        self.__activated = 0
        self.__xposition = x
        self.__yposition = y
        self.__activetime = 10

    def getActivated(self):
        return self.__activated

    def getXposition(self):
        return self.__xposition

    def getYposition(self):
        return self.__yposition