from QAP import QAP

MAX_T_LEN = 4

class Tabu(QAP):

    def makeMove(self, sol,T):
        localSol = []
        localSolValue = 0
        permutation = (0,0)

        for i in range(self.number):
            for j in range(i+1,self.number):
                if (i,j) not in T:
                    newSol = self.sol[:] 
                    newSol[i],newSol[j] = self.sol[j],self.sol[i]
                    newSolValue = self.objectiveFunc(newSol)

                    if localSolValue == 0 or newSolValue < localSolValue:
                        localSol = newSol
                        localSolValue = newSolValue
                        permutation = (i,j)

        return permutation,localSol,localSolValue

    def tabu(self, numIter):
        T = []

        for i in range(numIter):
            x,newSol,newSolValue = self.makeMove(self.sol,T)
            T.append(x)

            if newSolValue < self.solValue:
                self.solValue = newSolValue
                self.sol = newSol 

            if self.solValue <= self.optValue:
                print("Iteracion ",x+1)
                return

            if len(T) == MAX_T_LEN:
                T.pop(0)


