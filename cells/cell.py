#Cell class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import NUMCELLS, CELL_PROBABILITY

#TYPES = ["Water", "Ground"]

class Cell:
    def __init__(self, x, y): #every cell has coordinates x and y and a type got from the fun setType
        self.x = x
        self.y =  y
        self.type = self.setType()
    
    def getCoordinates(self):
        return self.x, self.y
  
    def getType(self):
        return self.type 

    def setType(self):
        if self.x == 0 or self.x == (NUMCELLS -1): #boundary cells are always water
            return "Water" 
        if self.y == 0 or self.y == (NUMCELLS -1):
            return "Water"
        if random.random() > CELL_PROBABILITY:
            return "Ground"
        else:
            return "Water"
        #return random.choice(TYPES) #if it's not boundary it's a random choise between the array TYPES
    
    def isGround(self):
        return self.type == "Ground"


