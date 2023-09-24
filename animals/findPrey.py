import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.setup import cells, setCellname
from vegetobs.setup import vegetobs
from erbasts.setup import herds
from parameters import parameters

def findPrey(cellname, prevCells):  #it finds the target cell for the Erbast based on Vegetob density, the one for the Carviz based on Erbast energy,
    density = 0                     #and returns killGroup = True is the social group is overwhelmed by the Vegetob
    neighbors = {}
    x0,y0 = cells[cellname].getCoordinates()
    targetCell_E, targetCell_C, maxDensity, maxErbast, killGroup = cellname, cellname, 0, 0, False
    for x in range(x0-parameters.getNeighborhood(), x0+parameters.getNeighborhood()+1):
        if x < 0 or x >= parameters.getNumcells():  #ignores the cells out of the grid
            continue
        for y in range(y0-parameters.getNeighborhood(), y0+parameters.getNeighborhood()+1):
            if y < 0 or y >= parameters.getNumcells(): #ignores the cells out of the grid
                continue
            if x == x0 and y == y0: #ignores the cell corresponding to the current one
                continue
            currCell = setCellname(x,y)
            if cells[currCell].getType() == "Water": #ignores the water cells 
                continue
            currDensity = vegetobs[currCell].getDensity()
            density += currDensity                          #adds the density to "density"
            neighbors[currCell] = vegetobs[currCell]        #and the vegetob to the dictionary "neighbors" to later check if the Vegetob overwhelm the group
            if currCell in prevCells:         #ignores the cells where the animals of the current social group have been the previous day
                continue
            for key in herds:
                if herds[key].cell == currCell:
                    currErbast = herds[key].getNumAnimal()
                    break
            if currDensity > maxDensity:    #eventually sets the new target cell for the Erbast
                targetCell_E, maxDensity = currCell, currDensity
            if currErbast > maxErbast:      #eventually sets the new target cell for the Carviz
                targetCell_C, maxErbast = currCell, currErbast
    if len(neighbors) != 0 and density == len(neighbors)*parameters.getMaxDensity():    #checks if the group is overwhelmed by the Vegetob
        killGroup = True
    return targetCell_E, targetCell_C, killGroup
                
