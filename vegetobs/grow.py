#function grow for which all densities continously grow 

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from vegetobs.setup import vegetobs

def grow():

    totalDensity = 0
    
    for cellname in vegetobs:
        vegetobs[cellname].grows()
        totalDensity += vegetobs[cellname].getDensity()

    return totalDensity

