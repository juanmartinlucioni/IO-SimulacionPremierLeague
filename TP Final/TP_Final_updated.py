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
df_teams = pd.DataFrame(team_stats_general, columns=['Squad', 'xG','xGA','Save%','SoTA','Tkl','Blocks','Cmp%','Kp'])
Skill = []
bestXG = df_teams.at[]
for i in range(20):
    #atacking stats
    xGp = ((df_teams.at[i,'xG']/ bestXG)*100)*25
    Sotp = ((df_teams.at[i, 'SoTA'] / bestSot)*100)*25
    KPp = ((df_teams.at[i, 'Kp'] / bestKP)*100)*25
    CPp = ((df_teams.at[i, 'Cmp%'] / bestCP)*100)*25
    #defensive stats
    xGAp = ((df_teams.at[i, 'xGA'] / bestXGA)*100)*25
    Tp = ((df_teams.at[i, 'Tkl'] / bestT)*100)*25
    Bp = ((df_teams.at[i, 'Blocks'] / bestB)*100)*25
    SPp = ((df_teams.at[i, 'Save%'] / bestSP)*100)*25
    #Overall Stats
    atk = xGp + Sotp + KPp + CPp,
    dfc = xGAp + Tp + Bp + SPp
    teambyskill = [df_teams.at[i,'rank'], atk, dfc]
    Skill.append(teambykill)
print(Skill)

# %%
#Filtro jugadores por posicion
#Short List Delanteros(xG+xA)
df_players_attack = pd.DataFrame(player_stats_complete, columns=['Player', 'Pos', 'Squad', 'xG','xA', '90s'])
sortedByXG = df_players_attack.sort_values(by='xG', axis=0, ascending=False, ignore_index=True)
TopAttkPlayers = []
for i in range(532):
    Gsi = sortedByTI.at[i, '90s']
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
    Gsi = sortedByTI.at[i, '90s']
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
