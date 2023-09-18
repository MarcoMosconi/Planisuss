# NUMCELLS = 10
# CELL_PROBABILITY = 0.2
# GROWING = 0.8
# NUMDAYS = 50
# MAX_DENSITY = 100
# MAX_ENERGY = 100
# MAX_LIFE = 30
# MAX_HERD = 10
# MAX_PRIDE = 10
# ERBAST_PROBABILITY = 0.3
# CARVIZ_PROBABILITY = 0.8
# AGING = 1
# NEIGHBORHOOD = 1
# MIN_SOCIAL_ATTITUDE = 0.4
# MOVE_PROBABILITY = 0.3  

class Parameters():
    def __init__(self):
        self.Numcells = 15
        self.Cell_Probability = 0.2
        self.Growing = 0.8
        self.Numdays = 250
        self.Max_Density = 100
        self.Max_Energy = 100
        self.Max_Life = 30
        self.Max_Herd = 10
        self.Max_Pride = 10
        self.Erbast_Probability = 0.3
        self.Carviz_Probability = 0.8
        self.Aging = 1
        self.Neighborhood = 1
        self.Min_Social_Attitude = 0.4
        self.Move_Probability = 0.3  

    def getNumcells(self):
        return self.Numcells

    def getCellProb(self):
        return self.Cell_Probability
    
    def getGrowing(self):
        return self.Growing

    def getNumdays(self):
        return self.Numdays

    def getMaxDensity(self):
        return self.Max_Density

    def getMaxEnergy(self):
        return self.Max_Energy
    
    def getMaxLife(self):
        return self.Max_Life

    def getMaxHerd(self):
        return self.Max_Herd
    
    def getMaxPride(self):
        return self.Max_Pride

    def getErbastProb(self):
        return self.Erbast_Probability
    
    def getCarvizProb(self):
        return self.Carviz_Probability

    def getAging(self):
        return self.Aging

    def getNeighborhood(self):
        return self.Neighborhood

    def getMinSocAtt(self):
        return self.Min_Social_Attitude
    
    def getMoveProb(self):
        return self.Move_Probability
    
parameters = Parameters()