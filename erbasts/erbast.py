#Erbast Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import MAX_ENERGY, MAX_LIFE, AGING

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
        isAlive = True
        self.age += 1
        if self.age != 0 and self.age%10 == 0:
                self.energy -= AGING
        if self.energy <= 0 or self.age == self.lifetime:
            isAlive = False 
        return isAlive, self.energy
    
    def grazes(self):
        self.energy += 1            


    