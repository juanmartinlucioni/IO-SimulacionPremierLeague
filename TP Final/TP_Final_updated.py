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
team_stats_skills = pd.read_csv('league-stats-skill.csv')
lc_stats_skills = pd.read_csv('LC_player_stats.csv')
bundes_player_stats = pd.read_csv('bundesliga-players-stats.csv')
# laliga_player_stats = pd.read_csv ()


# %%
# TODO -Rank Teams by Skill
df_teams = pd.DataFrame(team_stats_skills, columns=['Rk', 'Squad', 'xG','xGA','Save%','SoT','Tkl','Blocks','Cmp%','KP','Poss'])
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
    pos = df_teams.at[i, 'Poss']
    xG = df_teams.at[i, 'xG']
    Sp = df_teams.at[i, 'Save%']/3
    teambyskill = [df_teams.at[i,'Squad'],df_teams.at[i,'Rk'], atk.round(), dfc.round(), pos, xG/38,Sp]
    Skill.append(teambyskill)
#TODO NOTAS
    # xG y S% mandarlo a un array que sea teamstats asi no se mezcla con skill
#%% Sim League with out changes

# Teams
ManchesterCity = [Skill[0], [0,0,0,0,0,0,0]]
ManchesterUtd = [Skill[1], [0,0,0,0,0,0,0]]
Liverpool = [Skill[2], [0,0,0,0,0,0,0]]
Chelsea = [Skill[3], [0,0,0,0,0,0,0]]
LeicesterCity = [Skill[4], [0,0,0,0,0,0,0]]
WestHam = [Skill[5], [0,0,0,0,0,0,0]]
Tottenham = [Skill[6], [0,0,0,0,0,0,0]]
Arsenal = [Skill[7], [0,0,0,0,0,0,0]]
LeedsUnited = [Skill[8], [0,0,0,0,0,0,0]]
Everton = [Skill[9], [0,0,0,0,0,0,0]]
AstonVilla = [Skill[10], [0,0,0,0,0,0,0]]
NewcastleUtd = [Skill[11], [0,0,0,0,0,0,0]]
Wolves = [Skill[12], [0,0,0,0,0,0,0]]
CrystalPalace = [Skill[13], [0,0,0,0,0,0,0]]
Southampton = [Skill[14], [0,0,0,0,0,0,0]]
Brighton = [Skill[15], [0,0,0,0,0,0,0,0]]
Burnley = [Skill[16], [0,0,0,0,0,0,0,0]]
Fulham = [Skill[17], [0,0,0,0,0,0,0]]
WestBrom = [Skill[18], [0,0,0,0,0,0,0]]
SheffieldUtd = [Skill[19], [0,0,0,0,0,0,0]]

Teams = [ManchesterCity, ManchesterUtd, Liverpool, Chelsea, LeicesterCity, WestHam, Tottenham, Arsenal, LeedsUnited, Everton, AstonVilla, NewcastleUtd, Wolves, CrystalPalace, Southampton, Brighton, Burnley, Fulham, WestBrom, SheffieldUtd]

def homeGoals(ht, at):
    if ht[0] != at[0]:
        bonusRank = (-1 * (ht[1] - at[1]))/100
        bonusAtk = (ht[2] - at[3])/100
        bonusPossTemp= (ht[4] - at[4])/100
        if bonusPossTemp < 0.1:
            bonusPoss = 0.1
        else:
            bonusPoss = bonusPossTemp
        goals = 0


        # Better ATK
        if ht[2] > at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusAtk+bonusPoss)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Equal ATK
        if ht[2] == at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusPoss)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Worse ATK
        if ht[2] < at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusAtk+bonusPoss)
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
        bonusRank = (-1 * (at[1]-ht[1]))/100
        bonusAtk = (at[2] - ht[3])/100
        bonusPoss= (at[4] - ht[4])/100
        goals = 0

        # Better ATK
        if at[2] > ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusAtk+bonusPoss)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Equal ATK
        if at[2] == ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusPoss)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Worse ATK
        if at[2] < ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusAtk+bonusPoss)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1
        return goals
    else:
        return 'Same Team'


