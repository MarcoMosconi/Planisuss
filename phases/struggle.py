import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from carvizes.setup import prides
from cells.setup import cells
from carvizes.fight import fight
from carvizes.hunt import hunt

def struggle():
    for cellname in cells:
        if cells[cellname].isGround():
            joiningPrides = []
            pridestoRemove = []
            for key in prides:
                if prides[key].cell == cellname:
                    joiningPrides.append(key)
            joiningPrides.sort(key=lambda x: prides[key].getNumAnimal())
            if len(joiningPrides) > 1:
                for key in joiningPrides:
                    if prides[key].getNumAnimal() == 0:
                        prides.pop(key)
                        pridestoRemove.append(key)
                for key in pridestoRemove:
                    joiningPrides.remove(key)
            while len(joiningPrides) > 1:
                pride1 = prides[joiningPrides[0]]
                pride2 = prides[joiningPrides[1]]
                avSocialAtt1 = pride1.getAvSocialAttitude()
                avSocialAtt2 = pride2.getAvSocialAttitude()
                if avSocialAtt1 > 0.5 and avSocialAtt2 > 0.5:
                    pride2.join(pride1)
                    prides.pop(joiningPrides[1])
                    joiningPrides.remove(joiningPrides[1])
                else:
                    fight(joiningPrides)
            hunt(prides[joiningPrides[0]])

                    



