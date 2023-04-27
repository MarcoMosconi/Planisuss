#Erbast Class

import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

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
            

    # def grows(self):
    #     self.age += 1
    #     if self.age == self.lifetime:
    #          self.dead = True
    #          for cellname in erbasts:
    #             erbasts[cellname] = None

    # def moves(self):
    #     self.energy -= 1
    #     if self.density <= 0:
    #         self.dead = True
    #         for cellname in erbasts:
    #             erbasts[cellname] = None

    