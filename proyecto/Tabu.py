from QAP import QAP

MAX_T_LEN = 6

class Tabu(QAP):

    def makeMove(self, sol,T):
        for i in range(self.number): 
            for j in range(i+1,self.number):
                if (i,j) in T:
                    continue

                newSol = self.sol[:] 
                newSol[i],newSol[j] = self.sol[j],self.sol[i]
                newSolValue = self.objectiveFunc(newSol)

                if newSolValue < self.solValue:
                    self.sol = newSol
                    self.solValue = newSolValue
                    return (i,j), newSol,newSolValue

        return None, None, None

    def tabu(self, numIter):
        T = []

        for i in range(numIter):
            x,newSol,newSolValue = self.makeMove(self.sol,T)

            if x == None or self.solValue <= self.optValue:
                print("Iteracion ",i+1)
                return

            if len(T) == MAX_T_LEN:
                T.pop(0)

            T.append(x)