def runLeague(dataSet):
    #League Stats
    Points =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Wins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Loses = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Draws = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    GF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    GA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range(20):
        # print("========================================")
        # print(dataSet[x][0][0] + "'s Home Games: ")
        # print("========================================")
        for y in range(20):
            if dataSet[x][0] == dataSet[y][0]:
                pass
            else:
                homeScore = homeGoals(dataSet[x][0], dataSet[y][0])
                awayScore = awayGoals(dataSet[x][0], dataSet[y][0])
                # print(dataSet[x][0][0], homeScore, ":", awayScore, dataSet[y][0][0])
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
                
                dataSet[x][1][0]= Points[x]
                dataSet[x][1][1]= Wins[x]
                dataSet[x][1][2]= Draws[x]
                dataSet[x][1][3]= Loses[x]
                dataSet[x][1][4]= GF[x]
                dataSet[x][1][5]= GA[x]

                dataSet[y][1][0]= Points[y]
                dataSet[y][1][1]= Wins[y]
                dataSet[y][1][2]= Draws[y]
                dataSet[y][1][3]= Loses[y]
                dataSet[y][1][4]= GF[y]
                dataSet[y][1][5]= GA[y]


    #League Table
    sortedTeams = sorted(dataSet, key=lambda x: x[1][0], reverse=True)
    # print("| TEAM                      | POINTS | WINS | DRAWS | LOSSES | GOALS FOR | GOALS AGAINST | RANK |")
    for x in range(20):
        sortedTeams[x][1][6]= x+1
        # print('|', sortedTeams[x][0][0]," "*(24 - len(sortedTeams[x][0][0])),'|  ', sortedTeams[x][1][0]," "*(3 - len(str(sortedTeams[x][1][0]))),'| ', sortedTeams[x][1][1]," "*(2 - len(str(sortedTeams[x][1][1]))),'|  ', sortedTeams[x][1][2]," "*(2 - len(str(sortedTeams[x][1][2]))),'|  ', sortedTeams[x][1][3]," "*(3 - len(str(sortedTeams[x][1][3]))),'|    ', sortedTeams[x][1][4]," "*(4 - len(str(sortedTeams[x][1][4]))),"|     ", sortedTeams[x][1][5]," "*(7 - len(str(sortedTeams[x][1][5]))),"| ",x+1," "*(3 - len(str(sortedTeams[x][1][0]))),"|")


    for z in range(20):
        if sortedTeams[z][0][0] == 'Leicester City':
            LCPosRun = sortedTeams[z][1][6]

    LCPos[i] = LCPosRun


nSim = 100
LCPos = np.zeros(nSim)

for i in range(nSim):
    runLeague(Teams)
print('Probabilidad de que Leicester City termine en el Top 4: ',np.sum(LCPos < 5)/nSim)
#Con 10.000 runs nos dio una Prob de 0.2584

#%%
#Datos del Leicester City 20-21
LC_name = df_teams.at[4, 'Squad']
LC_xG= df_teams.at[4, 'xG'] 
LC_Sot = df_teams.at[4, 'SoT'] 
LC_KP = df_teams.at[4, 'KP'] 
LC_CP = df_teams.at[4, 'Cmp%']
#defensive stats
LC_xGA = df_teams.at[4, 'xGA']
LC_T = df_teams.at[4, 'Tkl']
LC_B = df_teams.at[4, 'Blocks']
LC_SP = df_teams.at[4, 'Save%']
LC_Stats = [LC_name, LC_xG, LC_Sot, LC_KP, LC_CP, LC_xGA, LC_T, LC_B, LC_SP]
print(LC_Stats)

# TODO - Afectar los datos y ver como modifica el correr la liga y las chances del leicester 
# xGA cambia segun como cambian los otros datos de def (mejoran 10%, xGA tiene que caer 10%)
# EJEMPLO - New Data
# Current DEF
LC_Def_xGA = ((bestXGA / LC_xGA)*25)
LC_Def_T = ((LC_T / bestT)*25)
LC_Def_B = ((LC_B / bestB)*25)
LC_Def_SP = ((LC_SP / bestSP)*25)

LC_Def = LC_Def_xGA + LC_Def_T + LC_Def_B + LC_Def_SP
print('Current Defense Stat =', LC_Def,
'Skill calculada arriba =', Teams[4][0][3])

