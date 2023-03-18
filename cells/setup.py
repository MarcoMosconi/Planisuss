import constants
from cells.cell import Cell

cells = {}

def setupCells():

    for i in range(0, constants.NUMCELLS):
        for j in range(0, constants.NUMCELLS):
            cellname = ("c_" + str(i) + "_" + str(j)) 
            c = Cell(i, j)
            cells[cellname] = c 

    # cells["c_3_7"].getCoordinates()

    for i in range(0, constants.NUMCELLS):
        ln = ''
        for j in range(0, constants.NUMCELLS):
            cellname = ("c_" + str(i) + "_" + str(j)) 
            x = 'G' if cells[cellname].isGround() else '.'
            ln = ln + x + ' '
        print(ln)