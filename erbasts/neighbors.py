import sys
import os


current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from cells.findMaxDensity import findMaxDensity
from erbasts.setup import herds

def neighbors():
    for key in herds:
        cellname = herds[key].cell
        _, killHerd = findMaxDensity(cellname)
        if killHerd:
            print('kill', cellname)
            herds[key].kill()
        
    
    
         