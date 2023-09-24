import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from animals.groups import Group

class Herd(Group):
    def __init__(self, cell):
        super().__init__(cell)
    
    def graze(self, availableEnergy):
        keys = self.sortAnimals()
        for key in keys:
            if availableEnergy <= 0:
                self.animals[key].socialAttitude -= 1   #if there's not enough energy for all the Erbast the social attitude of the ones not eating is decreased
            else:
                self.animals[key].grazes()
                availableEnergy -= 1
        return 
    
