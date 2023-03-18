from cells.setup import cells
from vegetobs.vegetob import Vegetob

vegetobs = {}

def setupVegetobs():
    totalDensity = 0
    for key in cells:
        if cells[key].isGround():
            v = Vegetob(key)
            vegetobs[key] = v
            totalDensity += v.getDensity()
    return totalDensity



