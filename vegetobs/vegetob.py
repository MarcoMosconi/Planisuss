import random
import constants

class Vegetob:
    def __init__(self, cell):
        self.cell = cell
        self.density = self.setInitialDensity()

    def setInitialDensity(self):
        return random.randint(0, 100)
    
    def getDensity(self):
        return self.density
        
    def grow(self):
        self.density += constants.GROWING
        if self.density > 100:
            self.density = 100 


