#Vegetob Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import GROWING, MAX_DENSITY
import math

class Vegetob:
    def __init__(self, cell):
        self.cell = cell             #every Vegetob belongs to a specific cell
        self.density = self.setInitialDensity()

    def setInitialDensity(self):
        return random.randint(0, MAX_DENSITY) #random initial density between 0 and MAX_DENSITY 
    
    def getDensity(self):
        return self.density
        
    def grows(self):
        self.density += GROWING #it grows by GROWING until it reaches 100
        if self.density > MAX_DENSITY:
            self.density = MAX_DENSITY 

    def graze(self, value):
        if self.getDensity() >= value:
            self.density -= value
            return value
        else:
            availableDensity = math.ceil(self.density)
            self.density = 0
            return availableDensity

