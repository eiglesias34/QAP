from QAP import QAP

MAX_T_LEN = 6

class Tabu(QAP):

    def firstImprovement(self,sol,solValue,T):
        for i in range(self.number): 
            for j in range(i+1,self.number):
                if (i,j) in T:
                    continue
                newSol = sol[:] 
                newSol[i],newSol[j] = sol[j],sol[i]
                newSolValue = self.objectiveFunc(newSol)

                if newSolValue < solValue:
                    return (i,j),newSol,newSolValue

        return None, sol,solValue

    def localSearch(self,T):
        sol = self.sol[:]
        solValue = self.solValue
        pair = None
        for x in range(500):
            #return si es el optimo o la solucion no mejoro
            if solValue <= self.optValue:
                return pair

            p, sol, solValue = self.firstImprovement(sol, solValue,T)
            if p:
                pair = p

            #return si es el optimo o la solucion no mejoro
            if solValue == self.solValue:
                return pair
            else:
                self.solValue = solValue
                self.sol = sol

        return pair

    def tabu(self, numIter):
        T = []

        for i in range(numIter):
            x,self.sol,self.solValue = self.firstImprovement(self.sol,self.solValue,T)

            #return si es el optimo o la solucion no mejoro
            if x == None or self.solValue <= self.optValue:
                print("Iteracion ",i+1)
                return

            if len(T) == MAX_T_LEN:
                T.pop(0)

            T.append(x)

