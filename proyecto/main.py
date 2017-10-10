#!/usr/bin/env pytho    
# -*- coding: utf-8 -*-
import sys
from LocalSearch import LocalSearchQAP
import time
'''
DATA: http://anjos.mgi.polymtl.ca/qaplib/inst.html
where n is the size of the instance, and A and B are either flow or distance matrix
'''

def readData(filename):
    data = []

    with open(filename, 'r') as data_file:
        number = int(data_file.readline().rstrip())
        for line in data_file:
            data_line = []
            l = line.rstrip()
            if l:
                for i in l.split():
                    data_line.append(int(i))
                data.append(data_line)

    if len(data) != number*2:
        rows = int((len(data)/2) / number) #numero de filas que componen una fila real

        distance,flow = [],[]
        for i in range(number):
            distance.append([item for sublist in data[:rows] for item in sublist])
            del data[:rows]

        for i in range(number):
            flow.append([item for sublist in data[:rows] for item in sublist])
            del data[:rows]

        return number, distance, flow

    return number, data[:number], data[number:]

def readSol(filename):
    data = []

    with open(filename, 'r') as data_file:
        first = data_file.readline().rstrip().split()

        data= []
        for line in data_file:
            l = line.rstrip()
            if l:
                for i in l.split():
                    data.append(int(i))

    return int(first[1]),data

##############################################
# MAIN
def main(argv):
    if len(sys.argv) < 3:
        print ("Usage: python main.py inputFile solFile [numIter]")
        sys.exit(1)
        
    number, distance, flow  = readData(argv[1])
    optValue, opt = readSol(argv[2])

    numIter = int(argv[3]) if len(sys.argv) > 2 else 500

    qap_best = []
    qap_first = []
    qap_random = []

    qap_best_time = []
    qap_first_time = []
    qap_random_time = []

    for x in range(5):
        qap = LocalSearchQAP(number, distance, flow, optValue)
        qap2 = LocalSearchQAP(number, distance, flow, optValue,qap.sol)
        qap3 = LocalSearchQAP(number, distance, flow, optValue,qap.sol)

        print("------------------------------------------")
        print("--> BEST - INICIAL",qap.sol,qap.solValue)
        start_time = time.time()
        qap.localSearchBest(numIter)
        end_time = time.time() - start_time
        qap_best_time.append(end_time)
        print("--- %s seconds ---" % end_time)
        print("SOL",qap.sol,qap.solValue)
        qap_best.append(qap.solValue)

        print("\n--> FIRST - INICIAL",qap2.sol,qap2.solValue)
        start_time = time.time()
        qap2.localSearchFirst(numIter)
        end_time = time.time() - start_time
        qap_first_time.append(end_time)
        print("--- %s seconds ---" % end_time)
        print("SOL",qap2.sol,qap2.solValue)
        qap_first.append(qap2.solValue)

        print("\n--> RANDOM - INICIAL",qap3.sol,qap3.solValue)
        start_time = time.time()
        qap3.localSearchRandom(numIter)
        end_time = time.time() - start_time
        qap_random_time.append(end_time)
        print("--- %s seconds ---" % end_time)
        print("SOL",qap3.sol,qap3.solValue)
        qap_random.append(qap3.solValue)
        print("------------------------------------------") 

    print("------------------------------------------")
    print("OPT",opt,optValue) 
    print("BEST ->",sum(qap_best)/len(qap_best),sum(qap_best_time)/len(qap_best_time),qap_best)
    print("FISRT ->",sum(qap_first)/len(qap_first),sum(qap_first_time)/len(qap_first_time),qap_first)
    print("RANDOM ->",sum(qap_random)/len(qap_random),sum(qap_random_time)/len(qap_random_time),qap_random)

if __name__ == "__main__":
    main(sys.argv)