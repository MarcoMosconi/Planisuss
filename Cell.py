import random

NUMCELLS = 10
TYPES = ["Water", "Ground"]

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y =  y
        self.type = self.setType()
    
    def getCoordinates(self):
        print(self.x)
        print(self.y)  
  
    def getType(self):
        return self.type 

    def setType(self):
        if self.x == 0 or self.x == (NUMCELLS -1):
            return "Water" 
        if self.y == 0 or self.y == (NUMCELLS -1):
            return "Water"
        return random.choice(TYPES)
    def isGround(self):
        return self.type == "Ground"

cells = {}

for i in range(0, NUMCELLS):
    for j in range(0, NUMCELLS):
        cellname = ("c_" + str(i) + "_" + str(j)) 
        c = Cell(i, j)
        cells[cellname] = c 

# cells["c_3_7"].getCoordinates()

for i in range(0, NUMCELLS):
    ln = ''
    for j in range(0, NUMCELLS):
        cellname = ("c_" + str(i) + "_" + str(j)) 
        x = 'G' if cells[cellname].isGround() else '.'
        ln = ln + x + ' '
    print(ln)


