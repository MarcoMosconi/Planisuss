#function grow for which all densities continously grow 

from setup import vegetobs

def grow():

    totalDensity = 0
    
    for cellname in vegetobs:
        vegetobs[cellname].grows()
        totalDensity += vegetobs[cellname].getDensity()

    return totalDensity

