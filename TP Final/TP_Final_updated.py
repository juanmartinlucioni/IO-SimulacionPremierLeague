#%%
# TP FINAL - JUAN MARTIN LUCIONI Y MATIAS AYERZA
# Nos contrato el Leicester City, salio 5 en la temporada 20-21, Quiere que analizemos los posibles fichajes de cara a la proxima temporada para asegurar una clasificacion a la Champions League el año proximo (terminar top 4). Con los datos de todos los jugadores de la premier league y con un presupuesto de 100 Millones de Libras, traer los refuerzos para lograrlo. Reconocer en que areas hay que mejorar y reforzar las mismas. 

#IMPORTACION DE DATOS
#Datasets from: 
#https://fbref.com/en/comps/9/Premier-League-Stats
import picos
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
#Import Data
team_stats_skills = pd.read_csv('league-stats-skill.csv')
lc_stats_skills = pd.read_csv('LC_player_stats.csv')
bundes_player_stats = pd.read_csv('bundesliga-players-stats.csv')

# %%
# Rank Teams by Skill + Sim League without changes
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
    xGp = ((df_teams.at[i,'xG']/ bestXG)*50)
    Sotp = ((df_teams.at[i, 'SoT'] / bestSoT)*12.5)
    CPp = ((df_teams.at[i, 'Cmp%'] / bestCP)*12.5)
    KPp = ((df_teams.at[i, 'KP'] / bestKP)*25)
    #defensive stats
    xGAp = ((bestXGA / df_teams.at[i, 'xGA'])*50)
    Tp = ((df_teams.at[i, 'Tkl'] / bestT)*12.5)
    Bp = ((df_teams.at[i, 'Blocks'] / bestB)*12.5)
    SPp = ((df_teams.at[i, 'Save%'] / bestSP)*25)
    #Overall Stats
    atk = xGp + Sotp + KPp + CPp
    dfc = xGAp + Tp + Bp + SPp
    pos = df_teams.at[i, 'Poss']
    xG = df_teams.at[i, 'xG']
    Sp = df_teams.at[i, 'Save%']/3
    teambyskill = [df_teams.at[i,'Squad'],df_teams.at[i,'Rk'], atk.round(), dfc.round(), pos, xG/38,Sp]
    Skill.append(teambyskill)

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
print(Skill)
def homeGoals(ht, at):
    if ht[0] != at[0]:
        bonusRank = (-1 * (ht[1] - at[1]))/100
        bonusAtk = (ht[2] - at[3])/100
        bonusPossTemp= (ht[4] - at[4])/100
        if bonusPossTemp < 0.1:
            bonusPoss = 0.1
        else:
            bonusPoss = bonusPossTemp

        randomFactorTemp = np.random.uniform(-0.1, 0.1)
        randomFactor = round(randomFactorTemp)

        goals = 0

        # Better ATK
        if ht[2] > at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Equal ATK
        if ht[2] == at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Worse ATK
        if ht[2] < at[2]:
            xGToTest = ht[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor)
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
        bonusPossTemp = (at[4] - ht[4])/100
        if bonusPossTemp < 0.1:
            bonusPoss = 0.1
        else:
            bonusPoss = bonusPossTemp

        randomFactorTemp = np.random.uniform(-0.1, 0.1)
        randomFactor = round(randomFactorTemp)

        goals = 0

        # Better ATK
        if at[2] > ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Equal ATK
        if at[2] == ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Worse ATK
        if at[2] < ht[2]:
            xGToTest = at[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor)
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
        # print('=============================')
        # print(dataSet[x][0][0], 'Home Games')
        # print('=============================')
        for y in range(20):
            if dataSet[x][0] == dataSet[y][0]:
                pass
            else:
                homeScore = homeGoals(dataSet[x][0], dataSet[y][0])
                awayScore = awayGoals(dataSet[x][0], dataSet[y][0])
                # print(dataSet[x][0][0], homeScore,':', awayScore, dataSet[y][0][0])
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
        # print('|', sortedTeams[x][0][0]," "*(24 - len(sortedTeams[x][0][0])),'|  ', sortedTeams[x][1][0]," "*(3 - len(str(sortedTeams[x][1][0]))),'| ', sortedTeams[x][1][1]," "*(2 - len(str(sortedTeams[x][1][1]))),'|  ', sortedTeams[x][1][2]," "*(2 - len(str(sortedTeams[x][1][2]))),'|  ', sortedTeams[x][1][3]," "*(3 - len(str(sortedTeams[x][1][3]))),'|    ', sortedTeams[x][1][4]," "*(4 - len(str(sortedTeams[x][1][4]))),"|     ", sortedTeams[x][1][5]," "*(7 - len(str(sortedTeams[x][1][5]))),"| ",x+1," "*(2 - len(str(sortedTeams[x][1][6]))),"|")


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
# LC Players y comformacion del equipo + Top Bundes Players
# FW = xG + SOT  // x
# MFFW = xG + SOT + KP + CMP% // y
# MF = TK + KP + CMP% // z
# DF = TK + BLK + CMP% // w
# GK = %S  // v

