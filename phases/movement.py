import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.setup import herds
from carvizes.setup import prides
from animals.findPrey import findPrey
from carvizes.pride import Pride
from keygenerator import generateKey

def movement():
    for key in herds:
        herd = herds[key]
        cellname = herd.cell
        prevCells = herd.prevCells
        num = herd.getNumAnimal()
        if num > 0:
            targetCellname, _, _ = findPrey(cellname, prevCells)    #finds the target cell
            if targetCellname != cellname:
                for key in herds:
                    if targetCellname == herds[key].cell:
                        herd.move(herds[key])               #move the herd's erbasts to the target cell
                        break
    for key in herds:
        herd= herds[key]
        herd.prevCells = []
        for cell in herd.currInCells:
            herd.prevCells.append(cell)     #put the cells of the new erbasts in prevCells so the herd won't move there the next day
        herd.currInCells = []

    
    newPrides = []
    for key in prides:
        pride = prides[key]
        cellname = pride.cell
        prevCells = pride.prevCells
        num = pride.getNumAnimal()
        if num > 0:
            _, targetCellname, _ = findPrey(cellname, prevCells)       #find the target cell
            if targetCellname != cellname:
                targetPride = Pride(targetCellname)                #creates new pride where to move the carvizes
                newPrides.append(targetPride)
                pride.move(targetPride)
    for newPride in newPrides:
        if newPride.getNumAnimal() > 0:
            prideKey = generateKey()
            prides[prideKey] = newPride             #adds the new prides to the dictionary "prides"
    return 