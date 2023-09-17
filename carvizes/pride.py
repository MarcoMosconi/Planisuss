import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from keygenerator import generateKey
import random
from parameters import parameters
from animals.groups import Group

class Pride(Group):
    def __init__(self, cell):
        super().__init__(cell)

    def eat(self, availableEnergy):
        keys = self.sortAnimals()
        indEnergy = availableEnergy//self.getNumAnimal()
        remainingEnergy = availableEnergy - indEnergy*self.getNumAnimal()
        if indEnergy < 1:
            for key in keys:
                self.animals[key].eats(1)
                availableEnergy -= 1
                if availableEnergy <= 0:
                    break
        else:
            for key in keys:
                self.animals[key].eats(indEnergy)
            if remainingEnergy > 0:
                for key in keys:
                    self.animals[key].eats(1)
                    remainingEnergy -= 1
                    if remainingEnergy <= 0:
                        break
        return
    
    def join(self, targetPride):
        for key in self.animals:
            self.animals[key].cell = targetPride.cell
            targetPride.addAnimal(key, self.animals[key])
    
    def winFight(self):
        for key in self.animals:
            if self.animals[key].socialAttitude < 1:
                self.animals[key].socialAttitude += 0.1
    
    def failHunt(self):
        deadCarviz = []
        for key in self.animals:
            self.animals[key].socialAttitude -= 0.1
            if self.animals[key].socialAttitude < 0:
                self.animals[key].socialAttitude == 0
            self.animals[key].energy -= 2
            if self.animals[key].energy <= 0:
                deadCarviz.append(key)
        for key in deadCarviz:
            self.removeAnimal(key)