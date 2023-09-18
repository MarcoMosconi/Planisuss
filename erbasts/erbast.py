#Erbast Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from parameters import parameters
from animals.animal import Animal

class Erbast(Animal):
    def __init__(self, cell, energy = None, lifetime = None, socialAttitude = None):
        super().__init__(cell, energy, lifetime, socialAttitude)
    
    def grazes(self):
        if not self.moved:
            if self.energy < parameters.getMaxEnergy():
                self.energy += 1
        else:
            self.moved = False   

