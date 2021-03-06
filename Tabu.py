#Fecha: noviembre, 2017

from QAP import QAP

MAX_T_LEN = 6

class Tabu(QAP):

    def firstImprovement(self,sol,solValue,T):
        '''
        Busqueda local primer mejor

        Parametros:
        sol -- solucion 
        solValue -- valor de la solucion
        T -- lista Tabu
        '''
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

    def tabu(self, numIter):
        '''
        Metaheuristica Tabu

        Parametros:
        numIter -- numero maximo de iteraciones
        '''
        T = []

        for i in range(numIter):
            x,self.sol,self.solValue = self.firstImprovement(self.sol,self.solValue,T)

            #return si es el optimo o la solucion no mejoro
            if x == None or self.solValue <= self.optValue:
                print("Iteracion ",i+1)
                return

            #si la lista esta llena, se saca el primer elemento, 
            #es decir, el movimiento tabu con mas tiempo en la lista
            if len(T) == MAX_T_LEN:
                T.pop(0)

            T.append(x)

