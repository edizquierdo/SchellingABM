import random
import numpy as np
import matplotlib.pyplot as plt

class City():

    def __init__(self, size, threshold):
        self.size = size        # Size of the neighborhood measured along one dimension
        self.threshold = threshold*8
        self.pop = np.zeros((size,size)) # Houses in a neighborhood
        self.emptyProb = 0.1    # Probability that a house will be empty
        self.raceProb = 0.5     # Probability that a house will have one race
        self.populate()

    def populate(self):
        # Populate the neighborhood at random
        for i in range(self.size):
            for j in range(self.size):
                # Flip a coin to see if the house is vacant or not
                if random.random() < self.emptyProb:
                    self.pop[i][j] = 0
                else:
                    # Flip another coin to see if the house will have race A or B living in it
                    if random.random() < self.raceProb:
                        self.pop[i][j] = 1
                    else:
                        self.pop[i][j] = -1

    def show(self,title):
        plt.imshow(self.pop, interpolation="nearest", cmap="bwr")
        plt.xticks([])
        plt.yticks([])
        plt.title(title)
        plt.show()

    def step(self):
        # pick random house
        i,j = self.randomHouse()
        # find a place to move to if it's unhappy
        if self.numberKin(i,j) < self.threshold:
            self.move(i,j)

    def randomHouse(self):
        found = False
        while not found:
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            if self.pop[i][j] != 0:
                found = True
        return i, j

    def randomVacant(self):
        found = False
        while not found:
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            if self.pop[i][j] == 0:
                found = True
        return i, j

    def numberKin(self, i, j):
        myrace = self.pop[i][j]
        kin = 0
        # Check neighbors' race and count kin
        for x in range(i-1,i+2):
            ni = x%self.size
            for y in range(j-1,j+2):
                nj = y%self.size
                if myrace == self.pop[ni][nj]:
                    kin += 1
        return kin-1

    def move(self, i, j):
        newi,newj = self.randomVacant()
        self.pop[newi][newj] = self.pop[i][j]
        self.pop[i][j] = 0

    def measureSeg(self):
        avgkin = 0.0
        for i in range(self.size-1):
            for j in range(self.size-1):
                k = self.numberKin(i,j)
                avgkin += k/8.0
        return avgkin/(self.size*self.size)