#New DEF Stats
Comparison_Def_Base = LC_Def_T + LC_Def_B + LC_Def_SP

#Esto en realidad se determinaria comparando LC_T vs LC_T_New ((LC_T_New/LC_T)-1)
LC_Def_T2 = LC_Def_T*1.05
LC_Def_B2 = LC_Def_B*1.07
LC_Def_SP2 = LC_Def_SP*1.1

New_Def_Base = LC_Def_T2 + LC_Def_B2 + LC_Def_SP2

Def_Mejora = (New_Def_Base/Comparison_Def_Base)-1

LC_xGA2 = LC_xGA*(1-Def_Mejora)
LC_Def_xGA2 = ((bestXGA / LC_xGA2)*25)

New_LC_Def = LC_Def_xGA2 + LC_Def_T2 + LC_Def_B2 + LC_Def_SP2
print('Current Defense Stat =', LC_Def,
    'New Defense Stat =', New_LC_Def)
Teams[4][0][3] = New_LC_Def

#Corremos un test run de la liga con nuevos datos
# for i in range(nSim):
#     runLeague(Teams)
# print('Probabilidad de que Leicester City termine en el Top 4: ',np.sum(LCPos < 5)/nSim)

# Volver Def al valor original
Teams[4][0][3] = LC_Def
#%% 
# TODO - Players y comformacion del equipo
# Necesito a xG quienes lo componen
# xG Compuesto por MFA + FW es 42.2 de 56.0 
# Tenes que parar 3 ( Vardy [19.7] + Barnes [6.2] + Ihenacho [7.8] ) xG=[33.4] de 42.2
# Tenemos un problemas Barnes hace 6.2 xG mientras que Madison hace 4.4, pero en xG+xA Madison hace 9.7 mientras que barnes se queda en 7.3
# LC_player_stats.csv

# FW = xG + SOT  // x
# MFFW = xG + SOT + KP + CMP% // y
# MF = TK + KP + CMP% // z
# DF = TK + BLK + CMP% // w
# GK = %S  // u

# df_LC_players = pd.DataFrame(lc_stats_skills, columns=['Player', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Tkl', 'Blocks', 'Save%', 'Price'])

# FW Players
df_LC_FW_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'xG', 'SoT', 'Price'])
LCFWPlayers = []
for i in range(27):
    Posi = df_LC_FW_players.at[i, 'Pos']
    if Posi == 'FW':
        LCFWPlayers.append(df_LC_FW_players.loc[i])
print(LCFWPlayers)

# MFFW 
df_LC_MFFW_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
LCMFFWPlayers = []
for i in range(27):
    Posi = df_LC_MFFW_players.at[i, 'Pos']
    if Posi == 'MFFW':
        LCMFFWPlayers.append(df_LC_MFFW_players.loc[i])
print(LCMFFWPlayers)

# MF
df_LC_MF_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
LCMFPlayers = []
for i in range(27):
    Posi = df_LC_MF_players.at[i, 'Pos']
    if Posi == 'MF':
        LCMFPlayers.append(df_LC_MF_players.loc[i])
print(LCMFPlayers)

# DF
df_LC_DF_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
LCDFPlayers = []
for i in range(27):
    Posi = df_LC_DF_players.at[i, 'Pos']
    if Posi == 'DF':
        LCDFPlayers.append(df_LC_DF_players.loc[i])
print(LCDFPlayers)

# GK
df_LC_GK_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'Save%', 'Price'])
LCGKPlayers = []
for i in range(27):
    Posi = df_LC_GK_players.at[i, 'Pos']
    if Posi == 'GK':
        LCGKPlayers.append(df_LC_GK_players.loc[i])
print(LCGKPlayers)

#%%
# Top Players Bundesliga
FWPlayers = []
MFFWPlayers = []
MFPlayers = []
DFPlayers = []
GKPlayers = []

# FW
league_players_stats = bundes_player_stats
df_FW_players = pd.DataFrame(league_players_stats, columns=['Player','90s', 'Pos', 'xG', 'SoT', 'Price'])
for i in range(505):
    Posi = df_FW_players.at[i, 'Pos']
    GamesPlayedi = df_FW_players.at[i, '90s']
    xGi = df_FW_players.at[i, 'xG']
    if Posi == 'FW' and GamesPlayedi > 20 and xGi > 8:
        FWPlayers.append(df_FW_players.loc[i])
