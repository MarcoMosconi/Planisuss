#Erbast Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import MAX_ENERGY, MAX_LIFE

class Erbast:
    def __init__(self, cell, herd, energy = None):
        self.cell = cell
        self.herd = herd
        self.lifetime = self.setLifetime()
        self.socialAttitude = self.setSocialAttitude()
        self.energy = self.setInitialEnergy(energy)
        self.age = 0

    def setLifetime(self):
        return random.randint(0, MAX_LIFE)
    
    def setSocialAttitude(self):
        return random.random()
    
    def setInitialEnergy(self, energy):
        if energy == None:
            return random.randint(0, MAX_ENERGY)
        return energy

    def getEnergy(self):
        return self.energy
    
    def grows(self):
        self.age += 1
        return self.age == self.lifetime 
            


    