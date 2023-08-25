import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.setup import cells
from constants import NUMCELLS

def map():
    cellList = []
    for cellname in cells:
        cellList.append(cells[cellname])
        
    mapLists = []
    for i in range(0, NUMCELLS):
        columnList = []
        for j in range(i, len(cellList), NUMCELLS):
            cell = cellList[j]
            if cell.isGround():
                columnList.append(1)
            else:
                columnList.append(0)
        mapLists.append(columnList)

    return mapLists

