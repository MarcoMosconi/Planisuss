import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.herd import Herd
from erbasts.setup import herds
from cells.findMaxDensity import findMaxDensity

def movement():
    for key in herds:
        herd = herds[key]
        cellname = herd.cell
        num = herd.getNumErbast()
        if num > 0:
            targetCellname = findMaxDensity(cellname)
            if targetCellname != cellname:
                for key in herds:
                    if targetCellname == herds[key].cell:
                        herd.move(herds[key])
                        break
    return 