import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as pat
import numpy as np
from cells.setup import cells
from constants import NUMCELLS, MAX_ENERGY, MAX_DENSITY
from vegetobs.setup import vegetobs
from erbasts.setup import herds
import random

def setColor(r,g,b):
    return [r,g,b]

def setErbastColor(c):
    return setColor(0,0,c)

def setCarvizColor(c):
    return setColor(c,0,0)

def setupMap(ax):
    cellList = []
    for cellname in cells:
        cellList.append(cells[cellname])
        
    mapLists = []
    densityLists = []
    herdLists = []
    for i in range(0, NUMCELLS):
        columnMapList = []
        columnDensityList = []
        columnHerdList = []
        for j in range(i, len(cellList), NUMCELLS):
            cell = cellList[j]
            if cell.isGround():
                columnMapList.append(1)
                for cellname in vegetobs:
                    if cells[cellname] == cell:
                        columnDensityList.append(vegetobs[cellname].getDensity()/MAX_DENSITY)
                for key in herds:
                    if cells[herds[key].cell] == cell:
                        columnHerdList.append(herds[key])
                        break
            else:
                columnMapList.append(0)
                columnDensityList.append(0.0)
                columnHerdList.append(0)
        mapLists.append(columnMapList)
        densityLists.append(columnDensityList)
        herdLists.append(columnHerdList)
    
    # A = np.asarray(mapLists)
    B = np.asarray(densityLists)
    # C = np.asarray(herdLists)
    # print(herdLists)

    # print(A)
    # print('--------------------------------')
    # print(B)
    # print('--------------------------------')
    # print(C)

    fig, ax = plt.subplots()
    colors = ['lightcyan', 'saddlebrown']
    cmap = ListedColormap(colors)
    mapCells = ax.imshow(mapLists, cmap=cmap, extent=[0,NUMCELLS,0,NUMCELLS])
    # densityCells = ax.imshow(densityLists, extent=[0,NUMCELLS,0,NUMCELLS])

    numCell = len(mapLists)
    # cellSize = int(NUMCELLS/numCell)

    for y in range(numCell):
        plt.axhline(y * 1, color='black', linewidth=0.2)
    for x in range(numCell):
        plt.axvline(x * 1, color='black', linewidth=0.2)
    
    # densityLista = [[0.7, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.0, 0.9, 0.0], [0.0, 0.2, 0.4, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.8]]

    for row, rowList in enumerate(mapLists):
        for col, _ in enumerate(rowList):
            densityValue = densityLists[row][col]
            # print('map value', mapLists[row][col], 'and density value', densityValue)
            if densityValue > 0:
                square = pat.Rectangle((col, NUMCELLS-1-row), densityValue, densityValue, color = 'green')
                ax.add_patch(square)
            herd = herdLists[row][col]
            if herd != 0:
                for key in herd.animals:
                    # print((herd.animals[key].getEnergy()/MAX_ENERGY))
                    circle = pat.Circle((col+random.uniform(0.15,0.85), NUMCELLS-random.uniform(0.15,0.85)-row), 0.15, color = setErbastColor(herd.animals[key].getEnergy()/MAX_ENERGY))
                    ax.add_patch(circle)
        # print('------------------------')
    
    ax.set_aspect('equal')

    return 
    


