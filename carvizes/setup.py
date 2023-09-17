import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from cells.setup import cells
from carvizes.pride import Pride
from carvizes.carviz import Carviz
from parameters import parameters
from keygenerator import generateKey

prides = {}

def setupPrides():
    totalNumberCarvizes = 0
    for cellname in cells:
        if cells[cellname].isGround():
            key = generateKey()
            p = Pride(cellname)
            prides[key] = p           
            if random.random() > parameters.getCarvizProb():
                carkey = generateKey()
                e = Carviz(cellname)
                p.addAnimal(carkey, e)
                totalNumberCarvizes += 1
    return totalNumberCarvizes
