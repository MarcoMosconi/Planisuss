import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from carvizes.setup import prides
from erbasts.setup import herds
import random

def hunt(pride):
    erbAlive = True
    for herdkey in herds:
        if herds[herdkey].cell == pride.cell:
            preyHerd = herds[herdkey]
            break
    revErbKeys = preyHerd.sortAnimals()  
    if len(revErbKeys) > 0: 
        erbKeys = revErbKeys[::-1]
        preyErbKey = erbKeys[0]
        erbEnergy = preyHerd.animals[preyErbKey].getEnergy()
        prideEnergy = 0
        for key in pride.animals:
            prideEnergy += pride.animals[key].getEnergy()
        while erbAlive and prideEnergy > 0:
            if random.randint(0, erbEnergy+prideEnergy) > erbEnergy:
                pride.eat(erbEnergy)
                for key in pride.animals:
                    pride.animals[key].socialAttitude += 0.1
                erbAlive = False
                preyHerd.removeAnimal(preyErbKey)
            else:
                deadCarviz = []
                for key in pride.animals:
                    pride.animals[key].socialAttitude -= 0.1
                    pride.animals[key].energy -= 2
                    if pride.animals[key].energy <= 0:
                        deadCarviz.append(key)
                for key in deadCarviz:
                    pride.removeAnimal(key)
                erbEnergy = preyHerd.animals[preyErbKey].getEnergy()
                prideEnergy = 0
                for key in pride.animals:
                    prideEnergy += pride.animals[key].getEnergy()
                
    return






    