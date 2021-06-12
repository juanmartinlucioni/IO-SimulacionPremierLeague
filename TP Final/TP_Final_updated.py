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
import math
#Import Data
league_stats = pd.read_csv('league-stats.csv')
team_stats_general = pd.read_csv('team-stats-general.csv')
team_stats_defense = pd.read_csv('team-stats-defense.csv')
team_stats_goalkeeping = pd.read_csv('team-stats-goalkeeping.csv')
player_stats_complete = pd.read_csv('player-stats-complete.csv')
player_stats_defense = pd.read_csv('player-stats-defense.csv')
player_stats_msc = pd.read_csv('player-stats-msc.csv')
player_stats_gk = pd.read_csv('player-stats-gk.csv') 
team_stats_skills = pd.read_csv('league-stats-skill.csv') 

# %%
# TODO -Rank Teams by Skill
df_teams = pd.DataFrame(team_stats_skills, columns=['Rk', 'Squad', 'xG','xGA','Save%','SoT','Tkl','Blocks','Cmp%','KP'])
Skill = []
bestXG = df_teams['xG'].max()
bestXGA = df_teams['xGA'].min()
bestSP = df_teams['Save%'].max()
bestSoT = df_teams['SoT'].max()
bestT = df_teams['Tkl'].max()
bestB = df_teams['Blocks'].max() 
bestCP = df_teams['Cmp%'].max()
bestKP = df_teams['KP'].max()

for i in range(20):
    #atacking stats
    xGp = ((df_teams.at[i,'xG']/ bestXG)*25)
    Sotp = ((df_teams.at[i, 'SoT'] / bestSoT)*25)
    KPp = ((df_teams.at[i, 'KP'] / bestKP)*25)
    CPp = ((df_teams.at[i, 'Cmp%'] / bestCP)*25)
    #defensive stats
    xGAp = ((bestXGA / df_teams.at[i, 'xGA'])*25)
    Tp = ((df_teams.at[i, 'Tkl'] / bestT)*25)
    Bp = ((df_teams.at[i, 'Blocks'] / bestB)*25)
    SPp = ((df_teams.at[i, 'Save%'] / bestSP)*25)
    #Overall Stats
    atk = xGp + Sotp + KPp + CPp
    dfc = xGAp + Tp + Bp + SPp
    pos = 1
    xG = df_teams.at[i, 'xG']
    Sp = df_teams.at[i, 'Save%']/2
    teambyskill = [df_teams.at[i,'Squad'],df_teams.at[i,'Rk'], atk.round(), dfc.round(), pos, xG/38,Sp]
    Skill.append(teambyskill)
#TODO NOTAS
    # xG y S% mandarlo a un array que sea teamstats asi no se mezcla con skill
print(Skill)
#%% Sim League with out changes

# Teams
ManchesterCity = [Skill[0], [0,0,0,0,0,0]]
ManchesterUtd = [Skill[1], [0,0,0,0,0,0]]
Liverpool = [Skill[2], [0,0,0,0,0,0]]
Chelsea = [Skill[3], [0,0,0,0,0,0]]
LeicesterCity = [Skill[4], [0,0,0,0,0,0]]
WestHam = [Skill[5], [0,0,0,0,0,0]]
Tottenham = [Skill[6], [0,0,0,0,0,0]]
Arsenal = [Skill[7], [0,0,0,0,0,0]]
LeedsUnited = [Skill[8], [0,0,0,0,0,0]]
Everton = [Skill[9], [0,0,0,0,0,0]]
AstonVilla = [Skill[10], [0,0,0,0,0,0]]
NewcastleUtd = [Skill[11], [0,0,0,0,0,0]]
Wolves = [Skill[12], [0,0,0,0,0,0]]
CrystalPalace = [Skill[13], [0,0,0,0,0,0]]
Southampton = [Skill[14], [0,0,0,0,0,0]]
Brighton = [Skill[15], [0,0,0,0,0,0]]
Burnley = [Skill[16], [0,0,0,0,0,0]]
Fulham = [Skill[17], [0,0,0,0,0,0]]
WestBrom = [Skill[18], [0,0,0,0,0,0]]
SheffieldUtd = [Skill[19], [0,0,0,0,0,0]]