# FW Players
df_LC_FW_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'xG', 'SoT', 'Price'])
LCFWPlayers = []
for i in range(27):
    Posi = df_LC_FW_players.at[i, 'Pos']
    if Posi == 'FW':
        LCFWPlayers.append(df_LC_FW_players.loc[i])

# MFFW 
df_LC_MFFW_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
LCMFFWPlayers = []
for i in range(27):
    Posi = df_LC_MFFW_players.at[i, 'Pos']
    if Posi == 'MFFW':
        LCMFFWPlayers.append(df_LC_MFFW_players.loc[i])
    if Posi == 'FWMF':
        LCMFFWPlayers.append(df_LC_MFFW_players.loc[i])
# MF
df_LC_MF_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
LCMFPlayers = []
for i in range(27):
    Posi = df_LC_MF_players.at[i, 'Pos']
    if Posi == 'MF':
        LCMFPlayers.append(df_LC_MF_players.loc[i])
    if Posi == 'MFDF':
        LCMFPlayers.append(df_LC_MF_players.loc[i])

# DF
df_LC_DF_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
LCDFPlayers = []
for i in range(27):
    Posi = df_LC_DF_players.at[i, 'Pos']
    if Posi == 'DF':
        LCDFPlayers.append(df_LC_DF_players.loc[i])
    if Posi == 'DFFW':
        LCDFPlayers.append(df_LC_DF_players.loc[i])

# GK
df_LC_GK_players = pd.DataFrame(lc_stats_skills, columns=['Player', '90s', 'Pos', 'Save%', 'Price'])
LCGKPlayers = []
for i in range(27):
    Posi = df_LC_GK_players.at[i, 'Pos']
    if Posi == 'GK':
        LCGKPlayers.append(df_LC_GK_players.loc[i])
#FW
xG_LC_FW = []
SoT_LC_FW = []
for i in range(len(LCFWPlayers)):
    xG_LC_FW.append(LCFWPlayers[i][3])
for i in range(len(LCFWPlayers)):
    SoT_LC_FW.append(LCFWPlayers[i][4])

#MFFW
xG_LC_MFFW = []
SoT_LC_MFFW = []
KP_LC_MFFW = []
CMP_LC_MFFW = []
for i in range(len(LCMFFWPlayers)):
    KP_LC_MFFW.append(LCMFFWPlayers[i][5])
for i in range(len(LCMFFWPlayers)):
    xG_LC_MFFW.append(LCMFFWPlayers[i][3])
for i in range(len(LCMFFWPlayers)):
    SoT_LC_MFFW.append(LCMFFWPlayers[i][4])
for i in range(len(LCMFFWPlayers)):
    CMP_LC_MFFW.append(LCMFFWPlayers[i][6])

# #MF
KP_LC_MF= []
CMP_LC_MF = []
TKL_LC_MF = []
for i in range(len(LCMFPlayers)):
    KP_LC_MF.append(LCMFPlayers[i][5])
for i in range(len(LCMFPlayers)):
    CMP_LC_MF.append(LCMFPlayers[i][4])
for i in range(len(LCMFPlayers)):
    TKL_LC_MF.append(LCMFPlayers[i][3])

# #DF
CMP_LC_DF = []
TKL_LC_DF = []
B_LC_DF = []
for i in range(len(LCDFPlayers)):
    B_LC_DF.append(LCDFPlayers[i][4])
for i in range(len(LCDFPlayers)):
    CMP_LC_DF.append(LCDFPlayers[i][5])
for i in range(len(LCDFPlayers)):
    TKL_LC_DF.append(LCDFPlayers[i][3])
# #GK
SP_LC_GK = []
for i in range(len(LCGKPlayers)):
    SP_LC_GK.append(LCGKPlayers[i][3])

#%%

#LC Best XI
# Planteamos el problema con picos
# Creo el problema
P = picos.Problem()
# Tipo de jugadores
#FW
f = picos.BinaryVariable('f', len(LCFWPlayers))
#MFFW
mffw = picos.BinaryVariable('mffw', len(LCMFFWPlayers))
#MF
mf = picos.BinaryVariable('mf', len(LCMFPlayers))
#DF
df = picos.BinaryVariable('df', len(LCDFPlayers))
#GK
gk = picos.BinaryVariable('gk', len(LCGKPlayers))

