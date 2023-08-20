from erbasts.setup import herds
from cells.findMaxDensity import findMaxDensity

def movement():
    for key in herds:
        herd = herds[key]
        cellname = herd.cell
        num = herd.getNumErbast()
        if num > 0:
            targetCellname = findMaxDensity(cellname)
    return 