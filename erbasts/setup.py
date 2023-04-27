import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

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






