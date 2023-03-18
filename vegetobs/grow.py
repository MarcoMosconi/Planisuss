from vegetobs.setup import vegetobs

def grow():

    totalDensity = 0
    
    for key in vegetobs:
        vegetobs[key].grow()
        totalDensity += vegetobs[key].getDensity()
    return totalDensity

