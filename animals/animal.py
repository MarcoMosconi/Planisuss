import random
from parameters import parameters

class Animal:
    def __init__(self, cell, energy = None, lifetime = None, socialAttitude = None):
        self.cell = cell
        self.lifetime = self.setLifetime(lifetime)
        self.socialAttitude = self.setSocialAttitude(socialAttitude)
        self.energy = self.setInitialEnergy(energy)
        self.age = 0
        self.moved = False

    def setLifetime(self, lifetime):
        if lifetime == None:
            return random.randint(0, parameters.getMaxLife())
        return lifetime
    
    def setSocialAttitude(self, socialAttitude):
        if socialAttitude == None:
            return random.random()
        return socialAttitude
    
    def setInitialEnergy(self, energy):
        if energy == None:
            return random.randint(0, parameters.getMaxEnergy())
        return energy

    def getEnergy(self):
        return self.energy
    
    def getSocialAttitude(self):
        return self.socialAttitude
    
    def grows(self):    #increases the age and enentually decreases the energy and returns isAlive = False if the animal dies
        isAlive = True
        self.age += 1
        if self.age != 0 and self.age%10 == 0:
                self.energy -= parameters.getAging()
        if self.energy <= 0 or self.age == self.lifetime:
            isAlive = False 
        return isAlive, self.energy, self.lifetime
    
    def moves(self):
        self.energy -= 1
        self.moved = True

    def willMove(self):
        moves = False
        isStill = True
        if self.moved:      #in case the animal moved it cannot move again, so moves is False and isStill is True
            return moves, isStill
        if self.getSocialAttitude() > parameters.getMinSocAtt() and random.randint(0,parameters.getMaxEnergy()) <= self.getEnergy(): #case in which the animal follows the moving social group
            moves = True
        if self.getSocialAttitude() <= parameters.getMinSocAtt() and random.randint(0,parameters.getMaxEnergy()) <= self.getEnergy(): #case in which the animal moves leaving the still social group
            isStill = False   
        return moves, isStill