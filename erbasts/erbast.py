#Erbast Class

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from constants import MAX_ENERGY, MAX_LIFE, AGING, MIN_SOCIAL_ATTITUDE
from animals.animal import Animal

class Erbast(Animal):
    def __init__(self, cell, energy = None):
        super().__init__(cell, energy)
    #     self.cell = cell
    #     self.lifetime = self.setLifetime()
    #     self.socialAttitude = self.setSocialAttitude()
    #     self.energy = self.setInitialEnergy(energy)
    #     self.age = 0
    #     self.moved = False

    # def setLifetime(self):
    #     return random.randint(0, MAX_LIFE)
    
    # def setSocialAttitude(self):
    #     return random.random()
    
    # def setInitialEnergy(self, energy):
    #     if energy == None:
    #         return random.randint(0, MAX_ENERGY)
    #     return energy

    # def getEnergy(self):
    #     return self.energy
    
    # def grows(self):
    #     isAlive = True
    #     self.age += 1
    #     if self.age != 0 and self.age%10 == 0:
    #             self.energy -= AGING
    #     if self.energy <= 0 or self.age == self.lifetime:
    #         isAlive = False 
    #     return isAlive, self.energy
    
    def grazes(self):
        if not self.moved:
            if self.energy < MAX_ENERGY:
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
    #     if self.socialAttitude > MIN_SOCIAL_ATTITUDE and self.getEnergy() > MAX_ENERGY//3:
    #         moves = True
    #     if self.socialAttitude <= MIN_SOCIAL_ATTITUDE and self.getEnergy() > MAX_ENERGY//3:
    #         isStill = False   
    #     return moves, isStill