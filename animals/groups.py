import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from carvizes.carviz import Carviz
from keygenerator import generateKey
import random
from constants import MOVE_PROBABILITY, MAX_HERD

class Group:
    def __init__(self, cell):
        self.cell = cell
        self.animals = {}

    def getAnimals(self):
        return self.animals
    
    def getNumAnimal(self):
        # print(self.cell, len(self.animals))
        return len(self.animals)
    
    def getAvSocialAttitude(self):
        socialAtt = 0
        for key in self.animals:
                socialAtt += self.animals[key].getSocialAttitude()
        avSocialAtt = socialAtt/self.getNumAnimal()
        return avSocialAtt
    
    def getTotalEnergy(self):
        totEnergy = 0
        for key in self.animals:
            totEnergy += self.animals[key].getEnergy()
        return totEnergy

    def addAnimal(self, key, animal):
        self.animals[key] = animal
        # print('added with key', key, 'and lifetime', animal.lifetime, 'and energy',animal.getEnergy(), 'and cell', animal.cell)
    
    def removeAnimal(self, key):
        # print('dead with key', key, 'and lifetime', self.animals[key].lifetime, 'and energy', self.animals[key].getEnergy(), 'and cell', self.animals[key].cell)
        self.animals.pop(key)
    
    def kill(self):
        self.animals = {}

    def sortAnimals(self):
        return sorted(self.animals, key = lambda item: self.animals[item].getEnergy())

    def spawns(self):
        if self.getNumAnimal() == 0:
            return 0
        born = []
        dead = []
        
        for key, animal in self.animals.items():
            isAlive, energy = animal.grows()
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
            self.removeAnimal(key)
        for elm in born:
            if isinstance(animal, Erbast):
                bornAnimal = Erbast(self.cell, elm['energy'])
            if isinstance(animal, Carviz):
                bornAnimal = Carviz(self.cell, elm['energy'])
            self.addAnimal(elm['key'], bornAnimal)
        return self.getNumAnimal()
    
    def move(self, targetGroup):
        movingAnimal = []
        groupMoves = random.random() > MOVE_PROBABILITY
        for key, animal in self.animals.items():
            animalMoves, animalIsStill = animal.willMove()
            if (groupMoves and animalMoves) or (not groupMoves and not animalIsStill) and targetGroup.getNumAnimal() < MAX_HERD:
                movingAnimal.append(key)
                # print('animal is in cell', animal.cell, 'with energy', animal.getEnergy())
                animal.moves()
                animal.cell = targetGroup.cell
                targetGroup.addAnimal(key, animal)
                # print('in herd cell', targetHerd.cell)
        for key in movingAnimal:
            self.removeAnimal(key)
        return 