print(FWPlayers)

# MFFW
df_MFFW_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
for i in range(505):
    Posi = df_MFFW_players.at[i, 'Pos']
    GamesPlayedi = df_MFFW_players.at[i, '90s']
    KPi = df_MFFW_players.at[i, 'KP']
    if Posi == 'MFFW' and GamesPlayedi > 20 and KPi > 22:
        MFFWPlayers.append(df_MFFW_players.loc[i])
print(MFFWPlayers)

# MF
df_MF_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
for i in range(505):
    Posi = df_MF_players.at[i, 'Pos']
    GamesPlayedi = df_MF_players.at[i, '90s']
    CMPi = df_MF_players.at[i, 'Cmp%']
    KPi = df_MF_players.at[i, 'KP']
    if Posi == 'MF' and GamesPlayedi > 20 and CMPi > 75 and KPi >20 :
        MFPlayers.append(df_MF_players.loc[i])
print(MFPlayers)

# DF
df_DF_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
for i in range(505):
    Posi = df_DF_players.at[i, 'Pos']
    GamesPlayedi = df_DF_players.at[i, '90s']
    Blocksi = df_DF_players.at[i, 'Blocks']
    Tkli = df_DF_players.at[i, 'Tkl']
    if Posi == 'DF' and GamesPlayedi > 20 and Blocksi > 32 and Tkli > 45:
        DFPlayers.append(df_DF_players.loc[i])
print(DFPlayers)

# GK
df_GK_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'Save%', 'Price'])
for i in range(505):
    Posi = df_GK_players.at[i, 'Pos']
    GamesPlayedi = df_GK_players.at[i, '90s']
    Savei = df_GK_players.at[i, 'Save%']
    if Posi == 'GK' and GamesPlayedi > 20 and Savei > 70:
        GKPlayers.append(df_GK_players.loc[i])
print(GKPlayers)

#%%
# Poner todos los jugadores en un solo array para cada posicion
FWLength = len(LCFWPlayers)
for i in range(FWLength):
    FWPlayers.append(LCFWPlayers[i])

MFFWLength = len(LCMFFWPlayers)
for i in range(MFFWLength):
    MFFWPlayers.append(LCMFFWPlayers[i])

MFLength = len(LCMFPlayers)
for i in range(MFLength):
    MFPlayers.append(LCMFPlayers[i])

DFLength = len(LCDFPlayers)
for i in range(DFLength):
    DFPlayers.append(LCDFPlayers[i])

GKLength = len(LCGKPlayers)
for i in range(GKLength):
    GKPlayers.append(LCGKPlayers[i])

#%%
#FW
cFW = []
KPMFFW = []
xGMFFW = []
# for i in range(len(FWPlayers)):
#     cFW.append(FWPlayers[i][5])


#MFFW
cMFFW = []
for i in range(len(MFFWPlayers)):
    cMFFW.append(MFFWPlayers[i][7])
for i in range(len(MFFWPlayers)):
    KPMFFW.append(MFFWPlayers[i][5])
for i in range(len(MFFWPlayers)):
    xGMFFW.append(MFFWPlayers[i][3])

#MF
cMF = []
CMPMF = []
KPMF = []
TKLMF = []
for i in range(len(MFPlayers)):
    cMF.append(MFPlayers[i][6])
for i in range(len(MFPlayers)):
    KPMF.append(MFPlayers[i][5])
for i in range(len(MFPlayers)):
    CMPMF.append(MFPlayers[i][4])
for i in range(len(MFPlayers)):
    TKLMF.append(MFPlayers[i][3])

#DF
cDF = []
CMPDF = []
TKLDF = []
BDF = []
for i in range(len(DFPlayers)):
    cDF.append(DFPlayers[i][6])
for i in range(len(DFPlayers)):
    CMPDF.append(DFPlayers[i][5])
for i in range(len(DFPlayers)):
    TKLDF.append(DFPlayers[i][3])
for i in range(len(DFPlayers)):
    BDF.append(DFPlayers[i][4])


