import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.setup import herds
from vegetobs.setup import vegetobs

def visualize_E():
    totalNumberErbast = 0
    for key in herds:
        totalNumberErbast += herds[key].getNumErbast()
    return totalNumberErbast
        
def visualize_V():
    totalDensity = 0
    for cellname in vegetobs:
        totalDensity += vegetobs[cellname].getDensity()

    return totalDensity