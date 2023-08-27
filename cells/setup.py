#setup (coordinates and grid) for the cells

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from constants import NUMCELLS
from cells.cell import Cell

cells = {}

def setCellname(x,y):
    return "c_" + str(x) + "_" + str(y)

def setupCells():           

    for i in range(0, NUMCELLS):      #coordinate x for every cell
        for j in range(0, NUMCELLS):  #coordinate y for every cell
            cellname = setCellname(i,j)   
            c = Cell(i, j)                      #the coordinates are attributed to member of the class Cell
            cells[cellname] = c                 #cellname is the key given to the dictionary cells and the value is the corresponding cell

    # cells["c_3_7"].getCoordinates()

    for i in range(0, NUMCELLS):      #this is the grid with water/ground cells
        ln = ''
        for j in range(0, NUMCELLS):
            cellname = setCellname(i,j) 
            x = 'G' if cells[cellname].isGround() else '.'
            ln = ln + x + ' '
        print(ln)
