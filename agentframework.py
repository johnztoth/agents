""" agentframework.py """

import random

class Agent():
    """ initialise and move an agent object"""
    
    def __init__ (self):
        """ initialise the agent object with a randon position """
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)

    
    def move(self):
        """ randonly move the agent by one unit in x and y direction """
        """ if the agent moves over 99 shift position to 0 """
        """ if the agent moves under 0 shift position to 99 """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
    

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def dely(self):
        del self._y

    y = property(gety, sety, dely, "I'm the 'y' property.")
    
    