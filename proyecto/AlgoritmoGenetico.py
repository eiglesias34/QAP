from QAP import QAP
from QAP_Poblacion import QAP_Poblacion
from math import exp
from random import randint,random

Population_Mutation = 0.2

class GenecticAlgorithm(QAP_Poblacion):

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

	def crossover(self, parentA, parentB):
		i = randint(0, len(sol)-1)

        childC.sol = parentA.sol[:]
        childD.sol = parentB.sol[:]
        newSol[i] = sol[j]
        newSol[j] = sol[i]

        return childC, childD
	
	def genetic(self, numIter, nonImprove):
		for x in xrange(len(self.population)):
			self.population[x].sol, self.population[x].solValue = self.firstImprovement(self.population[x].sol, self.population[x].solValue)

		for x in xrange(numIter):
			noni = 0
			while noni < nonImprove:
				i = randint(0, len(sol)-1)
	        	j = randint(0, len(sol)-1)
	        	parentA = self.population[i]
	        	parentB = self.population[j]
	        	childC, childD = self.crossover(parentA, parentB)

	        	if x%self.number != 0:
	        		if childC.solValue < parentA.solValue:
	        			self.population[i] = childC

	        		if childD.solValue < parentB.solValue:
	        			self.population[j] = childD

	            else:
	            	pos, worstindividual, worstvalue = self.getWorstIndividual()
	            	if childC.solValue < worstvalue:
	            		self.population[x] = childC

	            	pos, worstindividual, worstvalue = self.getWorstIndividual()
	            	if childC.solValue < worstvalue:
	            		self.population[x] = childD

	            self.bestindvidual, self.bestvalue = self.getBestIndividual()

	            if self.bestvalue <= self.optValue:
	                print("Iteracion ",x+1)
	                return