#xG FW
LC_xGFWTemp = np.array([xG_LC_FW])
LC_SoTFWTemp = np.array([SoT_LC_FW])

#MFFW
LC_KPMFFWTemp = np.array([KP_LC_MFFW])
LC_xGMFFWTemp = np.array([xG_LC_MFFW])
LC_SOTMFFWTemp = np.array([SoT_LC_MFFW])
LC_CMPMFFWTemp = np.array([CMP_LC_MFFW])

#MF
LC_KPMFTemp = np.array([KP_LC_MF])
LC_CMPMFTemp = np.array([CMP_LC_MF])
LC_TKLMFTemp = np.array([TKL_LC_MF])

#DF
LC_CMPDFTemp = np.array([CMP_LC_DF])
LC_TKLDFTemp = np.array([TKL_LC_DF])
LC_BDFTemp = np.array([B_LC_DF])

#GK
LC_SavePTemp = np.array([SP_LC_GK])

#Defino objetivo y función objetivo
P.set_objective('max', LC_xGFWTemp*f*50 + LC_SoTFWTemp*f*12.5 + LC_KPMFFWTemp*mffw*25 + (1+LC_xGMFFWTemp)*mffw*50 + LC_SOTMFFWTemp*mffw*12.5 + LC_CMPMFFWTemp *mffw *12.5+ (1+LC_KPMFTemp)*mf*25 + (1+LC_TKLMFTemp)*mf*12.5 + LC_CMPMFTemp*mf*12.5 + LC_CMPDFTemp*df*12.5 + (1+LC_TKLDFTemp)*df*12.5 + (1+LC_BDFTemp)*df*12.5 + LC_SavePTemp*gk*25)
#Constraints
#Limite de FW
P.add_constraint(sum(f) == 2)
#Limite de MFFW
P.add_constraint(sum(mffw) == 2)
#Limite de MF
P.add_constraint(sum(mf) == 3)
#Limite de DF
P.add_constraint(sum(df) == 3)
#Limite de GK
P.add_constraint(sum(gk) == 1)

#Verbosity
P.options.verbosity = 0
#Problema en consola
print(P)
#Resuelvo
P.solve(solver='glpk')
#Imprimo punto óptimo
print('f*=', f,
      'mffw*=', mffw,
      'mf*=', mf,
      'df*=', df,
      'gk*=', gk)
#Imprimo valor óptimo
print(P.value)

# Starting XI
xGToReplace = []
SoTToReplace = []
KPToReplace = []
CMPToReplace = []
TKLToReplace = []
BToReplace = []
SPToReplace = []
xGAToReplace = []
LC_startingXI = []

for i in range(len(LCFWPlayers)):
    currentx = round(f[i])
    if currentx == 1:
        LC_startingXI.append(LCFWPlayers[i][0])
        xGToReplace.append(LCFWPlayers[i][3])
        SoTToReplace.append(LCFWPlayers[i][4])
for i in range(len(LCMFFWPlayers)):
    currenty = round(mffw[i])
    if currenty == 1:
        LC_startingXI.append(LCMFFWPlayers[i][0])
        xGToReplace.append(LCMFFWPlayers[i][3])
        KPToReplace.append(LCMFFWPlayers[i][5])
        SoTToReplace.append(LCMFFWPlayers[i][4])
        CMPToReplace.append(LCMFFWPlayers[i][4])
for i in range(len(LCMFPlayers)):
    currentz = round(mf[i])
    if currentz == 1:
        LC_startingXI.append(LCMFPlayers[i][0])
        KPToReplace.append(LCMFPlayers[i][5])
        CMPToReplace.append(LCMFPlayers[i][4])
        TKLToReplace.append(LCMFPlayers[i][3])
for i in range(len(LCDFPlayers)):
    currentw = round(df[i])
    if currentw == 1:
        LC_startingXI.append(LCDFPlayers[i][0])
        CMPToReplace.append(LCDFPlayers[i][5])
        TKLToReplace.append(LCDFPlayers[i][3])
        BToReplace.append(LCDFPlayers[i][4])
for i in range(len(LCGKPlayers)):
    currentv = round(gk[i])
    if currentv == 1:
        LC_startingXI.append(LCGKPlayers[i][0])
        SPToReplace.append(LCGKPlayers[i][3])
print(LC_startingXI)

