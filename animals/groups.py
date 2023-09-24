import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from carvizes.carviz import Carviz
from keygenerator import generateKey
import random
from parameters import parameters

class Group:
    def __init__(self, cell):
        self.cell = cell
        self.animals = {}
        self.prevCells = []
        self.currInCells = []

    def getAnimals(self):
        return self.animals
    
    def getNumAnimal(self):
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
    
    def removeAnimal(self, key):
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
            isAlive, energy, lifetime = animal.grows()
            if not isAlive: #is the animal is dead it is put in the list to be later removed from the dictionary "animals"
                dead.append(key)
                max = parameters.getMaxHerd()-1 if isinstance(animal, Erbast) else parameters.getMaxPride()-1
                if self.getNumAnimal() < max and energy > 0:    #if it is dead because its age reached its lifetime the offspring is generated
                    energy1 = random.randint(0,energy)
                    energy2 = energy - energy1
                    lifetime1 = random.randint(0, min(parameters.getMaxLife(), 2*lifetime))
                    lifetime2 = 2*lifetime-lifetime1
                    socialAtt1 = random.uniform(0, min(1, 2*animal.getSocialAttitude()))
                    socialAtt2 = 2*animal.getSocialAttitude()-socialAtt1
                    key1 = generateKey()
                    key2 = generateKey()
                    born.append({'key': key1, 'energy': energy1, 'lifetime': lifetime1, 'socialAttitude': socialAtt1})
                    born.append({'key': key2, 'energy': energy2, 'lifetime': lifetime2, 'socialAttitude': socialAtt2})
        for key in dead:
            self.removeAnimal(key)
        for elm in born:
            if isinstance(animal, Erbast):
                bornAnimal = Erbast(self.cell, elm['energy'], elm['lifetime'], elm['socialAttitude'])
            if isinstance(animal, Carviz):
                bornAnimal = Carviz(self.cell, elm['energy'], elm['lifetime'], elm['socialAttitude'])
            self.addAnimal(elm['key'], bornAnimal)
        return self.getNumAnimal()
    
    def move(self, targetGroup):
        movingAnimal = []
        groupMoves = random.random() > parameters.getMoveProb()
        if groupMoves:  #it the group moves its cell is added to the target group list of the cells which are currently in 
            targetGroup.currInCells.append(self.cell)
        for key, animal in self.animals.items():
            animalMoves, animalIsStill = animal.willMove()
            max = parameters.getMaxHerd() if isinstance(animal, Erbast) else parameters.getMaxPride()
            if ((groupMoves and animalMoves) or (not groupMoves and not animalIsStill)) and targetGroup.getNumAnimal() < max: #either the group moves and the animal moves
                movingAnimal.append(key)                                                                                      #or the group is still and the animal moves
                animal.moves()
                animal.cell = targetGroup.cell
                targetGroup.addAnimal(key, animal)      #the animal moves, its energy is decreased and it is added to the dictionary "animals" of the target group
        for key in movingAnimal:                        #the animal is removed from the current dictionary
            self.removeAnimal(key)
        return 