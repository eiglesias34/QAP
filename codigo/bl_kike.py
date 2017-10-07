import sys, traceback, random, time
from input_matrices import *

def generar_sol_ini(num):
	sol_ini = []
	for x in xrange(num):
		sol_ini.append(x)
	return sol_ini

def valor_sol(sol, distancias, flujo):
	valor = 0
	for x in xrange(len(sol)):
		for y in xrange(len(sol)):
			valor += distancias[x][y]*flujo[sol[x]][sol[y]]
	return valor

def mejorvecinos(sol, permutacion, distancias, flujo):
	for x in xrange(len(permutacion)):
		for y in xrange(len(permutacion)):
			vecino = permutacion[:] 
			vecino[y], vecino[x] = vecino[x], vecino[y]
			valor_vecino = valor_sol(vecino, distancias, flujo)
			if valor_vecino < sol:
				print valor_vecino
				print vecino
			 	return valor_vecino, vecino
	return sol, permutacion 

def busqueda_local(num_ubicaciones, sol_op, distancias, flujo):
	permutacion = generar_sol_ini(num_ubicaciones)
	sol = valor_sol(permutacion, distancias, flujo)
	print sol
	print permutacion
	for x in xrange(200):
		sol, permutacion = mejorvecinos(sol,permutacion, distancias, flujo)
		if sol == sol_op:
			break
	return sol, permutacion


if __name__ == '__main__':
	fsalida = parseArgs(sys.argv)
	num_ubicaciones, distancias, flujo = lectura_de_matrices(fsalida)
	sol, permutacion = busqueda_local(num_ubicaciones, 9552, distancias, flujo)
	print sol
	print permutacion