LC_StartingXI_xG = sum(xGToReplace)
LC_StartingXI_SoT = sum(SoTToReplace)
LC_StartingXI_KP = sum(KPToReplace)
LC_StartingXI_CMP = sum(CMPToReplace)/len(CMPToReplace)
LC_StartingXI_TKL = sum(TKLToReplace)
LC_StartingXI_B = sum(BToReplace)
LC_StartingXI_SP = sum(SPToReplace)

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
    SoTi = df_FW_players.at[i, 'SoT']
    df_FW_players.at[i, 'xG'] = (xGi*2.69)/3.2
    df_FW_players.at[i, 'SoT'] = (SoTi*2.69)/3.2
    if Posi == 'FW' and GamesPlayedi > 20 and xGi > 8:
        FWPlayers.append(df_FW_players.loc[i])

# MFFW
df_MFFW_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
for i in range(505):
    Posi = df_MFFW_players.at[i, 'Pos']
    GamesPlayedi = df_MFFW_players.at[i, '90s']
    KPi = df_MFFW_players.at[i, 'KP']
    xGi = df_MFFW_players.at[i, 'xG']
    SoTi = df_MFFW_players.at[i, 'SoT']
    df_MFFW_players.at[i, 'xG'] = (xGi*2.69)/3.2
    df_MFFW_players.at[i, 'SoT'] = (SoTi*2.69)/3.2
    df_MFFW_players.at[i, 'KP'] = (KPi*2.69)/3.2
    if Posi == 'MFFW' and GamesPlayedi > 20 and KPi > 22:
        MFFWPlayers.append(df_MFFW_players.loc[i])
    if Posi == 'FWMF' and GamesPlayedi > 20 and KPi > 22:
        MFFWPlayers.append(df_MFFW_players.loc[i])

# MF
df_MF_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
for i in range(505):
    Posi = df_MF_players.at[i, 'Pos']
    GamesPlayedi = df_MF_players.at[i, '90s']
    CMPi = df_MF_players.at[i, 'Cmp%']
    KPi = df_MF_players.at[i, 'KP']
    Tkli = df_MF_players.at[i, 'Tkl']
    df_MF_players.at[i, 'KP'] = (KPi*2.69)/3.2
    df_MF_players.at[i, 'Tkl'] = (Tkli*2.69)/3.2
    if Posi == 'MF' and GamesPlayedi > 20 and CMPi > 75 and KPi >20 :
        MFPlayers.append(df_MF_players.loc[i])
    if Posi == 'DFMF' and GamesPlayedi > 20 and CMPi > 75 and KPi >20 :
        MFPlayers.append(df_MF_players.loc[i])
    if Posi == 'MFDF' and GamesPlayedi > 20 and CMPi > 75 and KPi >20 :
        MFPlayers.append(df_MF_players.loc[i])

# DF
df_DF_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
for i in range(505):
    Posi = df_DF_players.at[i, 'Pos']
    GamesPlayedi = df_DF_players.at[i, '90s']
    Blocksi = df_DF_players.at[i, 'Blocks']
    Tkli = df_DF_players.at[i, 'Tkl']
    df_DF_players.at[i, 'Blocks'] = (Blocksi*2.69)/3.2
    df_DF_players.at[i, 'Tkl'] = (Tkli*2.69)/3.2
    if Posi == 'DF' and GamesPlayedi > 20 and Blocksi > 32 and Tkli > 45:
        DFPlayers.append(df_DF_players.loc[i])
    if Posi == 'DFFW' and GamesPlayedi > 20 and Blocksi > 32 and Tkli > 45:
        DFPlayers.append(df_DF_players.loc[i])

# GK
df_GK_players = pd.DataFrame(league_players_stats, columns=['Player', '90s', 'Pos', 'Save%', 'Price'])
for i in range(505):
    Posi = df_GK_players.at[i, 'Pos']
    GamesPlayedi = df_GK_players.at[i, '90s']
    Savei = df_GK_players.at[i, 'Save%']
    if Posi == 'GK' and GamesPlayedi > 20 and Savei > 70:
        GKPlayers.append(df_GK_players.loc[i])

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

#FW
cFW = []
xGFW = []
SoTFW = []
for i in range(len(FWPlayers)):
    cFW.append(FWPlayers[i][5])
for i in range(len(FWPlayers)):
    xGFW.append(FWPlayers[i][3])
for i in range(len(FWPlayers)):
    SoTFW.append(FWPlayers[i][4])

#MFFW
cMFFW = []
KPMFFW = []
xGMFFW = []
SOTMFFW = []
CMPMFFW = []
for i in range(len(MFFWPlayers)):
    cMFFW.append(MFFWPlayers[i][7])
