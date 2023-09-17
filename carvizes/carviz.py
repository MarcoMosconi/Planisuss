import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from animals.animal import Animal
from parameters import parameters

class Carviz(Animal):
   def __init__(self, cell, energy = None, lifetime = None, socialAttitude = None):
      super().__init__(cell, energy, lifetime, socialAttitude)
   
   def eats(self, indEnergy):
         if self.energy + indEnergy < parameters.getMaxEnergy():
             self.energy += indEnergy
         else:
             self.energy == parameters.getMaxEnergy()
            
           
      