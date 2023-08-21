import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.setup import herds
from vegetobs.setup import vegetobs

def grazing():
    for key in herds:
        herd = herds[key]
        cellname = herd.cell
        num = herd.getNumErbast()
        if num > 0:
            availableEnergy = vegetobs[cellname].graze(num)
            herd.graze(availableEnergy)
    return 