for i in range(len(MFFWPlayers)):
    KPMFFW.append(MFFWPlayers[i][5])
for i in range(len(MFFWPlayers)):
    xGMFFW.append(MFFWPlayers[i][3])
for i in range(len(MFFWPlayers)):
    SOTMFFW.append(MFFWPlayers[i][4])
for i in range(len(MFFWPlayers)):
    CMPMFFW.append(MFFWPlayers[i][6])

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

#%%
# Problema Optimizacion
# Planteamos el problema con picos
import picos
# Creo el problema
P = picos.Problem()
# Tipo de jugadores
#FW
x = picos.BinaryVariable('x', len(FWPlayers))
#MFFW
y = picos.BinaryVariable('y', len(MFFWPlayers))
#MF
z = picos.BinaryVariable('z', len(MFPlayers))
#DF
w = picos.BinaryVariable('w', len(DFPlayers))
#GK
v = picos.BinaryVariable('v', len(GKPlayers))

#Matriz de costos
cFWTemp = np.array([cFW])
cMFFWTemp = np.array([cMFFW])
cMFTemp = np.array([cMF])
cDFTemp = np.array([cDF])
cGKTemp = np.array([cGK])

#xG FW 
xGFWTemp = np.array([xGFW])
SoTFWTemp = np.array([SoTFW])

#MFFW
KPMFFWTemp = np.array([KPMFFW])
xGMFFWTemp = np.array([xGMFFW])
SOTMFFWTemp = np.array([SOTMFFW])
CMPMFFWTemp = np.array([CMPMFFW])

#MF
KPMFTemp = np.array([KPMF])
CMPMFTemp = np.array([CMPMF])
TKLMFTemp = np.array([TKLMF])

#DF 
CMPDFTemp = np.array([CMPDF])
TKLDFTemp = np.array([TKLDF])
BDFTemp = np.array([BDF])

#GK
SavePTemp = np.array([SavePGK])
    
#Defino objetivo y función objetivo
P.set_objective('max', xGFWTemp*x*50 + SoTFWTemp*x*12.5 + KPMFFWTemp*y*25 + (1+xGMFFWTemp)*y*50 + SOTMFFWTemp*y*12.5 + CMPMFFWTemp*y*12.5 + (1+KPMFTemp)*z*25 + (1+TKLMFTemp)*z*12.5 + CMPMFTemp*z*12.5 + CMPDFTemp*w*12.5 + (1+TKLDFTemp)*w*12.5 + (1+BDFTemp)*w*12.5 + SavePTemp*v*25)
# Interesante la funcion objetivo, tenemos que buscar la forma de darle el peso que le corresponde a cada estadistica /25? y hacerlo igual que el skill? 

#Constraints
#Limite de dinero
# P.add_constraint(sum(cFW) + sum(cMFFW) + sum(cMF) + sum(cDF) + sum(cGK) <= 150000000)
P.add_constraint(sum(cFWTemp*x) + sum(cMFFWTemp*y) + sum(cMFTemp*z) + sum(cDFTemp*w) + sum(cGKTemp*v) <= 100000000)
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
print(sum(cFWTemp*x) + sum(cMFFWTemp*y) + sum(cMFTemp*z) + sum(cDFTemp*w) + sum(cGKTemp*v))

# Starting XI
startingXI = []
xGNew = []
SoTNew = []
KPNew = []
CMPNew = []
TKLNew = []
BNew = []
SPNew = []
xGANew = []
for i in range(len(FWPlayers)):
    currentx = round(x[i])
    if currentx == 1:
        startingXI.append(FWPlayers[i][0])
        xGNew.append(FWPlayers[i][3])
        SoTNew.append(FWPlayers[i][4])
for i in range(len(MFFWPlayers)):
    currenty = round(y[i])
    if currenty == 1:
        startingXI.append(MFFWPlayers[i][0])
        xGNew.append(MFFWPlayers[i][3])
        KPNew.append(MFFWPlayers[i][5])
        SoTNew.append(MFFWPlayers[i][4])
        CMPNew.append(MFFWPlayers[i][4])
for i in range(len(MFPlayers)):
    currentz = round(z[i])
    if currentz == 1:
        startingXI.append(MFPlayers[i][0])
        KPNew.append(MFPlayers[i][5])
        CMPNew.append(MFPlayers[i][4])
        TKLNew.append(MFPlayers[i][3])
