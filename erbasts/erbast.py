#Erbast Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import parameters
from animals.animal import Animal

class Erbast(Animal):
    def __init__(self, cell, energy = None, lifetime = None, socialAttitude = None):
        super().__init__(cell, energy, lifetime, socialAttitude)
    #     self.cell = cell
    #     self.lifetime = self.setLifetime()
    #     self.socialAttitude = self.setSocialAttitude()
    #     self.energy = self.setInitialEnergy(energy)
    #     self.age = 0
    #     self.moved = False

    # def setLifetime(self):
    #     return random.randint(0, parameters.getMaxLife())
    
    # def setSocialAttitude(self):
    #     return random.random()
    
    # def setInitialEnergy(self, energy):
    #     if energy == None:
    #         return random.randint(0, parameters.getMaxEnergy())
    #     return energy

    # def getEnergy(self):
    #     return self.energy
    
    # def grows(self):
    #     isAlive = True
    #     self.age += 1
    #     if self.age != 0 and self.age%10 == 0:
    #             self.energy -= parameters.getAging()
    #     if self.energy <= 0 or self.age == self.lifetime:
    #         isAlive = False 
    #     return isAlive, self.energy
    
    def grazes(self):
        if not self.moved:
            if self.energy < parameters.getMaxEnergy():
                self.energy += 1
        else:
            self.moved = False   

    # def moves(self):
    #     self.energy -= 1
    #     self.moved = True

    # def willMove(self):
    #     moves = False
    #     isStill = True
    #     if self.moved:
    #         return moves, isStill
    #     if self.socialAttitude > parameters.getMinSocAtt() and self.getEnergy() > parameters.getMaxEnergy()//3:
    #         moves = True
    #     if self.socialAttitude <= parameters.getMinSocAtt() and self.getEnergy() > parameters.getMaxEnergy()//3:
    #         isStill = False   
    #     return moves, isStill