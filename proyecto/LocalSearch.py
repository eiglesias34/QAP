from QAP import QAP

class LocalSearch(QAP):
    
    ## IMPROVE

    def improve(self): #fue una prueba, no usar
        localSol = []
        localSolValue = 0
        permutations = []
        for i in range(self.number):
            for j in range(i+1,self.number):
                permutations.append((i,j))

        import random
        randPermutations = random.sample(permutations, int(len(permutations)*40/100))
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
        prevSolValue = self.solValue
        for x in range(numIter):
            #if method():
            #    print(self.sol,self.solValue,"iter",x)
            method()

            if self.solValue <= self.optValue:
                return

            if prevSolValue == self.solValue:
                print("OPTIMO LOCAL - iter",x)
                return
            else:
                prevSolValue = self.solValue

        print("---",numIter,"iteraciones")

    def localSearchBest(self, numIter):
        self.localSearch(numIter, self.bestImprovement)

    def localSearchFirst(self, numIter):
        self.localSearch(numIter, self.firstImprovement)

    def localSearchRandom(self, numIter):
        self.localSearch(numIter, self.improve)