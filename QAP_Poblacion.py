# -*- coding: utf-8 -*-

class Solution(object):
    """docstring for Solution"""
    def __init__(self, initLen,distance,flow, initsol = None):
        if initsol:
            self.sol = initsol.sol[:]
            self.solValue = initsol.solValue
        else:
            self.getInitSol(initLen,distance,flow)

        
    def getInitSol(self,solLen,distance,flow):
        from random import shuffle
        l = [x for x in range(1,solLen+1)]
        shuffle(l)
        self.sol = l
        self.solValue = self.objectiveFunc(self.sol,solLen,distance,flow)


    def objectiveFunc(self,sol,solLen,distance,flow):
        value = 0
        for i in range(solLen):
            for j in range(solLen):
                value += flow[sol[i]-1][sol[j]-1]*distance[i][j]
        return value

class QAP_Poblacion(object):
    """docstring for QAP_Poblacion"""
    def __init__(self, number, distance, flow, optValue, populationSize=100, population = None):
        self.number = number
        self.distance = distance
        self.flow = flow
        self.optValue = optValue
        self.populationSize = populationSize

        if population:
            self.population = population
            self.bestindividual, self.bestvalue = self.getBestIndividual(population)
            self.populationSize = len(population)
        else:
            self.getInitPoblacion()

    def getInitPoblacion(self):
        population = []

        initsol = Solution(self.number,self.distance,self.flow)
        bestindividual = initsol.sol
        bestvalue = initsol.solValue
        population.append(initsol)

        for x in range(1,self.populationSize):
            initsol = Solution(self.number,self.distance,self.flow)
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

        for x in range(self.populationSize):
            if self.population[x].solValue < bestvalue:
                bestindividual = self.population[x].sol
                bestvalue = self.population[x].solValue

        return bestindividual, bestvalue

    def getWorstIndividual(self):
        worstindividual = self.population[0].sol
        worstvalue = self.population[0].solValue
        pos = 0

        for x in range(self.populationSize):
            if self.population[x].solValue > worstvalue:
                worstindividual = self.population[x].sol
                worstvalue = self.population[x].solValue
                pos = x

        return pos, worstindividual, worstvalue


    def setBestIndividual(self,newSol):
        if newSol.solValue < self.bestvalue:
            self.bestindividual = newSol.sol
            self.bestvalue = newSol.solValue
        