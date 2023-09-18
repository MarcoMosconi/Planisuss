#Cell class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from parameters import parameters

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
        if self.x == 0 or self.x == (parameters.getNumcells() -1): #boundary cells are always water
            return "Water" 
        if self.y == 0 or self.y == (parameters.getNumcells() -1):
            return "Water"
        if random.random() > parameters.getCellProb():
            return "Ground"
        else:
            return "Water"
            
    def isGround(self):
        return self.type == "Ground"


