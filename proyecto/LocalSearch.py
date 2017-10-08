class LocalSearchQAP(object):
    
    def __init__(self, number, distance, flow, optValue, initSol = None):
        self.number = number
        self.distance = distance
        self.flow = flow
        self.optValue = optValue
        
        if initSol:
            self.sol = initSol
            self.solValue = self.objectiveFunc(initSol)
        else:
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

    ## IMPROVE

    def improve(self): #fue una prueba, no usar
        localSol = []
        localSolValue = 0
        permutations = []
        for i in range(self.number):
            for j in range(i+1,self.number):
                    permutations.append((i,j))

        import random
        randPermutations = random.sample(permutations, int(len(permutations)/2))
        for i,j in randPermutations:
            newSol = self.sol[:] 
            newSol[i],newSol[j] = self.sol[j],self.sol[i]
            newSolValue = self.objectiveFunc(newSol)
            if newSolValue < self.solValue:
                localSol = newSol
                localSolValue = newSolValue

        if localSol:
            self.sol = localSol
            self.solValue = localSolValue
            return True

    def firstImprovement(self):
        for i in range(self.number): 
            for j in range(i+1,self.number):
                newSol = self.sol[:] 
                newSol[i],newSol[j] = self.sol[j],self.sol[i]
                newSolValue = self.objectiveFunc(newSol)

                if newSolValue < self.solValue:
                    self.sol = newSol
                    self.solValue = newSolValue
                    return True

    def bestImprovement(self):
        localSol = []
        localSolValue = 0

        for i in range(self.number): 
            for j in range(i+1,self.number):
                newSol = self.sol[:] 
                newSol[i],newSol[j] = self.sol[j],self.sol[i]
                newSolValue = self.objectiveFunc(newSol)

                if newSolValue < self.solValue:
                    localSol = newSol
                    localSolValue = newSolValue

        if localSol:
            self.sol = localSol
            self.solValue = localSolValue
            return True

    ## LOCAL SEARCH

    def localSearch(self, numIter, method):
        for x in range(numIter):
            if method():
                print(self.sol,self.solValue,"iter",x)
                
            if self.solValue <= self.optValue:
                return
        print("-->",numIter,"iteraciones")

    def localSearchBest(self, numIter):
        self.localSearch(numIter, self.firstImprovement)

    def localSearchFirst(self, numIter):
        self.localSearch(numIter, self.bestImprovement)