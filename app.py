from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import NUMDAYS
from phases.growing import growing

def setup():
    setupCells()
    setupVegetobs()

def main():
    for day in range(0, NUMDAYS):
        growing()

def run():
    setup()
    main()

run()
