from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import NUMDAYS
from phases.growing import growing
import matplotlib.pyplot as plt
import numpy as np
from erbasts.setup import setupHerds
from carvizes.setup import setupPrides
from phases.spawning import spawning
from phases.grazing import grazing
from phases.visualizing import visualizing
from phases.movement import movement
from phases.struggle import struggle
from map import setupMap
from random import seed
from matplotlib.animation import FuncAnimation 
import sys

seed(10)

totalDays = []
totalDensities = []
totalNumberErbasts = []
totalNumberCarvizes = []

def setup():
    totalDays.append(0)
    setupCells()
    totalDensity = setupVegetobs()
    totalDensities.append(totalDensity)
    totalNumberErbast = setupHerds()
    totalNumberErbasts.append(totalNumberErbast)
    totalNumberCarviz = setupPrides()
    totalNumberCarvizes.append(totalNumberCarviz)
    
    # A = np.asarray(setupMap())
    # colors = ['dodgerblue', 'saddlebrown']
    # cmap = ListedColormap(colors)
    # plt.imshow(A, cmap=cmap)

def main():
    fig, ((ax, bx),(cx,dx)) = plt.subplots(2,2)
    ax.set_title("Total Daily Vegetob Density")
    bx.set_title("Total Daily Erbast Number")
    cx.set_title("Total Daily Carviz Number")
    dx.set_aspect('equal')
    dx.set_title("Map")
    for day in range(1, NUMDAYS + 1):
        # print('--------------DAY', day)
        totalDays.append(day)
        growing()
        movement()
        # print('---------------')
        grazing()
        struggle()
        spawning()
        totalDensity, totalNumberErbast, totalNumberCarviz = visualizing()
        totalDensities.append(totalDensity)
        totalNumberErbasts.append(totalNumberErbast)
        totalNumberCarvizes.append(totalNumberCarviz)
        ax.plot(totalDays, totalDensities, 'tab:green')
        bx.plot(totalDays, totalNumberErbasts, 'tab:orange')
        cx.plot(totalDays, totalNumberCarvizes, 'tab:red')
        setupMap(dx)
        # anim = FuncAnimation(fig, setupMap(dx), interval=0)
        plt.pause(0.01)
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
