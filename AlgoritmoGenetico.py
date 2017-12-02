from QAP_Poblacion import Solution,QAP_Poblacion as QAP
from random import randint,random,sample
from random import shuffle

MUTATION = 0.2

class GenecticAlgorithm(QAP):

    def firstImprovement(self,sol,solValue):
        for i in range(self.number): 
            for j in range(i+1,self.number):
                if (i,j) in T:
                    continue
                newSol = sol[:] 
                newSol[i],newSol[j] = sol[j],sol[i]
                newSolValue = self.objectiveFunc(newSol)

                if newSolValue < solValue:
                    return newSol,newSolValue

        return sol,solValue

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

    def crossoverChild(self, parentA, parentB):
        '''
        Crea un hijo similar al padre B con 20 porciento del padre A

        Parámetros:
        parentA -- Padre A 
        parentB -- Padre B
        '''
        child = Solution(self.number,self.distance,self.flow,parentB)

        #obtengo los indices del 20 porciento de las componentes de padre A
        randParentA = sample(parentA.sol, int(len(parentA.sol)*MUTATION))

        #creo hijo
        for aElem in randParentA:
            i = parentA.sol.index(aElem) #indice en A del componente del padre A
            j = parentB.sol.index(aElem) #indice en B del componente del padre A
            bElem = parentB.sol[i] #componente del padre B en el indice del componente del A
            if i != j:
                #print("child[",i,"],child[",j,"] = B[",j,"],B[",i,"]","=>",child.sol[i],child.sol[j],"=",parentB.sol[j],parentB.sol[i])
                child.sol[i],child.sol[j] = parentB.sol[j],parentB.sol[i]

        child.solValue = child.objectiveFunc(child.sol,self.number,self.distance,self.flow)
        #print("child",child.sol)
        return child

    def crossover(self, parentA, parentB):
        '''
        se intercambia un 20 porcieto de las componentes del padre

        Parámetros:
        parentA -- Padre A 
        parentB -- Padre B
        '''
        childC = self.crossoverChild(parentB, parentA)
        childD = self.crossoverChild(parentA, parentB)

        return childC, childD
    
    def genetic(self, numIter):
        #for x in xrange(len(self.population)):
        #    self.population[x].sol, self.population[x].solValue = self.firstImprovement(self.population[x].sol, self.population[x].solValue)

        noImprovement = 0

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
                print("Iteracion ",x+1)
                return

            #se detiene si obtiene el optimo
            if self.bestvalue <= self.optValue:
                print("Iteracion ",x+1)
                return