Teams = [ManchesterCity, ManchesterUtd, Liverpool, Chelsea, LeicesterCity, WestHam, Tottenham, Arsenal, LeedsUnited, Everton, AstonVilla, NewcastleUtd, Wolves, CrystalPalace, Southampton, Brighton, Burnley, Fulham, WestBrom, SheffieldUtd]

def homeGoals(ht, at):
    if ht[0] != at[0]:
        bonusRank = (-1 * (ht[1]-at[1]))/100
        bonusAtk = (-1 * (ht[2] - at[3]))/100
        goals = 0

        # Better ATK
        if ht[2] > at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusAtk)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Equal ATK
        if ht[2] == at[2]:
            xGToTest = ht[5]
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Worse ATK
        if ht[2] < at[2]:
            xGToTest = ht[5] * (1+bonusRank-bonusAtk)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1
        return goals
    else:
        return 'Same Team'
        
def awayGoals(ht, at):
    if ht[0] != at[0]:
        bonusRank = (-1 * (at[1]-ht[1]))/100 #TODO chequear
        bonusAtk = (-1 * (at[2] - ht[3]))/100
        goals = 0

        # Better ATK
        if at[2] > ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusAtk)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Equal ATK
        if at[2] == ht[2]:
            xGToTest = at[5]
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Worse ATK
        if at[2] < ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusAtk)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1
        return goals
    else:
        return 'Same Team'
#League Stats
Points =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Wins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Loses = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Draws = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
GF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
GA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(20):
    print("========================================")
    print(Teams[x][0][0] + "'s Home Games: ")
    print("========================================")
    for y in range(20):
        if Teams[x][0] == Teams[y][0]:
            pass
        else:
            homeScore = homeGoals(Teams[x][0], Teams[y][0])
            awayScore = awayGoals(Teams[x][0], Teams[y][0])
            print(Teams[x][0][0], homeScore, ":", awayScore, Teams[y][0][0])
            if homeScore > awayScore:
              Wins[x] += 1
              Loses[y] += 1
              Points[x] += 3
              GF[x] += homeScore
              GA[x] += awayScore
              GF[y] += awayScore
              GA[y] += homeScore
            elif homeScore < awayScore:
              Wins[y] += 1
              Loses[x] += 1
              Points[y] += 3
              GF[x] += homeScore
              GA[x] += awayScore
              GF[y] += awayScore
              GA[y] += homeScore
            elif homeScore == awayScore:
              Draws[x] += 1
              Draws[y] += 1
              Points[x] += 1
              Points[y] += 1
              GF[x] += homeScore
              GA[x] += awayScore
              GF[y] += awayScore
              GA[y] += homeScore
            
            Teams[x][1][0]= Points[x]
            Teams[x][1][1]= Wins[x]
            Teams[x][1][2]= Draws[x]
            Teams[x][1][3]= Loses[x]
            Teams[x][1][4]= GF[x]
            Teams[x][1][5]= GA[x]

            Teams[y][1][0]= Points[y]
            Teams[y][1][1]= Wins[y]
            Teams[y][1][2]= Draws[y]
            Teams[y][1][3]= Loses[y]
            Teams[y][1][4]= GF[y]
            Teams[y][1][5]= GA[y]


#League Table
sortedTeams = sorted(Teams, key=lambda x: x[1][0], reverse=True)
print("| TEAM                      | POINTS | WINS | DRAWS | LOSSES | GOALS FOR | GOALS AGAINST |")
for x in range(20):
    print('|', sortedTeams[x][0][0]," "*(24 - len(sortedTeams[x][0][0])),'|  ', sortedTeams[x][1][0]," "*(3 - len(str(sortedTeams[x][1][0]))),'| ', sortedTeams[x][1][1]," "*(2 - len(str(sortedTeams[x][1][1]))),'|  ', sortedTeams[x][1][2]," "*(2 - len(str(sortedTeams[x][1][2]))),'|  ', sortedTeams[x][1][3]," "*(3 - len(str(sortedTeams[x][1][3]))),'|    ', sortedTeams[x][1][4]," "*(4 - len(str(sortedTeams[x][1][4]))),"|     ", sortedTeams[x][1][5]," "*(7 - len(str(sortedTeams[x][1][5]))),"|")
   




# %%
#Filtro jugadores por posicion
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
# TODO - Simulacion Teams con los cambios
