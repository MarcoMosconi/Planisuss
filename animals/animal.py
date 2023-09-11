import random
from constants import MAX_ENERGY, MAX_LIFE, AGING, MIN_SOCIAL_ATTITUDE

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
            return random.randint(0, MAX_LIFE)
        return lifetime
    
    def setSocialAttitude(self, socialAttitude):
        if socialAttitude == None:
            return random.random()
        return socialAttitude
    
    def setInitialEnergy(self, energy):
        if energy == None:
            return random.randint(0, MAX_ENERGY)
        return energy

    def getEnergy(self):
        return self.energy
    
    def getSocialAttitude(self):
        return self.socialAttitude
    
    def grows(self):
        isAlive = True
        self.age += 1
        if self.age != 0 and self.age%10 == 0:
                self.energy -= AGING
        if self.energy <= 0 or self.age == self.lifetime:
            isAlive = False 
        return isAlive, self.energy, self.lifetime
    
    def moves(self):
        self.energy -= 1
        self.moved = True

    def willMove(self):
        moves = False
        isStill = True
        if self.moved:
            return moves, isStill
        if self.getSocialAttitude() > MIN_SOCIAL_ATTITUDE and self.getEnergy() > MAX_ENERGY//3:
            moves = True
        if self.getSocialAttitude() <= MIN_SOCIAL_ATTITUDE and self.getEnergy() > MAX_ENERGY//3:
            isStill = False   
        return moves, isStill