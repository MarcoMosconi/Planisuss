#Cell class

import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

import random
import constants

TYPES = ["Water", "Ground"]

class Cell:
    def __init__(self, x, y): #every cell has coordinates x and y and a type got from the fun setType
        self.x = x
        self.y =  y
        self.type = self.setType()
    
    def getCoordinates(self):
        print(self.x)
        print(self.y)  
  
    def getType(self):
        return self.type 

    def setType(self):
        if self.x == 0 or self.x == (constants.NUMCELLS -1): #boundary cells are always water
            return "Water" 
        if self.y == 0 or self.y == (constants.NUMCELLS -1):
            return "Water"
        return random.choice(TYPES) #if it's not boundary it's a random choise between the array TYPES
    
    def isGround(self):
        return self.type == "Ground"


