#%%
import picos
import numpy as np
from scipy import optimize
# CONVIENE ARMAR EL PREDIO VS NO INVERSION
# Creo el problema
P = picos.Problem()
# Variables de decision
#Invierto o no
y = picos.BinaryVariable('y',2)
#y1 = No invierten en el predio
#y2 = Invierten en el predio
ganancias = [0, 0]
# para los costos por ahora usamos costo[1] como una SUM de los costos variables y fijos en el periodo de 10 años
costo = [0, 1000]
#Simulaciones
#12 months * 10 years
nSim = 120
gananciasSinPredio = np.zeros(nSim)
gananciasConPredio = np.zeros(nSim)
for i in range(nSim):
    gananciasSinPredio[i] = np.random.normal(10, 1)
    gananciasConPredio[i] = np.random.normal(20, 4)
ganancias[0] = sum(gananciasSinPredio) 
ganancias[1] = sum(gananciasConPredio)
print(ganancias)
#Defino objetivo y función objetivo
P.set_objective('max', y[0]*(ganancias[0] - costo[0]) + y[1]*(ganancias[1] - costo[1]))
#Constraints
P.add_constraint(y[0]+ y[1] == 1)
#Verbosity
P.options.verbosity = 0
#Problema en consola
print(P)
#Resuelvo
P.solve(solver='glpk')
#Imprimo punto óptimo
print('y*=',y)
#Imprimo valor óptimo
print(P.value)

# %%
# Complejizacion 2.0
# EN QUE CONVIENE INVERTIR ? FLOTA NUEVA vs PREDIO 
# GANANCIAS Y COSTOS SIMULADOS EN MILLONES DE PESOS
# Creo el problema
P = picos.Problem()
# Variables de decision
#Invierto o no
y = picos.BinaryVariable('y', 2)
#y1 = No invierten en el predio
#y2 = Invierten en el predio
ganancias = [0, 0]
# costos[0] equivale a la compra de una flota de 40 camiones(200.000 usd * 135)
# costo[1] como una SUM de los costos variables y fijos en el periodo de 10 años + el costo de no renovar flota (800 millones en arrelgos)
costo = [1080, 1800]
#Simulaciones
#12 months * 10 years
nSim = 120
gananciasCambioFlota = np.zeros(nSim)
gananciasConPredio = np.zeros(nSim)
for i in range(nSim):
    gananciasCambioFlota[i] = np.random.normal(14, 1)
    gananciasConPredio[i] = np.random.normal(20, 5)
ganancias[0] = sum(gananciasCambioFlota)
ganancias[1] = sum(gananciasConPredio)
print(ganancias)
#Defino objetivo y función objetivo
P.set_objective('max', y[0]*(ganancias[0] - costo[0] ) + y[1]*(ganancias[1] - costo[1]))
#Constraints
P.add_constraint(y[0] + y[1] == 1)
#Verbosity
P.options.verbosity = 0
#Problema en consola
print(P)
#Resuelvo
P.solve(solver='glpk')
#Imprimo punto óptimo
print('y*=', y)
#Imprimo valor óptimo
print(P.value)


# %%
# Complejizacion 3.0
# Comparacion Marca de flota a comprar
# Escania vs Volvo vs Iveco
# variables a tener en cuenta: 
# rendimiento autonomia
# horas de transito antes del servicio
# rendimiento de cubiertas
# precio
# Simular 1000 viajes para terminar decidiendo que flota comprar.


# %%
# Complejizacion 4.0
# Bulk buy o Elegir cantidad de cada uno 
