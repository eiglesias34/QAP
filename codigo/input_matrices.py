import sys, traceback, random, time
from math import *

def parseArgs(args):
    msg = "Error en la linea de comando:\arbolbinario  <nombre de archivo> <nombre del nuevo archivo>"
    if len(args) != 3:
        print(msg)
        sys.exit(1)
    return args[1], int(args[2])

def lectura_de_matrices(fent):
	myfile = open(fent, "r")
	num_ubicaciones = int(next(myfile))
	distancia = [[0 for x in range(num_ubicaciones)] for y in range(num_ubicaciones)] 
	flujo = [[0 for x in range(num_ubicaciones)] for y in range(num_ubicaciones)] 
	next(myfile)

	x = 0 
	for line in myfile:
		line = line.strip('\n')
		elementos = line.split(' ')
		for y in xrange(num_ubicaciones):
			distancia[x][y] = int(elementos[y])
		x+=1
		if x == num_ubicaciones:
			break
			
	next(myfile)
	x = 0 
	for line in myfile:
		line = line.strip('\n')
		elementos = line.split(' ')
		for y in xrange(num_ubicaciones):
			flujo[x][y] = int(elementos[y])
		x+=1
		if x == num_ubicaciones:
			break

	return num_ubicaciones, distancia, flujo


