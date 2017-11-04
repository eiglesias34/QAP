class QAP(object):
    
    def __init__(self, number, distance, flow, optValue, initSol = None):
        self.number = number
        self.distance = distance
        self.flow = flow
        self.optValue = optValue

        if initSol:
            self.sol = initSol
            self.solValue = self.objectiveFunc(initSol)
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