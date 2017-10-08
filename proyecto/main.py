#!/usr/bin/env pytho    
# -*- coding: utf-8 -*-
import sys
from LocalSearch import LocalSearchQAP
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

    qap = LocalSearchQAP(number, distance, flow, optValue)

    print("OPT",opt,optValue)

    if len(sys.argv) == 3:
        qap.greedy(int(argv[3]))
    else:
        qap.greedy(100)

    print("SOL",qap.sol,qap.solValue)

if __name__ == "__main__":
    main(sys.argv)