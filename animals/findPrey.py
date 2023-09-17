import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.setup import cells, setCellname
from vegetobs.setup import vegetobs
from erbasts.setup import herds
from parameters import parameters

def findPrey(cellname, prevCells):
    density = 0
    neighbors = {}
    x0,y0 = cells[cellname].getCoordinates()
    targetCell_E, targetCell_C, maxDensity, maxErbast, killGroup = cellname, cellname, 0, 0, False
    for x in range(x0-parameters.getNeighborhood(), x0+parameters.getNeighborhood()+1):
        if x < 0 or x >= parameters.getNumcells():
            continue
        for y in range(y0-parameters.getNeighborhood(), y0+parameters.getNeighborhood()+1):
            if y < 0 or y >= parameters.getNumcells():
                continue
            if x == x0 and y == y0:
                continue
            currCell = setCellname(x,y)
            if cells[currCell].getType() == "Water":
                continue
            if currCell in prevCells:
                continue
            neighbors[currCell] = vegetobs[currCell]
            currDensity = vegetobs[currCell].getDensity()
            for key in herds:
                # print(herds[key].cell)
                if herds[key].cell == currCell:
                    currErbast = herds[key].getNumAnimal()
                    break
            density += currDensity
            if currDensity > maxDensity:
                targetCell_E, maxDensity = currCell, currDensity
            if currErbast > maxErbast:
                targetCell_C, maxErbast = currCell, currErbast
    if len(neighbors) != 0 and density == len(neighbors)*parameters.getMaxDensity():
        killGroup = True
    return targetCell_E, targetCell_C, killGroup
                
