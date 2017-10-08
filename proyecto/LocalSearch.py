class LocalSearchQAP(object):
    
    def __init__(self, number, distance, flow, optValue):
        self.number = number
        self.distance = distance
        self.flow = flow
        self.optValue = optValue
        self.getInitSol()
        print("INICIAL",self.sol,self.solValue)

    def getInitSol(self):
        from random import shuffle
        l = [x for x in range(1,self.number+1)]
        shuffle(l)
        self.sol = l
        self.solValue = self.objectiveFunc(self.sol)

    def objectiveFunc(self,sol):
        value = 0
        for i in range(self.number):
            for j in range(self.number):
                value += self.flow[sol[i]-1][sol[j]-1]*self.distance[i][j]
        return value

    def greedy(self, numIter):
        for x in range(numIter):
            for i in range(self.number): 
                for j in range(1,self.number):
                    newSol = self.sol[:] 
                    newSol[i],newSol[j] = self.sol[j],self.sol[i]
                    newSolValue = self.objectiveFunc(newSol)

                    if newSolValue < self.solValue:
                        self.sol = newSol
                        self.solValue = newSolValue
                        print(self.sol,self.solValue)

                        if self.solValue == self.optValue:
                            return
        print("Hizo todas las iteraciones")