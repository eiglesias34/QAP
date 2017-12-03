from QAP_Poblacion import Solution,QAP_Poblacion as QAP
from LocalSearch import LocalSearch
from random import randint,random,sample
from random import shuffle

Q = 100

class AntColony(QAP):

	def createPheromeTrail(self, solValue):
		PT = [[1/(solValue*Q)]*self.number]*self.number
		return PT
	
	def colony(self, numIter):

		PT = self.createPheromeTrail()

		for x in range(numIter):
			for pos in len(self.population):
				ant = self.population[pos]

				qap = LocalSearch(self.number, self.distance, self.flow, self.optValue, ant.sol)
                qap.localSearchFirst(numIter)
                self.population[pos].sol, self.population[pos].solValue = qap.sol, qap.solValue 
