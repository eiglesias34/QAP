class QAP_Poblacion(object):
	"""docstring for QAP_Poblacion"""
	def __init__(self, number, distance, flow, optValue, populationSol = None):
		self.number = number
        self.distance = distance
        self.flow = flow
        self.optValue = optValue

        if poblacionSol:
        	self.poblacion = populationSol
        	self.bestindividual, self.bestvalue = self.getBestIndividual(populationSol)
        else:
        	self.getInitPoblacion()

    class Solution(object):
    	"""docstring for Solution"""
    	def __init__(self, initsol = None):
    		if initsol:
    			self.sol = initsol
    			self.solValue = self.objectiveFunc(initsol)
    		else:
    			self.getInitSol()

    		
    	def getInitSol(self):
	        from random import shuffle
	        l = [x for x in range(1,self.number+1)]
	        shuffle(l)
	        self.sol = l
	        self.solValue = self.objectiveFunc(self.sol)


	    def objectiveFunc(self,sol):
	        value = 0
	        for i in range(self.number):
	            for j in range(self.number):
	                value += self.flow[sol[i]-1][sol[j]-1]*self.distance[i][j]
	        return value

	def getInitPoblacion(self):
		population = []

		initsol = Solution()
		bestindividual = initsol.sol
		bestvalue = initsol.solValue
		population.append(initsol)

		for x in xrange(1,100):
			initsol = Solution()
			population.append(initsol)
			if initsol.solValue < bestvalue:
				bestindividual = initsol.sol
				bestvalue = initsol.solValue

		self.population = population
		self.bestindividual = bestindividual
		self.bestvalue = bestvalue
	    		

    def getBestIndividual(self):
    	bestindividual = self.population[0].sol
    	bestvalue = self.population[0].solValue

    	for x in xrange(1,100):
    		if self.population[x].solValue < bestvalue:
    			bestindividual = self.population[x].sol
				bestvalue = self.population[x].solValue

		return bestindividual, bestvalue

	def getWorstIndividual(self):
    	worstindividual = self.population[0].sol
    	worstvalue = self.population[0].solValue
    	pos = 0

    	for x in xrange(1,100):
    		if self.population[x].solValue > worstvalue:
    			worstindividual = self.population[x].sol
				worstvalue = self.population[x].solValue
				pos = x

		return pos, worstindividual, worstvalue


		