#setup for Vegetobs

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.setup import cells
from vegetobs.vegetob import Vegetob

vegetobs = {}

def setupVegetobs():
    totalDensity = 0
    for cellname in cells:
        if cells[cellname].isGround():  #if a cell is ground
            v = Vegetob(cellname)       #this cell is attributed to a member of the class Vegetob
            vegetobs[cellname] = v      #the dictionary vegetobs has as key the cell and as value the corresponding vegetob
            totalDensity += v.getDensity()
    return totalDensity