for i in range(len(DFPlayers)):
    currentw = round(w[i])
    if currentw == 1:
        startingXI.append(DFPlayers[i][0])
        CMPNew.append(DFPlayers[i][5])
        TKLNew.append(DFPlayers[i][3])
        BNew.append(DFPlayers[i][4])
for i in range(len(GKPlayers)):
    currentv = round(v[i])
    if currentv == 1:
        startingXI.append(GKPlayers[i][0])
        SPNew.append(GKPlayers[i][3])   
print (startingXI)
NewPlayers_xG = sum(xGNew)
NewPlayers_SoT = sum(SoTNew)
NewPlayers_KP = sum(KPNew)
NewPlayers_CMP = sum(CMPNew)
NewPlayers_TKL = sum(TKLNew)
NewPlayers_B = sum(BNew)
NewPlayers_SP = sum(SPNew)

#%%
#Set up new-league-stats-skills
LC_name = df_teams.at[4, 'Squad']
LC_xG= df_teams.at[4, 'xG']
LC_Sot = df_teams.at[4, 'SoT'] 
LC_KP = df_teams.at[4, 'KP'] 
LC_CP = df_teams.at[4, 'Cmp%']
#Defensive Stats
LC_xGA = df_teams.at[4, 'xGA']
LC_T = df_teams.at[4, 'Tkl']
LC_B = df_teams.at[4, 'Blocks']
LC_SP = df_teams.at[4, 'Save%']
LC_Stats = [LC_name, LC_xG, LC_Sot, LC_KP, LC_CP, LC_xGA, LC_T, LC_B, LC_SP]

LC_Def_xGA = ((bestXGA / LC_xGA)*50)
LC_Def_T = ((LC_T / bestT)*12.5)
LC_Def_B = ((LC_B / bestB)*12.5)
LC_Def_SP = ((LC_SP / bestSP)*25)

#atk
LC_New_xG = LC_xG - LC_StartingXI_xG + NewPlayers_xG
LC_New_SoT = LC_Sot - LC_StartingXI_SoT + NewPlayers_SoT
LC_New_KP = LC_KP - LC_StartingXI_KP + NewPlayers_KP
LC_New_CP = (LC_CP*len(lc_stats_skills) + NewPlayers_CMP)/(len(lc_stats_skills)+len(CMPNew))
#dfc 
LC_New_TKL = LC_T - LC_StartingXI_TKL + NewPlayers_TKL
LC_New_B = LC_B - - LC_StartingXI_B + NewPlayers_B
LC_New_SP = NewPlayers_SP

#New xGA Calc
Comparison_Def_Base = LC_Def_T + LC_Def_B + LC_Def_SP

LC_New_Def_T2 = ((LC_New_TKL/LC_T)-1)
LC_New_Def_B2 = ((LC_New_B/LC_B)-1)
LC_New_Def_SP2 = ((LC_New_SP/LC_SP)-1)

New_Def_Base = LC_Def_T*(1+LC_New_Def_T2) + LC_Def_B*(1+LC_New_Def_B2) + LC_Def_SP*(1+LC_New_Def_SP2)

#New xGA
Def_Mejora = (New_Def_Base/Comparison_Def_Base)-1
LC_xGA2 = LC_xGA*(1-Def_Mejora)
LC_New_xGA = LC_xGA2

#import Data
team_stats_skills.at[4,'xG']=LC_New_xG
team_stats_skills.at[4,'SoT']=LC_New_SoT
team_stats_skills.at[4,'KP']=LC_New_KP
team_stats_skills.at[4,'Cmp%']=LC_New_CP
team_stats_skills.at[4,'xGA']=LC_New_xGA
team_stats_skills.at[4,'Tkl']=LC_New_TKL
team_stats_skills.at[4,'Blocks']=LC_New_B
team_stats_skills.at[4,'Save%']=LC_New_SP

team_stats_skills.to_csv('new-league-stats-skill.csv',index=False)

# %%
# Rank Teams by Skill (incluyendo los nuevos cambios) + Sim League With Changes
new_team_stats_skills = pd.read_csv('new-league-stats-skill.csv')
df_new_teams = pd.DataFrame(new_team_stats_skills, columns=['Rk', 'Squad', 'xG','xGA','Save%','SoT','Tkl','Blocks','Cmp%','KP','Poss'])
newSkill = []
newBestXG = df_new_teams['xG'].max()
newBestXGA = df_new_teams['xGA'].min()
newBestSP = df_new_teams['Save%'].max()
newBestSoT = df_new_teams['SoT'].max()
newBestT = df_new_teams['Tkl'].max()
newBestB = df_new_teams['Blocks'].max() 
newBestCP = df_new_teams['Cmp%'].max()
newBestKP = df_new_teams['KP'].max()

