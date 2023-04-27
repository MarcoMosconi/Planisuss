from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import NUMDAYS
from phases.growing import growing
import matplotlib.pyplot as plt
from erbasts.setup import setupHerds
from phases.spawning import spawning

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
        totalDensity = growing()
        totalDensities.append(totalDensity)
        totalNumberErbast = spawning()
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
