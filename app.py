from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import NUMDAYS
from phases.growing import growing
import matplotlib.pyplot as plt


totalDays = []
totalDensities = []

def setup():
    totalDays.append(0)
    setupCells()
    totalDensity = setupVegetobs()
    totalDensities.append(totalDensity)


def main():
    for day in range(1, NUMDAYS + 1):
        totalDays.append(day)
        totalDensity = growing()
        totalDensities.append(totalDensity)
        
    fig, ax = plt.subplots()
    ax.plot(totalDays, totalDensities)
    ax.set_title("Total Daily Vegetob Density")
    plt.show()

def run():
    setup()
    main()

run()
