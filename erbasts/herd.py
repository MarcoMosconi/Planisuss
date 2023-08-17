import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from keygenerator import generateKey

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
    
    def spawns(self):
        if self.getNumErbast() == 0:
            return 0
        born = []
        dead = []
        
        for key, erbast in self.erbasts.items():
            isDead = erbast.grows()
            if isDead:
                energy = erbast.getEnergy()
                energy1 = energy//2
                energy2 = energy - energy1
                key1 = generateKey()
                key2 = generateKey()
                born.append({'key': key1, 'energy': energy1})
                born.append({'key': key2, 'energy': energy2})
                dead.append(key)
                
        for key in dead:
            self.removeErbast(key)
        for elm in born:
            erbast = Erbast(self.cell, elm['key'], elm['energy'])
            self.addErbast(elm['key'], erbast)
        return self.getNumErbast()

