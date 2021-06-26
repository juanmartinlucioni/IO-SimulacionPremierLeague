#%% 
#Imports
#Librerias
import picos
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
#Data
team_stats_skills = pd.read_csv('league-stats-skill.csv')
new_team_stats_skills = pd.read_csv('new-league-stats-skill.csv')
pl_players_stats_skills = pd.read_csv('pl-players-stats-skills.csv')
bundes_player_stats = pd.read_csv('bundesliga-players-stats.csv')

#Funciones de Graficos
#Dibujo de Cancha con jugadores
#Source: https://fcpython.com/visualisation/drawing-pitchmap-adding-lines-circles-matplotlib
def createPitch(playernames,d,m,ma,f):
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

    #Players
    playername = []
    tempName = []
    # TODO - Arreglar para nombres simples 'RODRI' 'FRED', no aparecen
    for i in range(len(playernames)):
        tempName.append(playernames[i].partition(" ")[2])
        playername.append(tempName[i].partition("\\")[0])
    if d == 4 and m == 3 and ma == 1 and f == 2 :
        print('Formacion 4312')
        player0 = plt.Circle((10, 45), 3, edgecolor="black",
                            facecolor='orange', fill=True, label=playername[0])
        plt.text(3, 33, playername[10])
        ax.add_patch(player0)
        player1 = plt.Circle((37, 15), 3, edgecolor="black",
                            facecolor='yellow', fill=True, label=playername[1])
        plt.text(30, 5, playername[9])
        ax.add_patch(player1)
        player2 = plt.Circle((37, 75), 3, edgecolor="black",
                            facecolor='yellow', fill=True, label=playername[2])
        plt.text(30, 65, playername[8])
        ax.add_patch(player2)
        player3 = plt.Circle((30, 55), 3, edgecolor="black",
                            facecolor='yellow', fill=True, label=playername[3])
        plt.text(23, 45, playername[7])
        ax.add_patch(player3)
        player6 = plt.Circle((30, 35), 3, edgecolor="black",
                            facecolor="yellow", fill=True, label=playername[6])
        plt.text(23, 25, playername[6])
        player4 = plt.Circle((70, 25), 3, edgecolor="black",
                            facecolor="green", fill=True, label=playername[4])
        plt.text(65, 15, playername[4])
        ax.add_patch(player4)
        player5 = plt.Circle((55, 45), 3, edgecolor="black",
                            facecolor="green", fill=True, label=playername[5])
        plt.text(45, 35, playername[5])
        ax.add_patch(player5)
        ax.add_patch(player6)
        player7 = plt.Circle((70, 65), 3, edgecolor="black",
                            facecolor="green", fill=True, label=playername[7])
        plt.text(65, 55, playername[3])
        ax.add_patch(player7)
        player8 = plt.Circle((90, 45), 3, edgecolor="black",
                            facecolor="blue", fill=True, label=playername[8])
        plt.text(83, 35, playername[2])
        ax.add_patch(player8)
        player9 = plt.Circle((107, 60), 3, edgecolor="black",
                            facecolor="blue", fill=True, label=playername[9])
        plt.text(100, 50, playername[1])
        ax.add_patch(player9)
        player10 = plt.Circle((107, 30), 3, edgecolor="black",
                            facecolor="blue", fill=True, label=playername[10])
        plt.text(100, 20, playername[0])
        ax.add_patch(player10)
        #Display Pitch
        plt.show()
    elif d == 4 and m == 2 and ma == 3 and f == 1:
        print('Formacion 4231')
        player0 = plt.Circle((10, 45), 3, edgecolor="black",
                             facecolor='orange', fill=True, label=playername[0])
        plt.text(3, 33, playername[10])
        ax.add_patch(player0)
        player1 = plt.Circle((37, 15), 3, edgecolor="black",
                             facecolor='yellow', fill=True, label=playername[1])
        plt.text(30, 5, playername[9])
        ax.add_patch(player1)
        player2 = plt.Circle((37, 75), 3, edgecolor="black",
                             facecolor='yellow', fill=True, label=playername[2])
        plt.text(30, 65, playername[8])
        ax.add_patch(player2)
        player3 = plt.Circle((30, 55), 3, edgecolor="black",
                             facecolor='yellow', fill=True, label=playername[3])
        plt.text(23, 45, playername[7])
        ax.add_patch(player3)
        player6 = plt.Circle((30, 35), 3, edgecolor="black",
                             facecolor="yellow", fill=True, label=playername[6])
        plt.text(23, 25, playername[6])
        ax.add_patch(player6)
        player4 = plt.Circle((55, 35), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[4])
        plt.text(50, 25, playername[4])
        ax.add_patch(player4)
        player5 = plt.Circle((55, 55), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[5])
        plt.text(45, 45, playername[5])
        ax.add_patch(player5)
        player7 = plt.Circle((85, 45), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[7])
        plt.text(76, 35, playername[3])
        ax.add_patch(player7)
        player8 = plt.Circle((85, 75), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[8])
        plt.text(80, 65, playername[2])
        ax.add_patch(player8)
        player9 = plt.Circle((85, 15), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[9])
        plt.text(80, 5, playername[1])
        ax.add_patch(player9)
        player10 = plt.Circle((107, 45), 3, edgecolor="black",
                              facecolor="blue", fill=True, label=playername[10])
        plt.text(100, 35, playername[0])
        ax.add_patch(player10)
        #Display Pitch
        plt.show()
    elif d == 4 and m == 3 and ma == 0 and f == 3:
        print('Formacion 4303')
        player0 = plt.Circle((10, 45), 3, edgecolor="black",
                             facecolor='orange', fill=True, label=playername[0])
        plt.text(3, 33, playername[10])
        ax.add_patch(player0)
        player1 = plt.Circle((37, 15), 3, edgecolor="black",
                             facecolor='yellow', fill=True, label=playername[1])
        plt.text(30, 5, playername[6])
        ax.add_patch(player1)
        player2 = plt.Circle((37, 75), 3, edgecolor="black",
                             facecolor='yellow', fill=True, label=playername[2])
        plt.text(30, 65, playername[9])
        ax.add_patch(player2)
        player3 = plt.Circle((30, 55), 3, edgecolor="black",
                             facecolor='yellow', fill=True, label=playername[3])
        plt.text(23, 45, playername[7])
        ax.add_patch(player3)
        player6 = plt.Circle((30, 35), 3, edgecolor="black",
                             facecolor="yellow", fill=True, label=playername[6])
        plt.text(23, 25, playername[8])
        player4 = plt.Circle((70, 25), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[4])
        plt.text(65, 15, playername[4])
        ax.add_patch(player4)
        player5 = plt.Circle((55, 45), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[5])
        plt.text(45, 35, playername[5])
        ax.add_patch(player5)
        ax.add_patch(player6)
        player7 = plt.Circle((70, 65), 3, edgecolor="black",
                             facecolor="green", fill=True, label=playername[7])
        plt.text(65, 55, playername[3])
        ax.add_patch(player7)
        player8 = plt.Circle((105, 15), 3, edgecolor="black",
                             facecolor="blue", fill=True, label=playername[8])
        plt.text(98, 5, playername[2])
        ax.add_patch(player8)
        player9 = plt.Circle((105, 75), 3, edgecolor="black",
                             facecolor="blue", fill=True, label=playername[9])
        plt.text(98, 65, playername[1])
        ax.add_patch(player9)
        player10 = plt.Circle((107, 45), 3, edgecolor="black",
                              facecolor="blue", fill=True, label=playername[10])
        plt.text(100, 35, playername[0])
        ax.add_patch(player10)
        #Display Pitch
        plt.show()
    
