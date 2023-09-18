import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as pat
from cells.setup import cells
from parameters import parameters
from vegetobs.setup import vegetobs
from erbasts.setup import herds
from carvizes.setup import prides
import random

#map where the daily status of the three species is represented

def setColor(r,g,b):
    return [r,g,b]

def setErbastColor(c):
    return setColor(0,0,c)

def setCarvizColor(c):
    return setColor(c,0,0)

def setupMap(ax,day):
    plt.cla()
    ax.set_title(f'Day {day}')

    #create one matrix with the Ground/Water cells, one with the density of the vegetobs, one with the energy of the erbasts 
    # and one with the energy of the carvizes
    cellList = []
    for cellname in cells:
        cellList.append(cells[cellname])

    mapLists = []
    densityLists = []
    herdLists = []
    prideLists = []
    for i in range(0, parameters.getNumcells()):
        columnMapList = []
        columnDensityList = []
        columnHerdList = []
        columnPrideList = []
        for j in range(i, len(cellList), parameters.getNumcells()):
            cell = cellList[j]
            if cell.isGround():
                columnMapList.append(1)
                for cellname in vegetobs:
                    if cells[cellname] == cell:
                        columnDensityList.append(vegetobs[cellname].getDensity()/parameters.getMaxDensity())
                for key in herds:
                    if cells[herds[key].cell] == cell:
                        columnHerdList.append(herds[key])
                        break
                for key in prides:
                    if cells[prides[key].cell] == cell:
                        columnPrideList.append(prides[key])
                        break
            else:
                columnMapList.append(0)
                columnDensityList.append(0.0)
                columnHerdList.append(0)
                columnPrideList.append(0)
        mapLists.append(columnMapList)
        densityLists.append(columnDensityList)
        herdLists.append(columnHerdList)
        prideLists.append(columnPrideList)
    
    #background map with Ground/Water cells
    colors = ['lightcyan', 'saddlebrown']
    cmap = ListedColormap(colors)
    mapCells = ax.imshow(mapLists, cmap=cmap, extent=[0,parameters.getNumcells(),0,parameters.getNumcells()])

    numCell = len(mapLists)
    #add the axis
    for y in range(numCell):
        plt.axhline(y * 1, color='black', linewidth=0.2)
    for x in range(numCell):
        plt.axvline(x * 1, color='black', linewidth=0.2)
    
    #add to the map the vegetobs (size based on density), the erbasts (color based on energy) and the carvizes (color based on energy)
    for row, rowList in enumerate(mapLists):
        for col, _ in enumerate(rowList):
            densityValue = densityLists[row][col]
            square = pat.Rectangle((col, parameters.getNumcells()-1-row), densityValue, densityValue, color = 'green')
            ax.add_patch(square)
            herd = herdLists[row][col]
            if herd != 0:
                for key in herd.animals:
                    circle = pat.Circle((col+random.uniform(0.15,0.85), parameters.getNumcells()-random.uniform(0.15,0.85)-row), 0.15, color = setErbastColor(herd.animals[key].getEnergy()/parameters.getMaxEnergy()))
                    ax.add_patch(circle)
            pride = prideLists[row][col]
            if pride != 0:
                for key in pride.animals:
                    triangle = pat.RegularPolygon((col+random.uniform(0.15,0.85), parameters.getNumcells()-random.uniform(0.15,0.85)-row), 3, 0.15, 0.0, color = setCarvizColor(pride.animals[key].getEnergy()/parameters.getMaxEnergy()))
                    ax.add_patch(triangle)


    plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    return 
    


