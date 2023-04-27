#function grow for which all densities continously grow 

import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

from vegetobs.setup import vegetobs

def grow():

    totalDensity = 0
    
    for cellname in vegetobs:
        vegetobs[cellname].grows()
        totalDensity += vegetobs[cellname].getDensity()

    return totalDensity

