#!/usr/bin/env pytho    
# -*- coding: utf-8 -*-
import sys
from ReadData import readData, readSol
from LocalSearch import LocalSearch
from SimulatedAnnealing import SimulatedAnnealing
from Tabu import Tabu
import time
'''
DATA: http://anjos.mgi.polymtl.ca/qaplib/inst.html
where n is the size of the instance, and A and B are either flow or distance matrix
'''

def runLS(argv):
    '''
    argv
        1 - inputFile 
        2 - solFile
        3 - numero de iteraciones de LS (default 500)
        4 - numero de corridas por instancia (default 5)
    '''
    number, distance, flow  = readData(argv[1])
    optValue, opt = readSol(argv[2])

    numIter = int(argv[3]) if len(sys.argv) > 3 else 500

    qap_first = []
    qap_random = []

    qap_best_time = []
    qap_first_time = []
    qap_random_time = [] 

    num = int(argv[4]) if len(sys.argv) > 4 else 10
    for x in range(num):
        qap = LocalSearch(number, distance, flow, optValue)
        qap2 = LocalSearch(number, distance, flow, optValue,qap.sol)
        qap3 = LocalSearch(number, distance, flow, optValue,qap.sol)

        #print("\n--> FIRST - INICIAL",qap2.sol,qap2.solValue)
        start_time = time.time()
        qap2.localSearchFirst(numIter)
        end_time = time.time() - start_time
        qap_first_time.append(end_time)
        qap_first.append(qap2.solValue)
        #print("--- %s seconds ---" % end_time)
        #print("SOL",qap2.sol,qap2.solValue)

        #print("\n--> RANDOM - INICIAL",qap3.sol,qap3.solValue)
        start_time = time.time()
        qap3.localSearchRandom(numIter)
        end_time = time.time() - start_time
        qap_random_time.append(end_time)
        qap_random.append(qap3.solValue)
        #print("--- %s seconds ---" % end_time)
        #print("SOL",qap3.sol,qap3.solValue)
        #print("------------------------------------------") 


    #print("------------------------------------------")
    #print("--> BEST - INICIAL",qap.sol,qap.solValue)
    start_time = time.time()
    qap.localSearchBest(numIter)
    end_time = time.time() - start_time
    #print("--- %s seconds ---" % end_time)
    #print("SOL",qap.sol,qap.solValue)

    print("------------------------------------------")
    print("OPT",opt,optValue) 
    print("FISRT ->",sum(qap_first)/len(qap_first),sum(qap_first_time)/len(qap_first_time),qap_first)
    print("RANDOM ->",sum(qap_random)/len(qap_random),sum(qap_random_time)/len(qap_random_time),qap_random)
    print("BEST ->",qap.solValue, end_time)

def runSA(argv):
    '''
    argv
        1 - inputFile 
        2 - solFile
        3 - numero de iteraciones de LS (default 500)
        4 - numero de iteraciones sin mejorar
    '''
    number, distance, flow  = readData(argv[1])
    optValue, opt = readSol(argv[2])

    numIter = int(argv[3]) if len(sys.argv) > 3 else 500
    numAccept = int(argv[4]) if len(sys.argv) > 4 else 5

    qap = SimulatedAnnealing(number, distance, flow, optValue)

    #temperature
    start_time = time.time()
    qap.annealing(numIter, numAccept)
    end_time = time.time() - start_time

    print("------------------------------------------")
    print("OPT",opt,optValue) 
    print("SA ",qap.solValue,abs(qap.solValue-qap.optValue)/qap.optValue, end_time)


def runTS(argv):
    '''
    argv
        1 - inputFile 
        2 - solFile
        3 - numero de iteraciones de LS (default 500)
    '''
    number, distance, flow  = readData(argv[1])
    optValue, opt = readSol(argv[2])

    numIter = int(argv[3]) if len(sys.argv) > 3 else 500

    qap = Tabu(number, distance, flow, optValue)

    #temperature
    start_time = time.time()
    qap.tabu(numIter)
    end_time = time.time() - start_time

    print("------------------------------------------")
    print("OPT",opt,optValue) 
    print("SA ",qap.solValue,abs(qap.solValue-qap.optValue)/qap.optValue, end_time)

##############################################
# MAIN
def main(argv):
    if len(sys.argv) < 3:
        print ("Usage: python main.py inputFile solFile [numIter]")
        sys.exit(1)

    # Now ask for input
    print("Seleccione entre:")
    print("1 - LS\n2 - SA\n3 - TS")
    user_input = input()

    if user_input == '1':
        runLS(argv)
    elif user_input == '2':
        runSA(argv)
    elif user_input == '3':
        runTS(argv)
           

if __name__ == "__main__":
    main(sys.argv)