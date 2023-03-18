import random
import constants

TYPES = ["Water", "Ground"]

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y =  y
        self.type = self.setType()
    
    def getCoordinates(self):
        print(self.x)
        print(self.y)  
  
    def getType(self):
        return self.type 

    def setType(self):
        if self.x == 0 or self.x == (constants.NUMCELLS -1):
            return "Water" 
        if self.y == 0 or self.y == (constants.NUMCELLS -1):
            return "Water"
        return random.choice(TYPES)
    def isGround(self):
        return self.type == "Ground"


