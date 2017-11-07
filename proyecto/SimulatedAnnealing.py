from QAP import QAP
from math import exp
from random import randint,random

ALFA = 0.5
T0 = 100

class SimulatedAnnealing(QAP):

    def setTemperature(self, temp):
        return temp * ALFA #temp - 0.0001 #

    def acceptanceProbability(self,difE,T):
        try:
            return exp(-difE / T)    
        except OverflowError:
            return float('inf')

    def makeMove(self, sol):
        i = randint(0, len(sol)-1)
        j = randint(0, len(sol)-1)
        while j == i:
            j = randint(0, len(sol)-1)

        newSol = sol[:]
        newSol[i] = sol[j]
        newSol[j] = sol[i]

        return newSol

    def annealing(self, numIter, nonImprove):
        T = self.number*self.number
        accept,improves = 0,0

        for x in range(numIter):
            noni = 0
            while noni < nonImprove:
                #new neighbour
                newSol = self.makeMove(self.sol)
                #neighbour energy
                newSolValue = self.objectiveFunc(newSol)

                difE = newSolValue - self.solValue
                if difE < 0.0:
                    improves += 1
                else:
                    noni+=1
                    P = self.acceptanceProbability(difE,T)
                    print("difE,T,P",difE,T,P)
                    if random() <= P:
                        accept+=1
                    else:
                        continue

                self.sol = newSol
                self.solValue = newSolValue

            T = self.setTemperature(T)
            print("accept,improves",accept,improves)

            if self.solValue <= self.optValue:
                print("Iteracion ",x+1)
                return