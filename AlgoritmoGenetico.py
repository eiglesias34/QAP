from QAP_Poblacion import Solution,QAP_Poblacion as QAP
from SimulatedAnnealing import SimulatedAnnealing
from LocalSearch import LocalSearch
from random import randint,random,sample
from random import shuffle

MUTATION = 0.2

class GenecticAlgorithm(QAP):

    def objectiveFunc(self,sol):
        '''
        Funcion objetivo
        '''
        value = 0
        for i in range(self.number):
            for j in range(self.number):
                value += self.flow[sol[i]-1][sol[j]-1]*self.distance[i][j]
        return value

    def firstImprovement(self,sol,solValue):
        for i in range(self.number): 
            for j in range(i+1,self.number):
                newSol = sol[:] 
                newSol[i],newSol[j] = sol[j],sol[i]
                newSolValue = self.objectiveFunc(newSol)

                if newSolValue < solValue:
                    return newSol,newSolValue

        return sol,solValue

    def localSearch(self, numIter):
        '''
        Dismunuye la temperatura

        Parámetros:
        numIter -- numero maximo de iteraciones
        method -- mejoramiento (localSearchBest,localSearchFirst,localSearchRandom)
        '''
        prevSolValue = self.bestvalue
        for x in range(numIter):
            #if method():
            #    print(self.sol,self.solValue,"iter",x)
            self.bestindvidual, self.bestvalue = self.firstImprovement(self.bestindvidual, self.bestvalue)

            if self.bestvalue <= self.optValue:
                return 

            if prevSolValue == self.bestvalue:
                #print("OPTIMO LOCAL - iter",x)
                return 
            else:
                prevSolValue = self.bestvalue

    def fitnessFunctions(self,solValue):
        return 1/solValue

    def getParents(self,population):
        '''
        Dada una poblacion, devuelve una lista de pares 
        Cada par contiene los indices de los padres en el arreglo 
        de poblacion

        Parámetros:
        population -- poblacion
        '''
        l = [x for x in range(self.populationSize)]
        shuffle(l)
        return zip(l[0::2], l[1::2])

    def crossover(self, parentA, parentB):
        '''
        Crea un hijo similar al padre B con 20 porciento del padre A

        Parámetros:
        parentA -- Padre A 
        parentB -- Padre B
        '''
        childD = Solution(self.number,self.distance,self.flow,parentB)
        childC = Solution(self.number,self.distance,self.flow,parentA)
        #obtengo los indices del 20 porciento de las componentes de padre A
        randParentA = sample(range(0,len(parentA.sol)), int(len(parentA.sol)*MUTATION))

        #creo hijo
        for aElem in randParentA:

            i = aElem #indice en A del componente del padre A
            j = parentB.sol.index(parentA.sol[aElem]) #indice en B del componente del padre A
            if i != j:
                #print("child[",i,"],child[",j,"] = B[",j,"],B[",i,"]","=>",child.sol[i],child.sol[j],"=",parentB.sol[j],parentB.sol[i])
                childD.sol[i],childD.sol[j] = parentB.sol[j],parentB.sol[i]

            i = aElem #indice en A del componente del padre A
            j = parentA.sol.index(parentB.sol[aElem]) #indice en B del componente del padre A
            if i != j:
                #print("child[",i,"],child[",j,"] = B[",j,"],B[",i,"]","=>",child.sol[i],child.sol[j],"=",parentB.sol[j],parentB.sol[i])
                childC.sol[i],childC.sol[j] = parentA.sol[j],parentA.sol[i]

        childD.solValue = childD.objectiveFunc(childD.sol,self.number,self.distance,self.flow)
        #print("child",child.sol)

        childC.solValue = childC.objectiveFunc(childC.sol,self.number,self.distance,self.flow)
        #print("child",child.sol)

        return childC, childD
    
    def genetic(self, numIter):
        #for x in range(len(self.population)):
        #    qap = SimulatedAnnealing(self.number, self.distance, self.flow, self.optValue, self.population[x].sol)
        #    qap.annealing(numIter)
        #    self.population[x].sol, self.population[x].solValue = qap.sol, qap.solValue

        #self.bestindvidual,self.bestvalue = self.getBestIndividual()
            

        noImprovement = 0

        print(abs(self.bestvalue-self.optValue)/self.optValue * 100)

        for x in range(numIter):

            parentsIndices = self.getParents(self.population)

            for i,j in parentsIndices:
                parentA = self.population[i]
                parentB = self.population[j]
                #sprint("padres",i,j)
                #sprint("A",parentA.sol)
                #sprint("B",parentB.sol)

                childC, childD = self.crossover(parentA, parentB)

                #cada n generacion cambiamos el peor de la poblacion
                if x > 0 and x % self.number != 0:
                    if childC.solValue < parentA.solValue:
                        self.population[i] = childC
                        #print("cambia padre a")

                    if childD.solValue < parentB.solValue:
                        self.population[j] = childD
                        #print("cambia padre b")

                else:
                    pos, worstindividual, worstvalue = self.getWorstIndividual()
                    if childC.solValue < worstvalue:
                        self.population[pos] = childC
                        #print("cambia padre peor por child C")

                    pos, worstindividual, worstvalue = self.getWorstIndividual()
                    if childD.solValue < worstvalue:
                        self.population[pos] = childD
                        #print("cambia padre peor por child D")

            #busca al mejor de la generacion
            lastBestValue = self.bestvalue
            self.bestindvidual, self.bestvalue = self.getBestIndividual()

            if self.bestvalue != lastBestValue:
                noImprovement = 0
            else:#aumenta el contador si no mejora
                noImprovement += 1

            #no mejora durante n iteraciones
            if noImprovement >= self.number:
                print(abs(self.bestvalue-self.optValue)/self.optValue * 100)
                qap = LocalSearch(self.number, self.distance, self.flow, self.optValue, self.bestindvidual)
                qap.localSearchFirst(numIter)
                self.bestindvidual, self.bestvalue = qap.sol, qap.solValue
                print(abs(self.bestvalue-self.optValue)/self.optValue * 100)
                print("Iteracion ",x+1)
                return

            #se detiene si obtiene el optimo
            if self.bestvalue <= self.optValue:
                print("Iteracion ",x+1)
                return
