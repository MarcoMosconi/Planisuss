import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import random
from carvizes.setup import prides

def fight(key1, key2, prideList):
    pride1 = prides[key1]
    pride2 = prides[key2]
    totEnergy1 = 0
    totEnergy2 = 0
    for key in pride1.animals:
        totEnergy1 += pride1.animals[key].getEnergy()
    for key in pride2.animals:
        totEnergy2 += pride2.animals[key].getEnergy()
    if random.randint(0,totEnergy1+totEnergy2) > totEnergy1:
        prides.pop(key1)
        prideList.remove(key1)
        for key in pride2.animals:
            pride2.animals[key].socialAttitude += 2
    else:
        prides.pop(key2)
        prideList.remove(key2)
        for key in pride1.animals:
            pride1.animals[key].socialAttitude += 2
    return 
