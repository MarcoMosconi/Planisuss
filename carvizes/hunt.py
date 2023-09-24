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
        if herds[herdkey].cell == pride.cell:   #finds the herd in the pride's cell
            preyHerd = herds[herdkey]
            break
    revErbKeys = preyHerd.sortAnimals()  
    if len(revErbKeys) > 0: 
        erbKeys = revErbKeys[::-1]
        preyErbKey = erbKeys[0]     #takes the erbast with most energy
        erbEnergy = preyHerd.animals[preyErbKey].getEnergy()
        prideEnergy = pride.getTotalEnergy()
        while erbAlive and prideEnergy > 0:     #until one of them dies based on their energies
            if random.randint(0, erbEnergy+prideEnergy) > erbEnergy:    #if the pride wins it eats the erbast which is removed from its herd dictionary
                pride.eat(erbEnergy)
                pride.winFight()
                erbAlive = False
                preyHerd.removeAnimal(preyErbKey)
            else:                                                       #otherwise it fails the hunt and their energy is computed again
                pride.failHunt()
                erbEnergy = preyHerd.animals[preyErbKey].getEnergy()
                prideEnergy = pride.getTotalEnergy()
                
    return






    