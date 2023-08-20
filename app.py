from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import NUMDAYS
from phases.growing import growing
import matplotlib.pyplot as plt
from erbasts.setup import setupHerds
from phases.spawning import spawning
from phases.grazing import grazing
from phases.visualizing import visualizing
from phases.movement import movement

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


def main():
    for day in range(1, NUMDAYS + 1):
        totalDays.append(day)
        growing()
        movement()
        grazing()
        spawning()
        totalDensity, totalNumberErbast = visualizing()
        totalDensities.append(totalDensity)
        totalNumberErbasts.append(totalNumberErbast)
       

    fig, (ax, bx) = plt.subplots(1,2)
    ax.plot(totalDays, totalDensities, 'tab:green')
    ax.set_title("Total Daily Vegetob Density")
    bx.plot(totalDays, totalNumberErbasts)
    bx.set_title("Total Daily Erbast Number")
    plt.show()

def run():
    setup()
    main()

run()
