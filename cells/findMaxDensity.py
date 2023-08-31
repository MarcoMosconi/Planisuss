import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.setup import cells, setCellname
from vegetobs.setup import vegetobs
from constants import NEIGHBORHOOD, NUMCELLS, MAX_DENSITY

def findMaxDensity(cellname):
    density = 0
    neighbors = {}
    x0,y0 = cells[cellname].getCoordinates()
    targetCell, maxDensity, killHerd = cellname, 0, False
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
            neighbors[currCell] = vegetobs[currCell]
            currDensity = vegetobs[currCell].getDensity()
            density += currDensity
            if currDensity > maxDensity:
                targetCell, maxDensity = currCell, currDensity
    if len(neighbors) != 0 and density == len(neighbors)*MAX_DENSITY:
        killHerd = True
    return targetCell, killHerd
                
