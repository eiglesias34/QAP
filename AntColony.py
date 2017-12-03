from QAP_Poblacion import Solution,QAP_Poblacion as QAP
from LocalSearch import LocalSearch
from random import randint,random,sample,uniform
from random import shuffle

Q = 100
q = 0.9
alpha = 0.2

class AntColony(QAP):

	def objectiveFunc(self,sol,solLen,distance,flow):
		value = 0
		for i in range(solLen):
			for j in range(solLen):
				value += flow[sol[i]-1][sol[j]-1]*distance[i][j]
		return value

	def updatePheromeTrail(self, PT, sol, solValue):
		for i in range(0, self.number):
			for j in range(0, self.number):
				PT[i][j] = (1 - alpha) * PT[i][j]

		for i in range(0, self.number):
			PT[i][sol[i]-1] = PT[i][sol[i]-1] + alpha/solValue

		return PT
		

	def getDividor(self, sol, PT):

		dividor = 0

		for i in range(self.number): 
			for j in range(i+1,self.number):
				dividor += PT[i][sol[j]-1] + PT[j][sol[i]-1]

		return dividor

	def permutation(self, sol, PT):

		randSwap = sample(range(len(sol)), int(len(sol)/3))
		i = randint(0, self.number-1)
		j_probability = uniform(0, 1)
		max_value = 0

		for j in randSwap:
			if i != j:
				if j_probability <= q:
					posible_value = PT[i][sol[j]-1] + PT[j][sol[i]-1]	
				else:
					dividor = self.getDividor(sol, PT)
					posible_value = (PT[i][sol[j]-1] + PT[j][sol[i]-1])/dividor

				if max_value < posible_value:
					max_value = posible_value
					newSol = sol[:] 
					newSol[i],newSol[j] = sol[j], sol[i]

		return newSol


	def createPheromeTrail(self, solValue):

		PT = [[1/(solValue*Q) for x in range(self.number)] for y in range(self.number)] 
		return PT
	
	def colony(self, numIter):

		noImprovement = 0
		PT = self.createPheromeTrail(self.bestvalue)
		Intensification = True
		for x in range(numIter):
			improvement = False

			for pos in range(self.populationSize):
				ant = Solution(self.number,self.distance,self.flow, self.population[pos]) 

				ant.sol = self.permutation(ant.sol, PT)
				ant.solValue = self.objectiveFunc(ant.sol, self.number, self.distance, self.flow)

				qap = LocalSearch(self.number, self.distance, self.flow, self.optValue, ant.sol)
				qap.localSearchFirst(numIter)
				ant.sol, ant.solValue = qap.sol[:], qap.solValue 
				if Intensification:
					if ant.solValue < self.population[pos].solValue:
						self.population[pos].sol, self.population[pos].solValue = ant.sol, ant.solValue	
					else:
						continue
				else:
					self.population[pos].sol, self.population[pos].solValue = ant.sol, ant.solValue

			for pos in range(len(self.population)):
				if self.population[pos].solValue < self.bestvalue:
					self.bestindividual, self.bestvalue = self.getBestIndividual()
					improvement = True
					Intensification = True

			PT = self.updatePheromeTrail(PT, self.bestindividual, self.bestvalue)

			if improvement: #self.bestvalue != lastBestValue:
				noImprovement = 0
			else:#aumenta el contador si no mejora
				noImprovement += 1

			if noImprovement >= self.number/2:
				print("Iteracion ",x+1)
				return

            #se detiene si obtiene el optimo
			if self.bestvalue <= self.optValue:
				print("Iteracion ",x+1)
				return
