import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from carvizes.setup import prides

def fight(prideList):
    pride1 = prides[prideList[0]]
    pride2 = prides[prideList[1]]
    totEnergy1 = pride1.getTotalEnergy()
    totEnergy2 = pride2.getTotalEnergy()
    if random.randint(0,totEnergy1+totEnergy2) > totEnergy1:    #the two prides are taken and based on their total energy one wins and the other is defeated
        prides.pop(prideList[0])
        prideList.remove(prideList[0])
        pride2.winFight()
    else:
        prides.pop(prideList[1])
        prideList.remove(prideList[1])
        pride1.winFight()
    return 
