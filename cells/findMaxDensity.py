import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.setup import cells, setCellname
from vegetobs.setup import vegetobs
from constants import NEIGHBORHOOD, NUMCELLS

def findMaxDensity(cellname):
    x0,y0 = cells[cellname].getCoordinates()
    targetCell, maxDensity = cellname, 0
    for x in range(x0-NEIGHBORHOOD, x0+NEIGHBORHOOD+1):
        if x < 0 or x >= NUMCELLS:
            continue
        for y in range(y0-NEIGHBORHOOD, y0+NEIGHBORHOOD+1):
            if y < 0 or y >= NUMCELLS:
                continue
            if x == x0 and y == y0:
                continue
            currCell = setCellname(x,y)
            if cells[currCell].getType() == "Water":
                continue
            currDensity = vegetobs[currCell].getDensity()
            if currDensity > maxDensity:
                targetCell, maxDensity = currCell, currDensity
    return targetCell
                