for i in range(20):
    #atacking stats
    xGpNew = ((df_new_teams.at[i,'xG']/ newBestXG)*50)
    KPpNew = ((df_new_teams.at[i, 'KP'] / newBestKP)*25)
    SotpNew = ((df_new_teams.at[i, 'SoT'] / newBestSoT)*12.5)
    CPpNew = ((df_new_teams.at[i, 'Cmp%'] / newBestCP)*12.5)
    #defensive stats
    xGApNew = ((newBestXGA / df_new_teams.at[i, 'xGA'])*50)
    SPpNew = ((df_new_teams.at[i, 'Save%'] / newBestSP)*25)
    TpNew = ((df_new_teams.at[i, 'Tkl'] / newBestT)*12.5)
    BpNew = ((df_new_teams.at[i, 'Blocks'] / newBestB)*12.5)
    #Overall Stats
    atk = xGpNew + SotpNew + KPpNew + CPpNew
    dfc = xGApNew + TpNew + BpNew + SPpNew
    pos = df_new_teams.at[i, 'Poss']
    xG = df_new_teams.at[i, 'xG']
    Sp = df_new_teams.at[i, 'Save%']/3
    teambyskill = [df_new_teams.at[i,'Squad'],df_new_teams.at[i,'Rk'], atk.round(), dfc.round(), pos, xG/38,Sp]
    newSkill.append(teambyskill)    
print(newSkill)
# Teams
ManchesterCity = [newSkill[0], [0,0,0,0,0,0,0]]
ManchesterUtd = [newSkill[1], [0,0,0,0,0,0,0]]
Liverpool = [newSkill[2], [0,0,0,0,0,0,0]]
Chelsea = [newSkill[3], [0,0,0,0,0,0,0]]
LeicesterCity = [newSkill[4], [0,0,0,0,0,0,0]]
WestHam = [newSkill[5], [0,0,0,0,0,0,0]]
Tottenham = [newSkill[6], [0,0,0,0,0,0,0]]
Arsenal = [newSkill[7], [0,0,0,0,0,0,0]]
LeedsUnited = [newSkill[8], [0,0,0,0,0,0,0]]
Everton = [newSkill[9], [0,0,0,0,0,0,0]]
AstonVilla = [newSkill[10], [0,0,0,0,0,0,0]]
NewcastleUtd = [newSkill[11], [0,0,0,0,0,0,0]]
Wolves = [newSkill[12], [0,0,0,0,0,0,0]]
CrystalPalace = [newSkill[13], [0,0,0,0,0,0,0]]
Southampton = [newSkill[14], [0,0,0,0,0,0,0]]
Brighton = [newSkill[15], [0,0,0,0,0,0,0,0]]
Burnley = [newSkill[16], [0,0,0,0,0,0,0,0]]
Fulham = [newSkill[17], [0,0,0,0,0,0,0]]
WestBrom = [newSkill[18], [0,0,0,0,0,0,0]]
SheffieldUtd = [newSkill[19], [0,0,0,0,0,0,0]]

newTeams = [ManchesterCity, ManchesterUtd, Liverpool, Chelsea, LeicesterCity, WestHam, Tottenham, Arsenal, LeedsUnited, Everton, AstonVilla, NewcastleUtd, Wolves, CrystalPalace, Southampton, Brighton, Burnley, Fulham, WestBrom, SheffieldUtd]

# Sim
nSim = 1000
LCPos = np.zeros(nSim)

for i in range(nSim):
    runLeague(newTeams)
print('Probabilidad de que Leicester City termine en el Top 4: ',np.sum(LCPos < 5)/nSim)

#Corriendo la nueva liga 10000 veces LC termina en el top 4 = 0.619 with nerf a nuevos 1/2 y viejos 4/5 presupuesto de 100.000.000
#Corriendo la nueva liga 10000 veces LC termina en el top 4 = 0.923 with nerf 2/3 a viejos
#Corriendo la nueva liga 10000 veces LC termina en el top 4 = 0.782 con nerfs por cambio de liga pre-optimizacion
#%%
# Cantidad de veces en las que termina en cada posicion
plt.hist(LCPos ,range=[1, 5], bins=5, density=False)
plt.title('Posicion del LC en la liga')
plt.ylabel('Cantidad de Veces')
plt.xlabel('Posicion')
plt.show()
# Posicion en la liga para cada SIM
plt.plot(LCPos)
plt.title('Posicion del LC en la liga')
plt.ylabel('Posicion')
plt.xlabel('Sim')
plt.show()
# Power ranking? 


