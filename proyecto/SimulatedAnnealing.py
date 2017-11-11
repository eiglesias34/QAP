from QAP import QAP
from math import exp
from random import randint,random

ALFA = 0.5

class SimulatedAnnealing(QAP):

    def setTemperature(self, temp):
        return temp * ALFA 

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

    def annealing(self, numIter):
        T = self.number**6
        accept,improves = 0,0
        iterr = 0

        for x in range(numIter):
            noni = 0

            lastAccept = accept
            lastImproves = improves

            #cicla hasta que no mejore en n/2 iteraciones continuas
            while noni < self.number/2:
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
                    #print("difE,T,P",difE,T,P)
                    if random() <= P:
                        accept+=1
                    else:
                        continue

                self.sol = newSol
                self.solValue = newSolValue

            #si por n iteraciones no mejora ni acepta una solucion, se retorna
            iterr = iterr+1 if lastImproves == improves and lastAccept == accept else 0
            if iterr >= self.number:
                print("Iteracion ",x+1,"-> No mejora, ni acepta")
                return

            #print("T,accept,improves",T,accept,improves)
            T = self.setTemperature(T)

            if self.solValue <= self.optValue or T<=0:
                print("Iteracion ",x+1)
                return