# TODO - Funciones de graficos 


#Funcion Skills
Skill = []
Teams = []
def defineSkills(teamSkillSet):
    global Skill, Teams
    df_teams = pd.DataFrame(teamSkillSet, columns=['Rk', 'Squad', 'xG','xGA','Save%','SoT','Tkl','Blocks','Cmp%','KP','Poss'])
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

# TODO - Funcion para simular la liga
# Goles
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

def runLeague(dataSet, team, sims):
    avgPoints = np.zeros(shape=(sims, 20))
    avgWins = np.zeros(shape=(sims, 20))
    avgLoses = np.zeros(shape=(sims, 20))
    avgDraws = np.zeros(shape=(sims, 20))
    avgGF = np.zeros(shape=(sims, 20))
    avgGA = np.zeros(shape=(sims, 20))
    for i in range(sims):
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
                    
                    # dataSet[x][1][0]= Points[x]
                    # dataSet[x][1][1]= Wins[x]
                    # dataSet[x][1][2]= Draws[x]
                    # dataSet[x][1][3]= Loses[x]
                    # dataSet[x][1][4]= GF[x]
                    # dataSet[x][1][5]= GA[x]

                    # dataSet[y][1][0]= Points[y]
                    # dataSet[y][1][1]= Wins[y]
                    # dataSet[y][1][2]= Draws[y]
                    # dataSet[y][1][3]= Loses[y]
                    # dataSet[y][1][4]= GF[y]
                    # dataSet[y][1][5]= GA[y]

        #Send data to average            
        avgPoints[i] = Points
        avgWins[i] = Wins
        avgLoses[i] = Loses
        avgDraws[i] = Draws
        avgGF[i] = GF
        avgGA[i] = GA
    
    tablePoints = avgPoints.sum(axis=0)/sims
    tableWins = avgWins.sum(axis=0)/sims
    tableLoses = avgLoses.sum(axis=0)/sims
    tableDraws = avgDraws.sum(axis=0)/sims
    tableGF = avgGF.sum(axis=0)/sims
    tableGA = avgGA.sum(axis=0)/sims

    # dataSet[x][1][0]= Points[x]
    # dataSet[x][1][1]= Wins[x]
    # dataSet[x][1][2]= Draws[x]
    # dataSet[x][1][3]= Loses[x]
    # dataSet[x][1][4]= GF[x]
    # dataSet[x][1][5]= GA[x]

    #League Table
    sortedTeams = sorted(dataSet, key=lambda x: x[1][0], reverse=True)
    # print("| TEAM                      | POINTS | WINS | DRAWS | LOSSES | GOALS FOR | GOALS AGAINST | RANK |")
    for x in range(20):
        sortedTeams[x][1][6]= x+1
        # print('|', sortedTeams[x][0][0]," "*(24 - len(sortedTeams[x][0][0])),'|  ', sortedTeams[x][1][0]," "*(3 - len(str(sortedTeams[x][1][0]))),'| ', sortedTeams[x][1][1]," "*(2 - len(str(sortedTeams[x][1][1]))),'|  ', sortedTeams[x][1][2]," "*(2 - len(str(sortedTeams[x][1][2]))),'|  ', sortedTeams[x][1][3]," "*(3 - len(str(sortedTeams[x][1][3]))),'|    ', sortedTeams[x][1][4]," "*(4 - len(str(sortedTeams[x][1][4]))),"|     ", sortedTeams[x][1][5]," "*(7 - len(str(sortedTeams[x][1][5]))),"| ",x+1," "*(2 - len(str(sortedTeams[x][1][6]))),"|")

    # teamAvg =['name',['Points'],['Wins'],['Draws'],['Losses'],['GF'],['GA']]
    # for z in range(20):
    #     if sortedTeams[z][0][0] == team:
    #         myTeamPosRun = sortedTeams[z][1][6]
    #         myTeamPointsRun = sortedTeams[z][1][0] 

    # myTeamPos[i] = myTeamPosRun
    # myTeamPoints[i]= myTeamPointsRun

