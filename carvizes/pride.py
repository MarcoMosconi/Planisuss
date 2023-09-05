import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from keygenerator import generateKey
import random
from constants import MOVE_PROBABILITY, MAX_HERD
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
    