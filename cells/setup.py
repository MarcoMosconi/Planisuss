#setup (coordinates and grid) for the cells

import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

import constants
from cells.cell import Cell

cells = {}

def setupCells():           

    for i in range(0, constants.NUMCELLS):      #coordinate x for every cell
        for j in range(0, constants.NUMCELLS):  #coordinate y for every cell
            cellname = ("c_" + str(i) + "_" + str(j))   
            c = Cell(i, j)                      #the coordinates are attributed to member of the class Cell
            cells[cellname] = c                 #cellname is the key given to the dictionary cells and the value is the corresponding cell

    # cells["c_3_7"].getCoordinates()

    for i in range(0, constants.NUMCELLS):      #this is the grid with water/ground cells
        ln = ''
        for j in range(0, constants.NUMCELLS):
            cellname = ("c_" + str(i) + "_" + str(j)) 
            x = 'G' if cells[cellname].isGround() else '.'
            ln = ln + x + ' '
        print(ln)
