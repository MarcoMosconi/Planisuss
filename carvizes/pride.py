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
    
    def graze(self, availableEnergy):
        keys = self.sortAnimals()
        for key in keys:
            self.animals[key].grazes()
            availableEnergy -= 1
            if availableEnergy <= 0:
                break
        return 
    
    def move(self, targetHerd):
        movingErbasts = []
        herdMoves = random.random() > MOVE_PROBABILITY
        for key, erbast in self.animals.items():
            erbastMoves, erbastIsStill = erbast.willMove()
            if (herdMoves and erbastMoves) or (not herdMoves and not erbastIsStill) and len(targetHerd.erbasts) < MAX_HERD:
                movingErbasts.append(key)
                # print('erbast is in cell', erbast.cell, 'with energy', erbast.getEnergy())
                erbast.moves()
                erbast.cell = targetHerd.cell
                targetHerd.addAnimal(key, erbast)
                # print('in herd cell', targetHerd.cell)
        for key in movingErbasts:
            self.removeAnimal(key)
        return 