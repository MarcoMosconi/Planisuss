import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.setup import herds
from carvizes.setup import prides
from animals.findPrey import findPrey

def movement():
    for key in herds:
        herd = herds[key]
        cellname = herd.cell
        num = herd.getNumAnimal()
        if num > 0:
            targetCellname = findPrey(cellname)
            if targetCellname != cellname:
                for key in herds:
                    if targetCellname == herds[key].cell:
                        herd.move(herds[key])
                        break
    
    for key in prides:
        pride = prides[key]
        cellname = pride.cell
        num = pride.getNumAnimal()
        if num > 0:
            _, targetCellname, _ = findPrey(cellname)
            if targetCellname != cellname:
                for key in prides:
                    if targetCellname == prides[key].cell:
                        pride.move(prides[key])
                        break
    return 