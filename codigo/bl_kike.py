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

def primer_mejor(sol, permutacion, distancias, flujo):
	for x in xrange(len(permutacion)):
		for y in xrange(x,len(permutacion)):
			vecino = permutacion[:] 
			vecino[y], vecino[x] = vecino[x], vecino[y]
			valor_vecino = valor_sol(vecino, distancias, flujo)
			if valor_vecino < sol:
				print valor_vecino
				print vecino
			 	return valor_vecino, vecino
	return sol, permutacion

def mejorvecinos(sol, permutacion, distancias, flujo):
	permutacion_op = permutacion[:]
	sol_op = sol
	for x in xrange(len(permutacion)):
		for y in xrange(x,len(permutacion)):
			vecino = permutacion[:] 
			vecino[y], vecino[x] = vecino[x], vecino[y]
			valor_vecino = valor_sol(vecino, distancias, flujo)
			if valor_vecino < sol_op:
				sol_op = valor_vecino
				permutacion_op = vecino[:]
				print valor_vecino
				print vecino
	return sol_op, permutacion_op

def busqueda_local(num_ubicaciones, sol_op, distancias, flujo):
	permutacion = generar_sol_ini(num_ubicaciones)
	sol = valor_sol(permutacion, distancias, flujo)
	print sol
	print permutacion
	for x in xrange(100):
		sol, permutacion = mejorvecinos(sol,permutacion, distancias, flujo)
		if sol == sol_op:
			break
	return sol, permutacion


if __name__ == '__main__':
	fsalida, sol_op = parseArgs(sys.argv)
	num_ubicaciones, distancias, flujo = lectura_de_matrices(fsalida)
	sol, permutacion = busqueda_local(num_ubicaciones, sol_op, distancias, flujo)
	print sol
	print permutacion