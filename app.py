from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import NUMDAYS
from phases.growing import growing
import matplotlib.pyplot as plt
import numpy as np
from erbasts.setup import setupHerds
from phases.spawning import spawning
from phases.grazing import grazing
from phases.visualizing import visualizing
from phases.movement import movement
from map import setupMap
from random import seed
import sys

seed(10)

totalDays = []
totalDensities = []
totalNumberErbasts = []

def setup():
    totalDays.append(0)
    setupCells()
    totalDensity = setupVegetobs()
    totalDensities.append(totalDensity)
    totalNumberErbast = setupHerds()
    totalNumberErbasts.append(totalNumberErbast)
    
    # A = np.asarray(setupMap())
    # colors = ['dodgerblue', 'saddlebrown']
    # cmap = ListedColormap(colors)
    # plt.imshow(A, cmap=cmap)

def main():
    fig, (ax, bx,cx) = plt.subplots(1,3)
    ax.set_title("Total Daily Vegetob Density")
    bx.set_title("Total Daily Erbast Number")
    for day in range(1, NUMDAYS + 1):
        print('--------------DAY', day)
        totalDays.append(day)
        growing()
        movement()
        # print('---------------')
        grazing()
        spawning()
        totalDensity, totalNumberErbast = visualizing()
        totalDensities.append(totalDensity)
        totalNumberErbasts.append(totalNumberErbast)
        ax.plot(totalDays, totalDensities, 'tab:green')
        bx.plot(totalDays, totalNumberErbasts)
        setupMap(cx)
        plt.pause(0.001)
    plt.show()

def run():
    setup()
    main()

# with open('C:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\ex.txt', 'w') as file:
#     original_stdout = sys.stdout
#     sys.stdout = file
#     run()
#     sys.stdout = original_stdout

run()