#GK
cGK = []
SavePGK = []
for i in range(len(GKPlayers)):
    cGK.append(GKPlayers[i][4])
for i in range(len(GKPlayers)):
    SavePGK.append(GKPlayers[i][3])

print(len(MFPlayers))
print(cMF)
print(CMPMF)
print(TKLMF)
print(KPMF)


#%%
# TODO -Problema Optimizacion
# Planteamos el problema con picos
import picos
# Creo el problema
P = picos.Problem()
# Tipo de jugadores
#FW
x = picos.BinaryVariable('x', 11)
#MFFW
y = picos.BinaryVariable('y', 16)
# #MF
z = picos.BinaryVariable('z', 15)
# #DF
w = picos.BinaryVariable('w', 34)
# #GK
v = picos.BinaryVariable('v', 5)
#Matriz de costos
cFW = np.array([[80000000.0, 45000000.0, 17000000.0, 7000000.0, 14500000.0, 1200000.0, 19000000.0, 0, 0, 0, 0]])
cMFFW = np.array([[825000.0, 7000000.0, 34000000.0, 3600000.0, 11000000.0, 525000.0, 3400000.0, 9000000.0, 13000000.0, 18500000.0, 12000000.0, 8000000.0, 0, 0, 0, 0]])
cMF = np.array([[65000000.0, 1800000.0, 12000000.0, 17500000.0, 31000000.0, 525000.0, 3800000.0, 10500000.0, 13500000.0, 10500000.0, 0, 0, 0, 0, 0]])
cDF = np.array([[4200000.0, 1900000.0, 13000000.0, 33000000.0, 27000000.0, 15500000.0, 9000000.0, 8000000.0, 2500000.0, 15500000.0, 7000000.0, 8000000.0, 13000000.0,13000000.0, 20000000.0, 6500000.0, 2000000.0, 3000000.0, 7000000.0, 8000000.0, 2200000.0, 3500000.0, 8500000.0, 1300000.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
cGK = np.array([[6000000.0, 5500000.0, 8000000.0, 22500000.0, 0]])

# print(FWPlayers)
print(MFFWPlayers)
print(MFPlayers)   
#xG FW 
xGFWTemp = np.array([[31.6, 23.7, 24.3, 9.1, 9.7, 9.0, 17.9, 0.1, 0.0, 19.7, 7.8]])
SoTFWTemp = np.array([[]])

#MFFW
KPMFFWTemp = np.array([[46, 48, 50, 52, 63, 32, 26, 32, 44, 38, 46, 24, 23, 6, 7, 52]])
xGMFFWTemp = np.array([[5.2, 4.8, 10.0, 5.6, 7.9, 5.5, 2.1, 2.8, 10.0, 7.6, 1.4, 3.9, 3.2, 0.3, 0.5, 4.4]])

#MF
KPMFTemp = np.array([[67, 49, 37, 22, 29, 25, 24, 26, 50, 21, 0, 0, 6, 0, 48]])
CMPMFTemp = np.array([[84.0, 78.2, 82.8, 83.6, 79.5, 84.0, 79.1, 78.6, 80.1, 77.2, 80.9, 77.8, 91.4, 73.1, 78.6]])
TKLMFTemp = np.array([[45, 25, 19, 50, 38, 89, 61, 60, 60, 90, 11, 1, 35, 0, 77]])

#DF 
CMPDFTemp = np.array([[83.7, 71.4, 92.9, 88.8, 62.7, 82.7, 72.6, 80.2, 85.1, 91.0, 81.5, 74.0, 92.8, 75.6, 89.1, 82.6, 72.8, 71.4, 80.9, 86.6, 81.1, 76.3, 84.8, 84.1, 89.0, 81.2, 85.8, 79.2, 87.5, 74.2, 78.3, 83.8, 100.0, 88.2]])
TKLDFTemp = np.array([[66, 51, 46, 65, 60, 76, 48, 63, 63, 64, 72, 58, 61, 60, 51, 63, 77, 58, 61, 50, 67, 71, 59, 63, 31, 15, 12, 63, 21, 23, 37, 59, 0, 63]])
BDFTemp = np.array([[72, 66, 38, 39, 67, 45, 53, 50, 41, 72, 70, 53, 58, 77, 40, 65, 50, 46, 68, 59, 67, 71, 63, 63, 22, 16, 19, 54, 27, 28, 28, 53, 0, 47]])

#GK
SavePTemp = np.array([[71.7, 71.5, 71.1, 70.3, 65.7]])
    
#Defino objetivo y función objetivo
P.set_objective('max', xGFWTemp*x + KPMFFWTemp*y + (1+xGMFFWTemp)*y + (1+KPMFTemp)*z + (1+TKLMFTemp)*z + CMPMFTemp*z + CMPDFTemp*w + (1+TKLDFTemp)*w + (1+BDFTemp)*w + SavePTemp*v)
# Interesante la funcion objetivo, tenemos que buscar la forma de darle el peso que le corresponde a cada estadistica /25? y hacerlo igual que el skill? 



#Constraints
#Limite de dinero
# P.add_constraint(sum(cFW) + sum(cMFFW) + sum(cMF) + sum(cDF) + sum(cGK) <= 150000000)
P.add_constraint(sum(cFW*x) + sum(cMFFW*y) + sum(cMF*z) + sum(cDF*w) + sum(cGK*v) <= 100000000)
#Limite de FW
P.add_constraint(sum(x) == 2)
#Limite de MFFW
P.add_constraint(sum(y) == 2)
#Limite de MF
P.add_constraint(sum(z) == 3)
#Limite de DF
P.add_constraint(sum(w) == 3)
#Limite de GK
P.add_constraint(sum(v) == 1)


#Verbosity
P.options.verbosity = 0
#Problema en consola
print(P)
#Resuelvo
P.solve(solver='glpk')
#Imprimo punto óptimo
print('x*=', x,
      'y*=', y,
      'z*=', z,
      'w*=', w,
      'v*=', v)
#Imprimo valor óptimo
print(P.value)
print(sum(cFW*x) + sum(cMFFW*y) + sum(cMF*z) + sum(cDF*w) + sum(cGK*v))

# Starting XI
startingXI = []
xGNew = []
SoTNew = []
KPNew = []
CMPNew = []
TKLNew = []
BNew = []
SPNew = []
for i in range(len(FWPlayers)):
    currentx = round(x[i])
    if currentx == 1:
        startingXI.append(FWPlayers[i][0])
        if FWPlayers[i][5] >= 1:
            xGNew.append(FWPlayers[i][3])
            SoTNew.append(FWPlayers[i][4])
for i in range(len(MFFWPlayers)):
    currenty = round(y[i])
    if currenty == 1:
        startingXI.append(MFFWPlayers[i][0])
        if MFFWPlayers[i][7] >= 1:
            xGNew.append(MFFWPlayers[i][3])
            KPNew.append(MFFWPlayers[i][5])
for i in range(len(MFPlayers)):
    currentz = round(z[i])
    if currentz == 1:
        startingXI.append(MFPlayers[i][0])
        if MFPlayers[i][6] >= 1:
            KPNew.append(MFPlayers[i][5])
            CMPNew.append(MFPlayers[i][4])
            TKLNew.append(MFPlayers[i][3])
for i in range(len(DFPlayers)):
    currentw = round(w[i])
    if currentw == 1:
        startingXI.append(DFPlayers[i][0])
        if DFPlayers[i][6] >= 1:
            CMPNew.append(DFPlayers[i][5])
            TKLNew.append(DFPlayers[i][3])
            BNew.append(DFPlayers[i][4])
for i in range(len(GKPlayers)):
    currentv = round(v[i])
    if currentv == 1:
        startingXI.append(GKPlayers[i][0])
        if GKPlayers[i][4] >= 1:
            SPNew.append(GKPlayers[i][3])   
print (startingXI)
print(sum(xGNew))
print(sum(SoTNew))
print(sum(KPNew))
print(sum(CMPNew)/len(CMPNew))
print(sum(TKLNew))
print(sum(BNew))
print(sum(SPNew))



# %%
# TODO - Rank Teams by Skill (incluyendo los nuevos cambios)
# ARMAR el mejor 11 sin vender 
# Stats de benched players un 1/4 de lo que reemplazan 


# %%
# TODO - Simulacion Teams con los cambios
