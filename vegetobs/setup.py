from cells.setup import cells
from vegetobs.vegetob import Vegetob

vegetobs = {}

def setupVegetobs():

    for key in cells:
        if cells[key].isGround():
            v = Vegetob(key)
            vegetobs[key] = v
#            print(key, v.getDensity())



