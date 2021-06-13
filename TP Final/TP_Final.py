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


#%%
#Filtro jugadores por posicion (OLD)
#Short List Delanteros(xG+xA)
df_players_attack = pd.DataFrame(player_stats_complete, columns=['Player', 'Pos', 'Squad', 'xG','xA', '90s'])
sortedByXG = df_players_attack.sort_values(by='xG', axis=0, ascending=False, ignore_index=True)
TopAttkPlayers = []
for i in range(532):
    Gsi = sortedByXG.at[i, '90s']
    xGi = sortedByXG.at[i, 'xG']
    xAi = sortedByXG.at[i, 'xA']
    Posi = sortedByXG.at[i, 'Pos']
    if Gsi > 20 and xGi > 10 and xAi > 5 and Posi == 'FW':
        TopAttkPlayers.append(sortedByXG.loc[i])
print(TopAttkPlayers)

#%%
#Short List MedioCampistas(xA) + (T+I)
# Expected Assist
df_players_mid = pd.DataFrame(player_stats_complete, columns=['Player', 'Pos', 'Squad', 'xA', '90s'])
sortedByXA = df_players_mid.sort_values(by='xA', axis=0, ascending=False, ignore_index=True)
TopMidPlayersByXA = []
for i in range(532):
    Gsi = sortedByXA.at[i, '90s']
    xAi = sortedByXA.at[i, 'xA']
    Posi = sortedByXA.at[i, 'Pos']
    if Gsi > 20 and xAi > 5 and Posi == 'MF':
        TopMidPlayersByXA.append(sortedByXA.loc[i])
print(TopMidPlayersByXA)

# Tackles & Interceptions
df_player_defense = pd.DataFrame(player_stats_defense, columns=['Player', 'Pos', 'Squad', 'Tkl+Int', 'Blocks', '90s'])
sortedByTI = df_player_defense.sort_values(by='Tkl+Int', axis=0, ascending=False, ignore_index=True)
TopMidPlayersByTI = []
for i in range(532):
    Gsi = sortedByTI.at[i, '90s']
    xTIi = sortedByTI.at[i, 'Tkl+Int']
    Posi = sortedByTI.at[i, 'Pos']
    if Gsi > 20 and xTIi > 100 and Posi == 'MF':
        TopMidPlayersByTI.append(sortedByTI.loc[i])
print(TopMidPlayersByTI)

#%%
#Short List Defensores (T) + (B)
#Agregar que filtre por POS ('DF')
# Tackles & Interceptions
df_player_defense = pd.DataFrame(player_stats_defense, columns=['Player', 'Pos', 'Squad', '90s', 'Tkl+Int', 'Blocks'])
sortedByTI = df_player_defense.sort_values(by='Tkl+Int', axis=0, ascending=False, ignore_index=True)
TopDefPlayers = []
for i in range(532):
    Gsi = sortedByTI.at[i, '90s']
    xGi = sortedByTI.at[i, 'Tkl+Int']
    Bi = sortedByTI.at[i, 'Blocks']
    if Gsi > 20 and xGi > 100 and Bi > 70:
        TopDefPlayers.append(sortedByTI.loc[i])
print(TopDefPlayers)

#Short List GoalKeepers(%S)
# TODO - Filtrar primero por minutos jugados mayor a 1000 que son mas de 10 partidos, sino las estadisticas procentuales fallan.
df_player_gk = pd.DataFrame(player_stats_gk, columns=['Player', 'Pos', 'Squad','90s', 'Save%'])
sortedBy90s = df_player_gk.sort_values(by='90s', axis=0, ascending=False, ignore_index=True)
TopGkPlayersBy90s = []
for i in range(42):
    Gsi = sortedBy90s.at[i, '90s']
    Si = sortedBy90s.at[i, 'Save%']
    if Gsi > 30 and Si>73:
        TopGkPlayersBy90s.append(sortedBy90s.loc[i])
print(TopGkPlayersBy90s)
