import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.setup import herds
from carvizes.setup import prides

def spawning():
    for key in herds:
        herds[key].spawns()

    for key in prides:
        prides[key].spawns()