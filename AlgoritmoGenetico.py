# -*- coding: utf-8 -*-
#Fecha: diciembre, 2017
from random import randint,random,sample
from random import shuffle
#proyecto
from QAP_Poblacion import Solution,QAP_Poblacion as QAP

MUTATION = 0.2

class GenecticAlgorithm(QAP):

    def getParents(self,population):
        '''
        Dada una poblacion, devuelve una lista de pares 
        Cada par contiene los indices de los padres en el arreglo 
        de poblacion

        Parametros:
        population -- poblacion
        '''
        l = [x for x in range(self.populationSize)]
        shuffle(l)
        return zip(l[0::2], l[1::2])

    def crossover(self, parentA, parentB):
        '''
        Crea un hijo similar al padre B con 20 porciento del padre A
        Crea un hijo similar al padre A con 20 porciento del padre B
        Parámetros:
        parentA -- Padre A 
        parentB -- Padre B
        '''
        childD = Solution(self.number,self.distance,self.flow,parentB)
        childC = Solution(self.number,self.distance,self.flow,parentA)
        #obtengo los indices del 20 porciento 
        randParent = sample(range(len(parentA.sol)), int(len(parentA.sol)*MUTATION))
        #print(randParent)
        #print("A",parentA.sol)
        #print("B",parentB.sol)

        #creo hijo
        for i in randParent:
            aElem = parentA.sol[i]
            bElem = parentB.sol[i]

            if aElem == bElem:
                continue

            j = childC.sol.index(bElem)
            childC.sol[i],childC.sol[j] = bElem,childC.sol[i]

            j = childD.sol.index(aElem)
            childD.sol[i],childD.sol[j] = aElem,childD.sol[i]

        childC.solValue = childC.objectiveFunc(childC.sol,self.number,self.distance,self.flow)
        #print("C",childC.sol)

        childD.solValue = childD.objectiveFunc(childD.sol,self.number,self.distance,self.flow)
        #print("D",childD.sol)

        return childC, childD
    
    def genetic(self, numIter):
        noImprovement = 0

        print("Mejor inicial",abs(self.bestvalue-self.optValue)/self.optValue * 100)

        for x in range(numIter):

            parentsIndices = self.getParents(self.population)

            improvement = False

            for i,j in parentsIndices:
                parentA = self.population[i]
                parentB = self.population[j]
                #print("padres",i,j)

                childC, childD = self.crossover(parentA, parentB)

                #cada n generacion cambiamos el peor de la poblacion
                if x > 0 and x % self.number != 0:
                    if childC.solValue < parentA.solValue:
                        self.population[i] = childC
                        improvement=True
                        #print("cambia padre a")

                    if childD.solValue < parentB.solValue:
                        self.population[j] = childD
                        improvement=True
                        #print("cambia padre b")

                else:
                    pos, worstindividual, worstvalue = self.getWorstIndividual()
                    if childC.solValue < worstvalue:
                        self.population[pos] = childC
                        improvement=True
                        #print("cambia padre peor por child C")

                    pos, worstindividual, worstvalue = self.getWorstIndividual()
                    if childD.solValue < worstvalue:
                        self.population[pos] = childD
                        improvement=True
                        #print("cambia padre peor por child D")

            #busca al mejor de la generacion
            self.bestindvidual, self.bestvalue = self.getBestIndividual()

            if improvement: 
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
