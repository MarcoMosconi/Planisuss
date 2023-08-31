import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from keygenerator import generateKey
import random
from constants import MOVE_PROBABILITY, MAX_HERD

class Herd:
    def __init__(self, cell):
        self.cell = cell
        self.erbasts = {}

    def getErbasts(self):
        return self.erbasts
    
    def getNumErbast(self):
        # print(self.cell, len(self.erbasts))
        return len(self.erbasts)

    def addErbast(self, key, erbast):
        self.erbasts[key] = erbast
        # print('added with key', key, 'and lifetime', erbast.lifetime, 'and energy',erbast.getEnergy(), 'and cell', erbast.cell)
    
    def removeErbast(self, key):
        # print('dead with key', key, 'and lifetime', self.erbasts[key].lifetime, 'and energy', self.erbasts[key].getEnergy(), 'and cell', self.erbasts[key].cell)
        self.erbasts.pop(key)
    
    def kill(self):
        self.erbasts = {}

    def sortErbasts(self):
        return sorted(self.erbasts, key = lambda item: self.erbasts[item].getEnergy())

    def spawns(self):
        if self.getNumErbast() == 0:
            return 0
        born = []
        dead = []
        
        for key, erbast in self.erbasts.items():
            isAlive, energy = erbast.grows()
            if not isAlive:
                dead.append(key)
                if energy > 0:
                    energy1 = energy//2
                    energy2 = energy - energy1
                    key1 = generateKey()
                    key2 = generateKey()
                    born.append({'key': key1, 'energy': energy1})
                    born.append({'key': key2, 'energy': energy2})
        for key in dead:
            # print('dead with', key, 'key in the right way')
            self.removeErbast(key)
        for elm in born:
            erbast = Erbast(self.cell, elm['energy'])
            self.addErbast(elm['key'], erbast)
        return self.getNumErbast()
    
    def graze(self, availableEnergy):
        keys = self.sortErbasts()
        for key in keys:
            self.erbasts[key].grazes()
            availableEnergy -= 1
            if availableEnergy <= 0:
                break
        return 
    
    def move(self, targetHerd):
        movingErbasts = []
        herdMoves = random.random() > MOVE_PROBABILITY
        for key, erbast in self.erbasts.items():
            erbastMoves, erbastIsStill = erbast.willMove()
            if (herdMoves and erbastMoves) or (not herdMoves and not erbastIsStill) and len(targetHerd.erbasts) < MAX_HERD:
                movingErbasts.append(key)
                # print('erbast is in cell', erbast.cell, 'with energy', erbast.getEnergy())
                erbast.moves()
                erbast.cell = targetHerd.cell
                targetHerd.addErbast(key, erbast)
                # print('in herd cell', targetHerd.cell)
        for key in movingErbasts:
            self.removeErbast(key)
        return 
