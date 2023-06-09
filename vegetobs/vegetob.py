#Vegetob Class

import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

import random
from constants import GROWING

class Vegetob:
    def __init__(self, cell):
        self.cell = cell             #every Vegetob belongs to a specific cell
        self.density = self.setInitialDensity()

    def setInitialDensity(self):
        return random.randint(0, 100) #random initial density between 0 and 100 
    
    def getDensity(self):
        return self.density
        
    def grows(self):
        self.density += GROWING #it grows by GROWING until it reaches 100
        if self.density > 100:
            self.density = 100 