#%%
# La funcion de la cancha la tomamos de: https://fcpython.com/visualisation/drawing-pitchmap-adding-lines-circles-matplotlib

def createPitch(playernames):

    #Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    #Pitch Outline & Centre Line
    plt.plot([0, 0], [0, 90], color="black")
    plt.plot([0, 130], [90, 90], color="black")
    plt.plot([130, 130], [90, 0], color="black")
    plt.plot([130, 0], [0, 0], color="black")
    plt.plot([65, 65], [0, 90], color="black")

    #Left Penalty Area
    plt.plot([16.5, 16.5], [65, 25], color="black")
    plt.plot([0, 16.5], [65, 65], color="black")
    plt.plot([16.5, 0], [25, 25], color="black")

    #Right Penalty Area
    plt.plot([130, 113.5], [65, 65], color="black")
    plt.plot([113.5, 113.5], [65, 25], color="black")
    plt.plot([113.5, 130], [25, 25], color="black")

    #Left 6-yard Box
    plt.plot([0, 5.5], [54, 54], color="black")
    plt.plot([5.5, 5.5], [54, 36], color="black")
    plt.plot([5.5, 0.5], [36, 36], color="black")

    #Right 6-yard Box
    plt.plot([130, 124.5], [54, 54], color="black")
    plt.plot([124.5, 124.5], [54, 36], color="black")
    plt.plot([124.5, 130], [36, 36], color="black")

    #Prepare Circles
    centreCircle = plt.Circle((65, 45), 9.15, color="black", fill=False)
    centreSpot = plt.Circle((65, 45), 0.8, color="black")
    leftPenSpot = plt.Circle((11, 45), 0.8, color="black")
    rightPenSpot = plt.Circle((119, 45), 0.8, color="black")

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    #Prepare Arcs
    leftArc = Arc((11, 45), height=18.3, width=18.3, angle=0,

                  theta1=310, theta2=50, color="black")
    rightArc = Arc((119, 45), height=18.3, width=18.3, angle=0,
                   theta1=130, theta2=230, color="black")

    # #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    #Tidy Axes
    plt.axis('off')

    playername = []
    tempName = []
    for i in range(len(playernames)):
        tempName.append(playernames[i].partition(" ")[2])
        playername.append(tempName[i].partition("\\")[0])

    player0 = plt.Circle((10,45), 3, edgecolor="black",facecolor='orange', fill=True, label=playername[0])
    plt.text(3, 33, playername[10])
    ax.add_patch(player0)
    player1 = plt.Circle((37,25), 3, edgecolor="black",facecolor='yellow', fill=True, label=playername[1])
    plt.text(30, 15, playername[9])
    ax.add_patch(player1)
    player2 = plt.Circle((37,65), 3, edgecolor="black",facecolor='yellow', fill=True, label=playername[2])
    plt.text(29, 55, playername[8])
    ax.add_patch(player2)
    player3 = plt.Circle((30,45), 3, edgecolor="black",facecolor='yellow', fill=True, label=playername[3])
    plt.text(23, 37, playername[7])
    ax.add_patch(player3)
    player4 = plt.Circle((70, 15), 3, edgecolor="black", facecolor="green", fill=True, label=playername[4])
    plt.text(59, 5, playername[4])
    ax.add_patch(player4)
    player5 = plt.Circle((70, 75), 3, edgecolor="black", facecolor="green", fill=True, label=playername[5])
    plt.text(65, 65, playername[5])
    ax.add_patch(player5)
    player6 = plt.Circle((55, 45), 3, edgecolor="black", facecolor="green", fill=True, label=playername[6])
    plt.text(47, 35, playername[6])
    ax.add_patch(player6)
    player7 = plt.Circle((90, 60), 3, edgecolor="black", facecolor="blue", fill=True, label=playername[7])
    plt.text(82, 50, playername[3])
    ax.add_patch(player7)
    player8 = plt.Circle((90, 30), 3, edgecolor="black", facecolor="blue", fill=True, label=playername[8])
    plt.text(80, 20, playername[2])
    ax.add_patch(player8)
    player9 = plt.Circle((120, 50), 3, edgecolor="black", facecolor="blue", fill=True, label=playername[9])
    plt.text(113, 40, playername[1])
    ax.add_patch(player9)
    player10 = plt.Circle((110, 40), 3, edgecolor="black", facecolor="blue", fill=True, label=playername[10])
    plt.text(105, 30, playername[0])
    ax.add_patch(player10)

    #Display Pitch
    plt.show()

createPitch(LC_startingXI)
createPitch(startingXI)

# %%
