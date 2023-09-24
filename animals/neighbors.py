import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from animals.findPrey import findPrey
from erbasts.setup import herds
from carvizes.setup import prides

#iterates through herds and prides and if killHerd is True, hence
#all the ground cells they have next to them are full of vegetobs, 
#the animals inside the group die

def neighbors():
    for key in herds:
        cellname = herds[key].cell
        prevCells = herds[key].prevCells
        _, _, killHerd = findPrey(cellname,prevCells)
        if killHerd:
            herds[key].kill()

    for key in prides:
        cellname = prides[key].cell
        prevCells = prides[key].prevCells
        _, _, killHerd = findPrey(cellname,prevCells)
        if killHerd:
            prides[key].kill()
    
    
        
    
    
         