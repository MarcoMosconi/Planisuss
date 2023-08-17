import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from cells.setup import cells
from erbasts.herd import Herd
from erbasts.erbast import Erbast
from constants import ERBAST_PROBABILITY
from keygenerator import generateKey

herds = {}

def setupHerds():
    totalNumberErbast = 0
    for cellname in cells:
        if cells[cellname].isGround():
            key = generateKey()
            h = Herd(cellname)
            herds[key] = h           
            if random.random() > ERBAST_PROBABILITY:
                erbkey = generateKey()
                e = Erbast(cellname, key)
                h.addErbast(erbkey, e)
                totalNumberErbast += 1
    return totalNumberErbast






