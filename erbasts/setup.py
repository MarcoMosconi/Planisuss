import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from cells.setup import cells
from erbasts.herd import Herd
from erbasts.erbast import Erbast
from parameters import parameters
from keygenerator import generateKey

herds = {}

def setupHerds():
    totalNumberErbast = 0
    for cellname in cells:
        if cells[cellname].isGround():
            key = generateKey()
            h = Herd(cellname)
            herds[key] = h           #random string as key and herd as value
            if random.random() > parameters.getErbastProb():
                erbkey = generateKey()
                e = Erbast(cellname)
                h.addAnimal(erbkey, e)  #the erbast is added inside the dictionary "animals" of the herd
                totalNumberErbast += 1
    return totalNumberErbast






