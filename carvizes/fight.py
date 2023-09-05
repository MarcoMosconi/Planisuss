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
    totEnergy1 = 0
    totEnergy2 = 0
    for key in pride1.animals:
        totEnergy1 += pride1.animals[key].getEnergy()
    for key in pride2.animals:
        totEnergy2 += pride2.animals[key].getEnergy()
    if random.randint(0,totEnergy1+totEnergy2) > totEnergy1:
        prides.pop(prideList[0])
        prideList.remove(prideList[0])
        for key in pride2.animals:
            if pride2.animals[key].socialAttitude < 1:
                pride2.animals[key].socialAttitude += 0.1
    else:
        prides.pop(prideList[1])
        prideList.remove(prideList[1])
        for key in pride1.animals:
            if pride1.animals[key].socialAttitude < 1:
                pride1.animals[key].socialAttitude += 0.1
    return 
