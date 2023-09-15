#Vegetob Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import parameters
import math

class Vegetob:
    def __init__(self, cell):
        self.cell = cell             #every Vegetob belongs to a specific cell
        self.density = self.setInitialDensity()

    def setInitialDensity(self):
        return random.randint(0, parameters.getMaxDensity()) #random initial density between 0 and parameters.getMaxDensity() 
    
    def getDensity(self):
        return self.density
        
    def grows(self):
        self.density += parameters.getGrowing() #it grows by parameters.getGrowing() until it reaches 100
        if self.density > parameters.getMaxDensity():
            self.density = parameters.getMaxDensity() 

    def graze(self, value):
        if self.getDensity() >= value:
            self.density -= value
            return value
        else:
            availableDensity = math.ceil(self.density)
            self.density = 0
            return availableDensity