def runSimulation(skillSet, team, sims):
    defineSkills(skillSet)
    runLeague(Teams, team, sims)

runSimulation(team_stats_skills, 'Leicester City', 100)
#%%
#Funcion traer own team
MyStartingXI = []
MyStartingXI_xG = 0
MyStartingXI_SoT = 0
MyStartingXI_KP = 0
MyStartingXI_CMP = 0
MyStartingXI_TKL = 0
MyStartingXI_B = 0
MyStartingXI_SP = 0
MyFWPlayers = []
MyMFFWPlayers = []
MyMFPlayers = []
MyDFPlayers = []
MyGKPlayers = []

def myTeam(teamname,d,m,ma,f):
    global MyStartingXI_xG, MyStartingXI_SoT, MyStartingXI_KP, MyStartingXI_CMP, MyStartingXI_TKL, MyStartingXI_B, MyStartingXI_SP, MyFWPlayers, MyMFFWPlayers, MyMFPlayers, MyDFPlayers, MyGKPlayers
    #FW
    df_FW_players = pd.DataFrame(pl_players_stats_skills,  columns=['Player','Squad', '90s', 'Pos', 'xG', 'SoT', 'Price'])
    for i in range(532):
        Posi = df_FW_players.at[i, 'Pos']
        Squad = df_FW_players.at[i, 'Squad']
        if Posi == 'FW' and Squad == teamname:
            MyFWPlayers.append(df_FW_players.loc[i])
    xG_MyFW = []
    SoT_MyFW = []
    for i in range(len(MyFWPlayers)):
        xG_MyFW.append(MyFWPlayers[i][4])
    for i in range(len(MyFWPlayers)):
        SoT_MyFW.append(MyFWPlayers[i][5])
    #MFFW
    df_MFFW_players = pd.DataFrame(pl_players_stats_skills, columns=['Player', 'Squad', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
    for i in range(532):
        Posi = df_MFFW_players.at[i, 'Pos']
        Squad = df_MFFW_players.at[i, 'Squad']
        if Posi == 'MFFW' and Squad == teamname:
            MyMFFWPlayers.append(df_MFFW_players.loc[i])
        if Posi == 'FWMF' and Squad == teamname:
            MyMFFWPlayers.append(df_MFFW_players.loc[i])
        if Posi == 'DFFW' and Squad == teamname:
            MyMFFWPlayers.append(df_MFFW_players.loc[i])
    xG_MyMFFW = []
    SoT_MyMFFW = []
    KP_MyMFFW = []
    CMP_MyMFFW = []
    for i in range(len(MyMFFWPlayers)):
        KP_MyMFFW.append(MyMFFWPlayers[i][6])
    for i in range(len(MyMFFWPlayers)):
        xG_MyMFFW.append(MyMFFWPlayers[i][4])
    for i in range(len(MyMFFWPlayers)):
        SoT_MyMFFW.append(MyMFFWPlayers[i][5])
    for i in range(len(MyMFFWPlayers)):
        CMP_MyMFFW.append(MyMFFWPlayers[i][7])
    #MF
    df_MF_players = pd.DataFrame(pl_players_stats_skills, columns=['Player', 'Squad', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
    for i in range(532):
        Posi = df_MF_players.at[i, 'Pos']
        Squad = df_MF_players.at[i, 'Squad']
        if Posi == 'MF' and Squad == teamname:
            MyMFPlayers.append(df_MF_players.loc[i])
        if Posi == 'MFDF' and Squad == teamname:
            MyMFPlayers.append(df_MF_players.loc[i])
    KP_MyMF = []
    CMP_MyMF = []
    TKL_MyMF = []
    for i in range(len(MyMFPlayers)):
        KP_MyMF.append(MyMFPlayers[i][6])
    for i in range(len(MyMFPlayers)):
        CMP_MyMF.append(MyMFPlayers[i][5])
    for i in range(len(MyMFPlayers)):
        TKL_MyMF.append(MyMFPlayers[i][4])
    #DF
    df_DF_players = pd.DataFrame(pl_players_stats_skills, columns=['Player','Squad','90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
    for i in range(532):
        Posi = df_DF_players.at[i, 'Pos']
        Squad = df_DF_players.at[i, 'Squad']
        if Posi == 'DF' and Squad == teamname:
            MyDFPlayers.append(df_DF_players.loc[i])
    CMP_MyDF = []
    TKL_MyDF = []
    B_MyDF = []
    for i in range(len(MyDFPlayers)):
        B_MyDF.append(MyDFPlayers[i][5])
    for i in range(len(MyDFPlayers)):
        CMP_MyDF.append(MyDFPlayers[i][6])
    for i in range(len(MyDFPlayers)):
        TKL_MyDF.append(MyDFPlayers[i][4])
    #GK
    df_GK_players = pd.DataFrame(pl_players_stats_skills, columns=['Player', 'Squad','90s', 'Pos', 'Save%', 'Price'])
    for i in range(532):
        Posi = df_GK_players.at[i, 'Pos']
        GPi = df_GK_players.at[i, '90s']
        Squad = df_GK_players.at[i, 'Squad']
        if Posi == 'GK' and Squad == teamname and GPi > 10:
            MyGKPlayers.append(df_GK_players.loc[i])
    SP_MyGK = []
    for i in range(len(MyGKPlayers)):
        SP_MyGK.append(MyGKPlayers[i][4])

    # OPTIMIZACION - Best XI
    #Formacion
    formationDF = d
    formationMF = m
    formationMFFW = ma
    formationFW = f
    # Planteamos el problema con picos
    # Creo el problema
    P = picos.Problem()
    # Tipo de jugadores
    #FW
    f = picos.BinaryVariable('f', len(MyFWPlayers))
    #MFFW
    mffw = picos.BinaryVariable('mffw', len(MyMFFWPlayers))
    #MF
    mf = picos.BinaryVariable('mf', len(MyMFPlayers))
    #DF
    df = picos.BinaryVariable('df', len(MyDFPlayers))
    #GK
    gk = picos.BinaryVariable('gk', len(MyGKPlayers))

    #xG FW
    MyxGFWTemp = np.array([xG_MyFW])
    MySoTFWTemp = np.array([SoT_MyFW])

    #MFFW
    MyKPMFFWTemp = np.array([KP_MyMFFW])
    MyxGMFFWTemp = np.array([xG_MyMFFW])
    MySOTMFFWTemp = np.array([SoT_MyMFFW])
    MyCMPMFFWTemp = np.array([CMP_MyMFFW])

    #MF
    MyKPMFTemp = np.array([KP_MyMF])
    MyCMPMFTemp = np.array([CMP_MyMF])
    MyTKLMFTemp = np.array([TKL_MyMF])

    #DF
    MyCMPDFTemp = np.array([CMP_MyDF])
    MyTKLDFTemp = np.array([TKL_MyDF])
    MyBDFTemp = np.array([B_MyDF])

    #GK
    MySavePTemp = np.array([SP_MyGK])

    #Defino objetivo y función objetivo
    P.set_objective('max', MyxGFWTemp*f*50 + MySoTFWTemp*f*12.5 + MyKPMFFWTemp*mffw*25 + (1+MyxGMFFWTemp)*mffw*50 + MySOTMFFWTemp*mffw*12.5 + MyCMPMFFWTemp * mffw * 12.5 +
                    (1+MyKPMFTemp)*mf*25 + (1+MyTKLMFTemp)*mf*12.5 + MyCMPMFTemp*mf*12.5 + MyCMPDFTemp*df*12.5 + (1+MyTKLDFTemp)*df*12.5 + (1+MyBDFTemp)*df*12.5 + MySavePTemp*gk*25)
    #Constraints
    #Limite de FW
    P.add_constraint(sum(f) == formationFW)
    #Limite de MFFW
    P.add_constraint(sum(mffw) == formationMFFW)
    #Limite de MF
    P.add_constraint(sum(mf) == formationMF)
    #Limite de DF
    P.add_constraint(sum(df) == formationDF)
    #Limite de GK
    P.add_constraint(sum(gk) == 1)

    #Verbosity
    P.options.verbosity = 0
    #Problema en consola
    # print(P)
    #Resuelvo
    P.solve(solver='glpk')
    #Imprimo punto óptimo
    # print('f*=', f,
    #     'mffw*=', mffw,
    #     'mf*=', mf,
    #     'df*=', df,
    #     'gk*=', gk)
    #Imprimo valor óptimo
    # print(P.value)

    # Starting XI
    xGToReplace = []
    SoTToReplace = []
    KPToReplace = []
    CMPToReplace = []
    TKLToReplace = []
    BToReplace = []
    SPToReplace = []

    for i in range(len(MyFWPlayers)):
        currentx = round(f[i])
        if currentx == 1:
            MyStartingXI.append(MyFWPlayers[i][0])
            xGToReplace.append(MyFWPlayers[i][4])
            SoTToReplace.append(MyFWPlayers[i][5])
    for i in range(len(MyMFFWPlayers)):
        currenty = round(mffw[i])
        if currenty == 1:
            MyStartingXI.append(MyMFFWPlayers[i][0])
            xGToReplace.append(MyMFFWPlayers[i][4])
            SoTToReplace.append(MyMFFWPlayers[i][5])
            KPToReplace.append(MyMFFWPlayers[i][6])
            CMPToReplace.append(MyMFFWPlayers[i][7])
    for i in range(len(MyMFPlayers)):
        currentz = round(mf[i])
        if currentz == 1:
            MyStartingXI.append(MyMFPlayers[i][0])
            TKLToReplace.append(MyMFPlayers[i][4])
            CMPToReplace.append(MyMFPlayers[i][5])
            KPToReplace.append(MyMFPlayers[i][6])
    for i in range(len(MyDFPlayers)):
        currentw = round(df[i])
        if currentw == 1:
            MyStartingXI.append(MyDFPlayers[i][0])
            TKLToReplace.append(MyDFPlayers[i][4])
            BToReplace.append(MyDFPlayers[i][5])
            CMPToReplace.append(MyDFPlayers[i][6])
    for i in range(len(MyGKPlayers)):
        currentv = round(gk[i])
        if currentv == 1:
            MyStartingXI.append(MyGKPlayers[i][0])
            SPToReplace.append(MyGKPlayers[i][4])
    print(MyStartingXI)
    MyStartingXI_xG = sum(xGToReplace)
    MyStartingXI_SoT = sum(SoTToReplace)
    MyStartingXI_KP = sum(KPToReplace)
    MyStartingXI_CMP = sum(CMPToReplace)/len(CMPToReplace)
    MyStartingXI_TKL = sum(TKLToReplace)
    MyStartingXI_B = sum(BToReplace)
    MyStartingXI_SP = sum(SPToReplace)
    createPitch(MyStartingXI,d,m,ma,f)


# TODO - Funcion Merge Players to buy & optimizacion
# Top Players + MyPlayers
FWPlayers = []
MFFWPlayers = []
MFPlayers = []
DFPlayers = []
GKPlayers = []
#My new StartingXI data
MyNewStartingXI= []
MyNewPlayers_xG = 0 
MyNewPlayers_SoT = 0 
MyNewPlayers_KP = 0 
MyNewPlayers_CMP = 0 
MyNewPlayers_TKL = 0 
MyNewPlayers_B = 0 
MyNewPlayers_SP = 0 

def myNewTeam(money,d,m,ma,f):
    global FWPlayers, MFFWPlayers, MFPlayers, DFPlayers, GKPlayers, MyNewStartingXI, MyNewPlayers_xG, MyNewPlayers_SoT, MyNewPlayers_KP, MyNewPlayers_CMP, MyNewPlayers_TKL, MyNewPlayers_B, MyNewPlayers_SP
    #TODO - esto esta por si se quiere agregar o cambiar la liga donde se compra.
    league_players_stats = bundes_player_stats
    #TODO - a la hora de filtrar podriamos agregar que filter sea mejor que los jugadores de nuestro equipo, aka que xGi sea una variable de la media de cada equipo
    df_FW_players = pd.DataFrame(league_players_stats, columns=['Player','Squad', '90s', 'Pos', 'xG', 'SoT', 'Price'])
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
    df_MFFW_players = pd.DataFrame(league_players_stats, columns=['Player','Squad', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
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
    df_MF_players = pd.DataFrame(league_players_stats, columns=['Player','Squad', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
    for i in range(505):
        Posi = df_MF_players.at[i, 'Pos']
        GamesPlayedi = df_MF_players.at[i, '90s']
        CMPi = df_MF_players.at[i, 'Cmp%']
        KPi = df_MF_players.at[i, 'KP']
        Tkli = df_MF_players.at[i, 'Tkl']
        df_MF_players.at[i, 'KP'] = (KPi*2.69)/3.2
        df_MF_players.at[i, 'Tkl'] = (Tkli*2.69)/3.2
        if Posi == 'MF' and GamesPlayedi > 20 and CMPi > 75 and KPi > 20:
            MFPlayers.append(df_MF_players.loc[i])
        if Posi == 'DFMF' and GamesPlayedi > 20 and CMPi > 75 and KPi > 20:
            MFPlayers.append(df_MF_players.loc[i])
        if Posi == 'MFDF' and GamesPlayedi > 20 and CMPi > 75 and KPi > 20:
            MFPlayers.append(df_MF_players.loc[i])

    # DF
    df_DF_players = pd.DataFrame(league_players_stats, columns=['Player','Squad', '90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
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
    df_GK_players = pd.DataFrame(league_players_stats, columns=['Player','Squad','90s', 'Pos', 'Save%', 'Price'])
    for i in range(505):
        Posi = df_GK_players.at[i, 'Pos']
        GamesPlayedi = df_GK_players.at[i, '90s']
        Savei = df_GK_players.at[i, 'Save%']
        if Posi == 'GK' and GamesPlayedi > 20 and Savei > 70:
            GKPlayers.append(df_GK_players.loc[i])
    
    #Append MyPlayers a TopPlayers
    for i in range(len(MyFWPlayers)):
        FWPlayers.append(MyFWPlayers[i])
    for i in range(len(MyMFFWPlayers)):
        MFFWPlayers.append(MyMFFWPlayers[i])
    for i in range(len(MyMFPlayers)):
        MFPlayers.append(MyMFPlayers[i])
    for i in range(len(MyDFPlayers)):
        DFPlayers.append(MyDFPlayers[i])
    for i in range(len(MyGKPlayers)):
        GKPlayers.append(MyGKPlayers[i])
    
    #Datos de todos los jugadores
    #FW
    cFW = []
    xGFW = []
    SoTFW = []
    for i in range(len(FWPlayers)):
        cFW.append(FWPlayers[i][6])
    for i in range(len(FWPlayers)):
        xGFW.append(FWPlayers[i][4])
    for i in range(len(FWPlayers)):
        SoTFW.append(FWPlayers[i][5])

    #MFFW
    cMFFW = []
    KPMFFW = []
    xGMFFW = []
    SOTMFFW = []
    CMPMFFW = []
    for i in range(len(MFFWPlayers)):
        cMFFW.append(MFFWPlayers[i][8])
    for i in range(len(MFFWPlayers)):
        KPMFFW.append(MFFWPlayers[i][6])
    for i in range(len(MFFWPlayers)):
        xGMFFW.append(MFFWPlayers[i][4])
    for i in range(len(MFFWPlayers)):
        SOTMFFW.append(MFFWPlayers[i][5])
    for i in range(len(MFFWPlayers)):
        CMPMFFW.append(MFFWPlayers[i][7])

    #MF
    cMF = []
    CMPMF = []
    KPMF = []
    TKLMF = []
    for i in range(len(MFPlayers)):
        cMF.append(MFPlayers[i][7])
    for i in range(len(MFPlayers)):
        KPMF.append(MFPlayers[i][6])
    for i in range(len(MFPlayers)):
        CMPMF.append(MFPlayers[i][5])
    for i in range(len(MFPlayers)):
        TKLMF.append(MFPlayers[i][4])

    #DF
    cDF = []
    CMPDF = []
    TKLDF = []
    BDF = []
    for i in range(len(DFPlayers)):
        cDF.append(DFPlayers[i][7])
    for i in range(len(DFPlayers)):
        CMPDF.append(DFPlayers[i][6])
    for i in range(len(DFPlayers)):
        TKLDF.append(DFPlayers[i][4])
    for i in range(len(DFPlayers)):
        BDF.append(DFPlayers[i][5])


    #GK
    cGK = []
    SavePGK = []
    for i in range(len(GKPlayers)):
        cGK.append(GKPlayers[i][5])
    for i in range(len(GKPlayers)):
        SavePGK.append(GKPlayers[i][4])

    #%%
    # Problema Optimizacion
    #Formacion
    formationDF = d
    formationMF = m
    formationMFFW = ma
    formationFW = f
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
    P.add_constraint(sum(cFWTemp*x) + sum(cMFFWTemp*y) + sum(cMFTemp*z) + sum(cDFTemp*w) + sum(cGKTemp*v) <= money*1000000)
     #Limite de FW
    P.add_constraint(sum(x) == formationFW)
    #Limite de MFFW
    P.add_constraint(sum(y) == formationMFFW)
    #Limite de MF
    P.add_constraint(sum(z) == formationMF)
    #Limite de DF
    P.add_constraint(sum(w) == formationDF)
    #Limite de GK
    P.add_constraint(sum(v) == 1)

    #Verbosity
    P.options.verbosity = 0
    #Problema en consola
    # print(P)
    #Resuelvo
    P.solve(solver='glpk')
    #Imprimo punto óptimo
    # print('x*=', x,
    #     'y*=', y,
    #     'z*=', z,
    #     'w*=', w,
    #     'v*=', v)
    #Imprimo valor óptimo
    # print(P.value)
    print('Money Spent: ', sum(cFWTemp*x) + sum(cMFFWTemp*y) + sum(cMFTemp*z) + sum(cDFTemp*w) + sum(cGKTemp*v))

    #NewStartingXI
    MyNewStartingXI = []
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
            MyNewStartingXI.append(FWPlayers[i][0])
            xGNew.append(FWPlayers[i][4])
            SoTNew.append(FWPlayers[i][5])
    for i in range(len(MFFWPlayers)):
        currenty = round(y[i])
        if currenty == 1:
            MyNewStartingXI.append(MFFWPlayers[i][0])
            xGNew.append(MFFWPlayers[i][4])
            SoTNew.append(MFFWPlayers[i][5])
            KPNew.append(MFFWPlayers[i][6])
            CMPNew.append(MFFWPlayers[i][7])
    for i in range(len(MFPlayers)):
        currentz = round(z[i])
        if currentz == 1:
            MyNewStartingXI.append(MFPlayers[i][0])
            KPNew.append(MFPlayers[i][6])
            CMPNew.append(MFPlayers[i][5])
            TKLNew.append(MFPlayers[i][4])
    for i in range(len(DFPlayers)):
        currentw = round(w[i])
        if currentw == 1:
            MyNewStartingXI.append(DFPlayers[i][0])
            CMPNew.append(DFPlayers[i][6])
            TKLNew.append(DFPlayers[i][4])
            BNew.append(DFPlayers[i][5])
    for i in range(len(GKPlayers)):
        currentv = round(v[i])
        if currentv == 1:
            MyNewStartingXI.append(GKPlayers[i][0])
            SPNew.append(GKPlayers[i][4])   
    print(MyNewStartingXI)
    createPitch(MyNewStartingXI,d,m,ma,f)
    MyNewPlayers_xG = sum(xGNew)
    MyNewPlayers_SoT = sum(SoTNew)
    MyNewPlayers_KP = sum(KPNew)
    MyNewPlayers_CMP = sum(CMPNew)
    MyNewPlayers_TKL = sum(TKLNew)
    MyNewPlayers_B = sum(BNew)
    MyNewPlayers_SP = sum(SPNew)




# TODO - Funcion setear nuevo skillset del equipo

def runTeamImprovement(team,money,d,m,ma,f):
    myTeam(team,d,m,ma,f)
    myNewTeam(money,d,m,ma,f)



# Team = 'Leicester City'
# myTeam(Team,4,2,3,1)
# Team = 'Chelsea'
# myTeam(Team,4,2,3,1)
# Team = 'Liverpool'
# myTeam(Team,4,3,0,3)
Team = 'Manchester City'
# myTeam(Team,4,3,0,3)
# Team = 'Manchester Utd'
# myTeam(Team,4,2,3,1)

runTeamImprovement(Team,100,4,3,0,3)

# TODO - Una funcion que corra todo con el team deseado
    # Con opcion para correr liga actual o con optimizaciones (0 == actual, 1 == nuevo)
    # Actual seria defineskill => liga
# Nueva => defineSkill(? no se si seria necesario) > myTeam > New Team > defineSkill nuevo => Liga


# %%
