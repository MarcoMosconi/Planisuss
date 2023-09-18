import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

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
        prideEnergy = pride.getTotalEnergy()
        while erbAlive and prideEnergy > 0:
            if random.randint(0, erbEnergy+prideEnergy) > erbEnergy:
                pride.eat(erbEnergy)
                pride.winFight()
                erbAlive = False
                preyHerd.removeAnimal(preyErbKey)
            else:
                pride.failHunt()
                erbEnergy = preyHerd.animals[preyErbKey].getEnergy()
                prideEnergy = pride.getTotalEnergy()
                
    return






    