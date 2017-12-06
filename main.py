#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#Autores: Andrea Centeno, Enrique Iglesias
#Fecha: sep-dic, 2017
import sys
import time
from ReadData import readData, readSol
from LocalSearch import LocalSearch
from AlgoritmoGenetico import GenecticAlgorithm
from AntColony import AntColony

'''
DATA: http://anjos.mgi.polymtl.ca/qaplib/inst.html
where n is the size of the instance, and A and B are either flow or distance matrix
'''

def error(opt,sol):
    '''
    Error porcentual

    Parámetros:
    opt -- solucion optima
    sol -- solucion aproximada
    ''' 
    return abs(sol-opt)/opt * 100

def runGA(number, distance, flow, optValue, numIter):
    '''
    Crea clase QAP y ejecuta el algoritmo genetico

    Parámetros:
    number -- cardinalidad del problema
    distance -- matriz de distancia
    flow -- matriz de flujo
    optValue -- valor optimo
    numIter -- numero maximo de iteraciones
    '''   
    qap = GenecticAlgorithm(number, distance, flow, optValue)

    #temperature
    start_time = time.time()
    qap.genetic(numIter)
    end_time = time.time() - start_time

    print("GA",qap.optValue,qap.bestvalue,error(qap.optValue,qap.bestvalue),'%',end_time,'s')
    return end_time,qap.bestvalue

def runAC(number, distance, flow, optValue, numIter):
    '''
    Crea clase QAP y ejecuta la colonia de hormigas

    Parámetros:
    number -- cardinalidad del problema
    distance -- matriz de distancia
    flow -- matriz de flujo
    optValue -- valor optimo
    numIter -- numero maximo de iteraciones
    '''   
    qap = AntColony(number, distance, flow, optValue, 10)
    start_time = time.time()
    qap.colony(numIter)
    end_time = time.time() - start_time

    print("AC",qap.optValue,qap.bestvalue,error(qap.optValue,qap.bestvalue),'%',end_time,'s')
    return end_time,qap.bestvalue

def run(number, distance, flow, optValue,numIter, opt, method):
    '''
    Realiza de 5 a 10 corridas por instancias y promedia resultados

    Parámetros:
    number -- cardinalidad del problema
    distance -- matriz de distancia
    flow -- matriz de flujo
    optValue -- valor optimo
    numIter -- numero maximo de iteraciones
    opt -- solucion optima
    method -- metodo (runGA o runAC)
    '''
    qap_first = []
    qap_first_time = []

    iters = 10 if number < 60 else 5
    for x in range(iters):
        end_time,solValue = method(number, distance, flow, optValue,numIter)
        qap_first_time.append(end_time)
        qap_first.append(solValue)

    solAvg = sum(qap_first)/len(qap_first)
    timeAvg =  sum(qap_first_time)/len(qap_first_time)
    print("------------------------------------------")
    print("OPT",opt,optValue) 
    print("SOL",solAvg,error(optValue,solAvg),'%',timeAvg,'s',qap_first)

##############################################
# MAIN
##############################################
def main(argv):
    if len(sys.argv) < 3:
        print ("Usage: python main.py inputFile solFile [numIter]")
        sys.exit(1)

    #leemos datos del los archivo de entrada
    number, distance, flow  = readData(argv[1])
    optValue, opt = readSol(argv[2])
    numIter = int(argv[3]) if len(sys.argv) > 3 else 1000

    # Now ask for input
    print("Seleccione entre:")
    print("1 - GA\n2 - AC")
    user_input = input()

    if int(user_input) == 1:
        runGA(number, distance, flow, optValue, numIter)
    elif int(user_input) == 2:
        runAC(number, distance, flow, optValue, numIter)           

if __name__ == "__main__":
    main(sys.argv)