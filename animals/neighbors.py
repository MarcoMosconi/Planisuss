import sys
import os


current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from animals.findPrey import findPrey
from erbasts.setup import herds
from carvizes.setup import prides

def neighbors():
    for key in herds:
        cellname = herds[key].cell
        prevCells = herds[key].prevCells
        _, _, killHerd = findPrey(cellname,prevCells)
        if killHerd:
            # print('kill', cellname)
            herds[key].kill()

    for key in prides:
        cellname = prides[key].cell
        prevCells = prides[key].prevCells
        _, _, killHerd = findPrey(cellname,prevCells)
        if killHerd:
            # print('kill', cellname)
            prides[key].kill()
    
    
        
    
    
         