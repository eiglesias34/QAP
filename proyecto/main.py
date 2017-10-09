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

    qap = LocalSearchQAP(number, distance, flow, optValue)
    qap2 = LocalSearchQAP(number, distance, flow, optValue)
    qap2.sol = qap.sol[:]
    qap2.solValue = qap.solValue
    qap3 = LocalSearchQAP(number, distance, flow, optValue)
    qap3.sol = qap.sol[:]
    qap3.solValue = qap.solValue
    print("INICIAL",qap.sol,qap.solValue)
    start_time = time.time()
    qap.localSearchBest(numIter)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("SOL",qap.sol,qap.solValue)
    print('\n')
    print("INICIAL",qap2.sol,qap2.solValue)
    start_time = time.time()
    qap2.localSearchFirst(numIter)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("SOL FIRST",qap2.sol,qap2.solValue)
    print('\n')
    print("INICIAL",qap3.sol,qap3.solValue)
    start_time = time.time()
    qap3.localSearchRandom(numIter)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("SOL RAANDOM",qap3.sol,qap3.solValue)
    print('\n')
    print("OPT",opt,optValue)
    print('\n') 

if __name__ == "__main__":
    main(sys.argv)