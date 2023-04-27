import sys

sys.path[0] = "c:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\"

from erbasts.setup import herds

def spawn():
    totalNumberErbast = 0
    for key in herds:
        herds[key].spawns()
        totalNumberErbast += herds[key].getNumErbast()
    return totalNumberErbast
        

