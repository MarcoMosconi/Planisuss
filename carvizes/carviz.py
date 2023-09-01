import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from animals.animal import Animal

class Carviz(Animal):
     def __init__(self, cell, energy = None):
        super().__init__(cell, energy)