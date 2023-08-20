import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from keygenerator import generateKey
from constants import NEIGHBORHOOD
from vegetobs.setup import vegetobs

class Herd:
    def __init__(self, cell):
        self.cell = cell
        self.erbasts = {}

    def getErbasts(self):
        return self.erbasts
    
    def getNumErbast(self):
        return len(self.erbasts)

    def addErbast(self, key, erbast):
        self.erbasts[key] = erbast
    
    def removeErbast(self, key):
        self.erbasts.pop(key)

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
            self.removeErbast(key)
        for elm in born:
            erbast = Erbast(self.cell, elm['key'], elm['energy'])
            self.addErbast(elm['key'], erbast)
        return self.getNumErbast()
    
    def graze(self, availableEnergy):
        keys = self.sortErbasts()
        for key in keys:
            self.erbasts[key].grazes()
            availableEnergy -= 1
            if availableEnergy == 0:
                break
        return 