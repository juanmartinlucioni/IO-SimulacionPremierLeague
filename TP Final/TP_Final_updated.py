#%%
#Ideas
# 1 - Fichaje de Futbol para mejorar un club
# Problematica a enfrentar:
# nuestro equipo X de futbol tiene problemas en estas areas: 
# xG = Expected Goals
# xP = Expected Points
# Tenemos que buscando la informacion de posibles prospectos a fichar : 
# Utilizar una optimizacion para conseguir la mejor combinacion de opciones a la hora de mejorar tanto nuestos xG y xP 
# Pros: 
# Es facil de obtener los datos
# Pintaria entretenido

# CONSIGNA: 
# Nos contrato el Leicester City, salio 5 en la temporada 20-21, Quiere que analizemos los posibles fichajes de cara a la proxima temporada para asegurar una clasificacion a la Champions League el año proximo (terminar top 4). Con los datos de todos los jugadores de la premier league y con un presupuesto de 100 Millones de Libras, traer los refuerzos para lograrlo. Reconocer en que areas hay que mejorar y reforzar las mismas. 
#Leicester Team Stats

# IMPORTACION DE DATOS
#Datasets from: 
#https://fbref.com/en/comps/9/Premier-League-Stats
import pandas as pd
import numpy as np
#Import Data
league_stats = pd.read_csv('league-stats.csv')
team_stats_general = pd.read_csv('team-stats-general.csv')
team_stats_defense = pd.read_csv('team-stats-defense.csv')
team_stats_goalkeeping = pd.read_csv('team-stats-goalkeeping.csv')
player_stats_complete = pd.read_csv('player-stats-complete.csv')
player_stats_defense = pd.read_csv('player-stats-defense.csv')
player_stats_msc = pd.read_csv('player-stats-msc.csv')
player_stats_gk = pd.read_csv('player-stats-gk.csv') 

#Filter, Sort & Save Stats
#Filtramos columnas de interes
df = pd.DataFrame(league_stats, columns=['Squad', 'xG','xGA','xGD'])
#Sorteamos por una columna en especifico
sorted = df.sort_values(by='xG',axis=0,ascending=False,ignore_index=True)
print(sorted)
#Iteramos y guardamos la data relevante en un Array
TopTeams = []
for i in range(20):
    xGi = sorted.at[i,'xG']
    if  xGi > 55:
        TopTeams.append(sorted.loc[i])
print(TopTeams)


# %%
# TODO -Rank Teams by Skill


# %%
#Filtro jugadores por posicion
# TODO - Falta lograr meter mas de un filtro en el mismo
#Short List Delanteros(xG+xA)
#Agregar que filtre por POS ('FW')
df_players_attack = pd.DataFrame(player_stats_complete, columns=['Player', 'Pos', 'Squad', 'xG','xA'])
sortedByXG = df_players_attack.sort_values(by='xG', axis=0, ascending=False, ignore_index=True)
TopAttkPlayers = []
for i in range(531):
    xGi = sortedByXG.at[i, 'xG']
    xAi = sortedByXG.at[i, 'xA']
    Posi = sortedByXG.at[i, 'Pos']
    if xGi > 10 and xAi > 5 and Posi == 'FW':
        TopAttkPlayers.append(sortedByXG.loc[i])
print(TopAttkPlayers)

#%%
#Short List MedioCampistas(xA) + (T+I)
#Agregar que filtre por POS ('MF')
# Expected Assist
df_players_mid = pd.DataFrame(player_stats_complete, columns=['Player', 'Pos', 'Squad','xA', 'Tkl+Int'])
sortedByXA = df_players_mid.sort_values(by='xA', axis=0, ascending=False, ignore_index=True)
TopMidPlayers = []
for i in range(531):
    xAi = sortedByXA.at[i, 'xA']
    xTIi = sortedByTI.at[i, 'Tkl+Int']
    Posi = sortedByXG.at[i, 'Pos']
    if xAi > 5 + and xTIi > 100 and Posi = 'MF':
        TopMidPlayers.append(sortedByXA.loc[i])
print(TopMidPlayers)
# Tackles & Interceptions
# df_player_defense = pd.DataFrame(player_stats_defense, columns=['Player', 'Pos', 'Squad', , 'Blocks'])
# sortedByTI = df_player_defense.sort_values(by='Tkl+Int', axis=0, ascending=False, ignore_index=True)
# TopMidPlayersByTI = []
# for i in range(532):
#     xGi = sortedByTI.at[i, 'Tkl+Int']
#     if xGi > 100:
#         TopMidPlayersByTI.append(sortedByTI.loc[i])
# print(TopMidPlayersByTI)

#%%
#Short List Defensores (T) + (B) + (%AD)
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

#%%
# Aerial Success %
df_player_msc = pd.DataFrame(player_stats_msc, columns=['Player', 'Pos', 'Squad', '90s', 'Won%'])
sortedByAS = df_player_msc.sort_values(by='Won%', axis=0, ascending=False, ignore_index=True)
TopDefPlayersByAS = []
for i in range(532):
    Gsi = sortedByAS.at[i, '90s']
    ASi = sortedByAS.at[i, 'Won%']
    if Gsi > 20 and ASi > 70:
        TopDefPlayersByAS.append(sortedByAS.loc[i])
print(TopDefPlayersByAS)

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



# TODO -Problema Optimizacion


# %%
# TODO - Rank Teams by Skill (incluyendo los nuevos cambios)

# %%
# TODO - Simulacion Teams sin cambios

# %%
# TODO - Simulacion Teams con los cambios
