#%% 
#Imports
#Librerias
import picos
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Arc
#Data
team_stats_skills = pd.read_csv('league-stats-skill.csv')
# new_team_stats_skills = pd.read_csv('new-league-stats-skill.csv')
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
    for i in range(len(playernames)):
        tempName.append(playernames[i].partition("\\")[2])
        if tempName[i].find('-') == -1:
            playername.append(tempName[i])
        else:
            playername.append(tempName[i].partition("-")[2])
            if playername[i].find('-') != -1:
                playername[i] = playername[i].replace('-', " ")
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
# Graficos
def scatter_xG(stats):
    fig, ax = plt.subplots()

    #Set plot size
    fig.set_size_inches(7, 5)
    Atk = []
    Dfc = []
    for i in range(len(stats)):
        plt.plot(stats[i][2], stats[i][3], "o",label=stats[i][0])
        Atk.append(stats[i][2])
        Dfc.append(stats[i][3])
        if stats[i][1] < 6:
            plt.text(stats[i][2], stats[i][3]+1,stats[i][0])
        # if stats[i][0] == "Leicester City":
        #     plt.text(stats[i][2], stats[i][3]+1,'Leicester City')
    #Cross
    plt.plot([sum(Atk)/len(Atk),sum(Atk)/len(Atk)],[100,50],'k-', linestyle = ":", lw=1)
    plt.plot([50,100],[sum(Dfc)/len(Dfc),sum(Dfc)/len(Dfc)],'k-', linestyle = ":", lw=1)

    #Add labels to chart area
    ax.set_title("Skill Ranking")
    ax.set_xlabel("Attack")
    ax.set_ylabel("Defence")

    ax.text(49,50,"Poor attack, poor defense",color="red",size="8")

    ax.text(85,99,"Strong attack, strong defense",color="red",size="8")

    #Display the chart
    plt.show()

#Funciones de simulacion y optimizacion
#Funcion Skills
Skill = []
Teams = []

def defineSkills(teamSkillSet):
    #RESET VARIABLES
    global Skill, Teams
    Skill = []
    Teams = []

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
        teamName = df_teams.at[i, 'Squad']
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
        teambyskill = [df_teams.at[i,'Squad'],df_teams.at[i,'Rk'], atk.round(), dfc.round(), pos, (xG/38).round(2),Sp.round(2)]
        Skill.append(teambyskill)

    # Teams
    ManchesterCity = [Skill[0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    ManchesterUtd = [Skill[1], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Liverpool = [Skill[2], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Chelsea = [Skill[3], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    LeicesterCity = [Skill[4], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    WestHam = [Skill[5], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Tottenham = [Skill[6], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Arsenal = [Skill[7], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    LeedsUnited = [Skill[8], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Everton = [Skill[9], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    AstonVilla = [Skill[10], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    NewcastleUtd = [Skill[11], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Wolves = [Skill[12], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    CrystalPalace = [Skill[13], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Southampton = [Skill[14], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Brighton = [Skill[15], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Burnley = [Skill[16], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    Fulham = [Skill[17], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    WestBrom = [Skill[18], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
    SheffieldUtd = [Skill[19], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]

    Teams = [ManchesterCity, ManchesterUtd, Liverpool, Chelsea, LeicesterCity, WestHam, Tottenham, Arsenal, LeedsUnited, Everton, AstonVilla, NewcastleUtd, Wolves, CrystalPalace, Southampton, Brighton, Burnley, Fulham, WestBrom, SheffieldUtd]

# Funcion para simular la liga
# Goles
def homeGoals(ht, at):
    if ht[0] != at[0]:
        bonusRank = (-1 * (ht[1] - at[1]))/100
        bonusAtk = (ht[2] - at[3])/100
        bonusPoss = (ht[4] - at[4])/100

        goals = 0

        # Better ATK
        if ht[2] > at[2]:
            randomFactorTemp = np.random.uniform(-0.15, 0.15)
            randomFactor = round(randomFactorTemp, 2)
            xGToTest = ht[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor) + 0.25
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Equal ATK
        if ht[2] == at[2]:
            randomFactorTemp = np.random.uniform(-0.15, 0.15)
            randomFactor = round(randomFactorTemp, 2)
            xGToTest = ht[5] * (1+bonusRank+bonusPoss+randomFactor) + 0.25
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > at[6]/100:
                    goals += 1

        # Worse ATK
        if ht[2] < at[2]:
            randomFactorTemp = np.random.uniform(-0.15, 0.15)
            randomFactor = round(randomFactorTemp, 2)
            xGToTest = ht[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor) + 0.25
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
        bonusPoss = (at[4] - ht[4])/100

        goals = 0

        # Better ATK
        if at[2] > ht[2]:
            randomFactorTemp = np.random.uniform(-0.15, 0.15)
            randomFactor = round(randomFactorTemp, 2)
            xGToTest = at[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Equal ATK
        if at[2] == ht[2]:
            randomFactorTemp = np.random.uniform(-0.15, 0.15)
            randomFactor = round(randomFactorTemp, 2)
            xGToTest = at[5] * (1+bonusRank+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1

        # Worse ATK
        if at[2] < ht[2]:
            randomFactorTemp = np.random.uniform(-0.15, 0.15)
            randomFactor = round(randomFactorTemp, 2)
            xGToTest = at[5] * (1+bonusRank+bonusAtk+bonusPoss+randomFactor)
            xGTestRound = round(xGToTest)
            for i in range(xGTestRound):
                chanceOfGoal = np.random.random()
                if chanceOfGoal > ht[6]/100:
                    goals += 1
        return goals
    else:
        return 'Same Team'

def runLeague(dataSet, team, nSim):
    #TODO - Probabilidad de batacazo en un partido? Menos probable si la dif de goles es alta
    myTeamPosRun = np.zeros(nSim)
    MCPosRun = np.zeros(nSim)
    myTeamPointsRun = np.zeros(nSim)
    MCPointsRun = np.zeros(nSim)
    runPoints = np.zeros(shape=(nSim, 20))
    runWins = np.zeros(shape=(nSim, 20))
    runDraws = np.zeros(shape=(nSim, 20))
    runLoses = np.zeros(shape=(nSim, 20))
    runGF = np.zeros(shape=(nSim, 20))
    runGA = np.zeros(shape=(nSim, 20))
    runGD = np.zeros(shape=(nSim, 20))
    for i in range(nSim):
        #League Stats
        Points =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Wins = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Draws = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Loses = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        GF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        GA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        GD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                    GD[x] += homeScore - awayScore
                    GD[y] += awayScore - homeScore

        #Send data to average            
        runPoints[i] = Points
        runWins[i] = Wins
        runDraws[i] = Draws
        runLoses[i] = Loses
        runGF[i] = GF
        runGA[i] = GA
        runGD[i] = GD
    
        tablePoints = runPoints.sum(axis=0)/nSim
        tableWins = runWins.sum(axis=0)/nSim
        tableDraws = runDraws.sum(axis=0)/nSim
        tableLoses = runLoses.sum(axis=0)/nSim
        tableGF = runGF.sum(axis=0)/nSim
        tableGA = runGA.sum(axis=0)/nSim
        tableGD = runGD.sum(axis=0)/nSim

        #Rank
        for z in range(20):
            dataSet[z][2][0]= Points[z]
            dataSet[z][2][1]= Wins[z]
            dataSet[z][2][2]= Draws[z]
            dataSet[z][2][3]= Loses[z]
            dataSet[z][2][4]= GF[z]
            dataSet[z][2][5]= GA[z]
            dataSet[z][2][7]= GD[z]
        
        sortedTeamsRun = sorted(dataSet, key=lambda x: x[2][0], reverse=True)

        for w in range(20):
            sortedTeamsRun[w][2][6]= w+1
            if sortedTeamsRun[w][0][0] == team:
                myTeamPosRun[i] = sortedTeamsRun[w][2][6]
                myTeamPointsRun[i] = sortedTeamsRun[w][2][0]
            elif sortedTeamsRun[w][0][0] == 'Manchester City':
                MCPosRun[i] = sortedTeamsRun[w][2][6]
                MCPointsRun[i] = sortedTeamsRun[w][2][0]

    for x in range(20):
        dataSet[x][1][0]= round(tablePoints[x], 1)
        dataSet[x][1][1]= round(tableWins[x], 1)
        dataSet[x][1][2]= round(tableDraws[x], 1)
        dataSet[x][1][3]= round(tableLoses[x], 1)
        dataSet[x][1][4]= round(tableGF[x], 1)
        dataSet[x][1][5]= round(tableGA[x], 1)
        dataSet[x][1][7]= round(tableGD[x], 1)

    #League Table
    sortedTeams = sorted(dataSet, key=lambda x: x[1][0], reverse=True)

    print("| RANK | TEAM             | POINTS |  WINS  | DRAWS | LOSSES | GOALS FOR | GOALS AGAINST | GOAL DIFF. |")
    for x in range(20):
        sortedTeams[x][1][6]= x+1
        print("| ",x+1," "*(2 - len(str(sortedTeams[x][1][6]))),'|', sortedTeams[x][0][0]," "*(15 - len(sortedTeams[x][0][0])),'| ', sortedTeams[x][1][0]," "*(4 - len(str(sortedTeams[x][1][0]))),'| ', sortedTeams[x][1][1]," "*(4 - len(str(sortedTeams[x][1][1]))),'|', sortedTeams[x][1][2]," "*(4 - len(str(sortedTeams[x][1][2]))),'| ', sortedTeams[x][1][3]," "*(4 - len(str(sortedTeams[x][1][3]))),'|   ', sortedTeams[x][1][4]," "*(5 - len(str(sortedTeams[x][1][4]))),"|    ", sortedTeams[x][1][5]," "*(8 - len(str(sortedTeams[x][1][5]))),"|   ", sortedTeams[x][1][7]," "*(6 - len(str(sortedTeams[x][1][7]))),"|")
    print('===============================')
    print('Probabilidad de que', team, 'quede en el Top 4 =', np.sum(myTeamPosRun < 5)/nSim)
    print('===============================')
    print('Plots')
    print('===============================')

    fig, ax1 = plt.subplots()
    color = 'tab:green'
    ax1.set_xlabel('Simulations')
    ax1.set_ylabel('Points', color=color)
    ax1.plot(myTeamPointsRun, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


    color = 'tab:blue'

    ax2.set_ylabel('Position', color=color)  # we already handled the x-label with ax1
    ax2.plot(myTeamPosRun,"o",color=color)
    ax2.invert_yaxis()
    ax2.tick_params(axis='y', labelcolor=color,)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

    #Create the bare bones of what will be our visualisation
    fig, ax = plt.subplots()

    myTeamPointsCumulative = np.zeros(len(myTeamPointsRun))
    for i in range(len(myTeamPointsRun)):
        myTeamPointsCumulative[i] = myTeamPointsCumulative[i-1] + myTeamPointsRun[i]

    MCPointsCumulative = np.zeros(len(MCPointsRun))
    for i in range(len(MCPointsRun)):
        MCPointsCumulative[i] = MCPointsCumulative[i-1] + MCPointsRun[i]

    #Add our data as before, but setting colours and widths of lines
    plt.plot(myTeamPointsCumulative, color="#231F20", linewidth=2)
    plt.plot(MCPointsCumulative, color="#6CABDD", linewidth=2)

    #Give the axes and plot a title each
    plt.xlabel('Sims')
    plt.ylabel('Points')
    plt.title('Team v Man City Running Total Points')

    #Add a faint grey grid
    plt.grid()
    ax.xaxis.grid(color="#F8F8F8")
    ax.yaxis.grid(color="#F9F9F9")

    #Remove the margins between our lines and the axes
    plt.margins(x=0, y=0)

    #Remove the spines of the chart on the top and right sides
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    #Create the bare bones of what will be our visualisation
    fig, ax = plt.subplots()

    #Add our data as before, but setting colours and widths of lines
    plt.plot(myTeamPointsRun, color="#231F20", linewidth=2)
    plt.plot(MCPointsRun, color="#6CABDD", linewidth=2)

    #Give the axes and plot a title each
    plt.xlabel('Sims')
    plt.ylabel('Points')
    plt.title('Team v Man City Points Per Sim')

    #Add a faint grey grid
    plt.grid()
    ax.xaxis.grid(color="#F8F8F8")
    ax.yaxis.grid(color="#F9F9F9")

    #Remove the margins between our lines and the axes
    plt.margins(x=0, y=0)

    #Remove the spines of the chart on the top and right sides
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    

#Funcion traer own team
MyTeamPlayers = []
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
    #RESET VARIABLES
    global MyStartingXI_xG, MyStartingXI_SoT, MyStartingXI_KP, MyStartingXI_CMP, MyStartingXI_TKL, MyStartingXI_B, MyStartingXI_SP, MyFWPlayers, MyMFFWPlayers, MyMFPlayers, MyDFPlayers, MyGKPlayers
    MyTeamPlayers = []
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
    
    #All My Players
    df_all_players = pd.DataFrame(pl_players_stats_skills,  columns=['Player','Squad'])
    for i in range(532):
        Squad = df_all_players.at[i, 'Squad']
        if Squad == teamname:
            MyTeamPlayers.append(df_all_players.loc[i])
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
    print('Optimal Starting XI:', MyStartingXI)
    MyStartingXI_xG = sum(xGToReplace)
    MyStartingXI_SoT = sum(SoTToReplace)
    MyStartingXI_KP = sum(KPToReplace)
    MyStartingXI_CMP = sum(CMPToReplace)/len(CMPToReplace)
    MyStartingXI_TKL = sum(TKLToReplace)
    MyStartingXI_B = sum(BToReplace)
    MyStartingXI_SP = sum(SPToReplace)
    createPitch(MyStartingXI,d,m,ma,f)


#Funcion Merge Players to buy & optimizacion
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

myTeamxG = 0
myTeamSoT = 0 
myTeamKP = 0 
myTeamCP = 0
myTeamxGA = 0
myTeamT = 0
myTeamB = 0
myTeamSP = 0

def myNewTeam(teamname,money,d,m,ma,f):
    #RESET VARIABLES
    global FWPlayers, MFFWPlayers, MFPlayers, DFPlayers, GKPlayers, MyNewStartingXI, MyNewPlayers_xG, MyNewPlayers_SoT, MyNewPlayers_KP, MyNewPlayers_CMP, MyNewPlayers_TKL, MyNewPlayers_B, MyNewPlayers_SP, myTeamxG, myTeamSoT, myTeamKP, myTeamCP, myTeamxGA, myTeamT, myTeamB, myTeamSP
    FWPlayers = []
    MFFWPlayers = []
    MFPlayers = []
    DFPlayers = []
    GKPlayers = []
    MyNewStartingXI= []
    MyNewPlayers_xG = 0 
    MyNewPlayers_SoT = 0 
    MyNewPlayers_KP = 0 
    MyNewPlayers_CMP = 0 
    MyNewPlayers_TKL = 0 
    MyNewPlayers_B = 0 
    MyNewPlayers_SP = 0 
    
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
    print('New Optimal Starting XI', MyNewStartingXI)
    createPitch(MyNewStartingXI,d,m,ma,f)
    MyNewPlayers_xG = sum(xGNew)
    MyNewPlayers_SoT = sum(SoTNew)
    MyNewPlayers_KP = sum(KPNew)
    MyNewPlayers_CMP = sum(CMPNew)
    MyNewPlayers_TKL = sum(TKLNew)
    MyNewPlayers_B = sum(BNew)
    MyNewPlayers_SP = sum(SPNew)

    # Setear nuevo skillset del equipo
    df_teams = pd.DataFrame(team_stats_skills, columns=['Rk', 'Squad', 'xG','xGA','Save%','SoT','Tkl','Blocks','Cmp%','KP','Poss'])
    teamLocation = 0
    for i in range(len(df_teams)):
        Teami = df_teams.at[i, 'Squad']
        if Teami == teamname:
            teamLocation = i
    bestT = df_teams['Tkl'].max()
    bestB = df_teams['Blocks'].max() 
    bestSP = df_teams['Save%'].max()

    myTeamxG = df_teams.at[teamLocation, 'xG']
    myTeamSoT = df_teams.at[teamLocation, 'SoT'] 
    myTeamKP = df_teams.at[teamLocation, 'KP'] 
    myTeamCP = df_teams.at[teamLocation, 'Cmp%']
    #Defensive Stats
    myTeamxGA = df_teams.at[teamLocation, 'xGA']
    myTeamT = df_teams.at[teamLocation, 'Tkl']
    myTeamB = df_teams.at[teamLocation, 'Blocks']
    myTeamSP = df_teams.at[teamLocation, 'Save%']

    myTeamDef_T = ((myTeamT / bestT)*12.5)
    myTeamDef_B = ((myTeamB / bestB)*12.5)
    myTeamDef_SP = ((myTeamSP / bestSP)*25)

    #atk
    myTeamNew_xG = myTeamxG - MyStartingXI_xG + MyNewPlayers_xG
    myTeamNew_SoT = myTeamSoT - MyStartingXI_SoT + MyNewPlayers_SoT
    myTeamNew_KP = myTeamKP - MyStartingXI_KP + MyNewPlayers_KP
    myTeamNew_CP = (myTeamCP*len(MyTeamPlayers) + MyNewPlayers_CMP)/(len(MyTeamPlayers)+len(CMPNew))
    #dfc 
    myTeamNew_TKL = myTeamT - MyStartingXI_TKL + MyNewPlayers_TKL
    myTeamNew_B = myTeamB - MyStartingXI_B + MyNewPlayers_B
    myTeamNew_SP = MyNewPlayers_SP

    #New xGA Calc
    Comparison_Def_Base = myTeamDef_T + myTeamDef_B + myTeamDef_SP

    myTeamNew_Def_T2 = ((myTeamNew_TKL/myTeamT)-1)
    myTeamNew_Def_B2 = ((myTeamNew_B/myTeamB)-1)
    myTeamNew_Def_SP2 = ((myTeamNew_SP/myTeamSP)-1)

    New_Def_Base = myTeamDef_T*(1+myTeamNew_Def_T2) + myTeamDef_B*(1+myTeamNew_Def_B2) + myTeamDef_SP*(1+myTeamNew_Def_SP2)

    #New xGA
    Def_Mejora = (New_Def_Base/Comparison_Def_Base)-1
    myTeamxGA2 = myTeamxGA*(1-Def_Mejora)
    myTeamNew_xGA = myTeamxGA2

    #Import Data
    team_stats_skills.at[teamLocation,'xG']=myTeamNew_xG
    team_stats_skills.at[teamLocation,'SoT']=myTeamNew_SoT
    team_stats_skills.at[teamLocation,'KP']=myTeamNew_KP
    team_stats_skills.at[teamLocation,'Cmp%']=myTeamNew_CP
    team_stats_skills.at[teamLocation,'xGA']=myTeamNew_xGA
    team_stats_skills.at[teamLocation,'Tkl']=myTeamNew_TKL
    team_stats_skills.at[teamLocation,'Blocks']=myTeamNew_B
    team_stats_skills.at[teamLocation,'Save%']=myTeamNew_SP

    team_stats_skills.to_csv('new-league-stats-skill.csv',index=False)

    team_stats_skills.at[teamLocation,'xG']=myTeamxG
    team_stats_skills.at[teamLocation,'SoT']=myTeamSoT
    team_stats_skills.at[teamLocation,'KP']=myTeamKP
    team_stats_skills.at[teamLocation,'Cmp%']=myTeamCP
    team_stats_skills.at[teamLocation,'xGA']=myTeamxGA
    team_stats_skills.at[teamLocation,'Tkl']=myTeamT
    team_stats_skills.at[teamLocation,'Blocks']=myTeamB
    team_stats_skills.at[teamLocation,'Save%']=myTeamSP

#Combinacion Optimizaciones
def runTeamImprovement(team,money,d,m,ma,f):
    myTeam(team,d,m,ma,f)
    myNewTeam(team,money,d,m,ma,f)

# Funcion principal
def runSimulation(new, nSim, team, budget, d, m, ma, f):
    if new == False: 
        team_stats_skills = pd.read_csv('league-stats-skill.csv')
        defineSkills(team_stats_skills)
        runLeague(Teams, team, nSim)
    else:
        #Reset CSV
        team_stats_skills = pd.read_csv('league-stats-skill.csv')
        csvFile = 'new-league-stats-skill.csv'
        if os.path.exists(csvFile):
            os.remove(csvFile)
            print('CSV File deleted')
        defineSkills(team_stats_skills)
        print('=========================================================================================')
        print('Simulacion de Liga antes de comprar')
        print('=========================================================================================')
        print('xG Scatter Plot')
        print('===============================')
        scatter_xG(Skill)
        print('===============================')
        print('Resultados de la Liga')
        print('===============================')
        runLeague(Teams, team, nSim)
        runTeamImprovement(team, budget, d, m, ma, f)
        new_team_stats_skills = pd.read_csv('new-league-stats-skill.csv')
        defineSkills(new_team_stats_skills)
        print('=========================================================================================')
        print('Simulacion de Liga despues de comprar')
        print('=========================================================================================')
        print('xG Scatter Plot')
        print('===============================')
        scatter_xG(Skill)
        print('===============================')
        print('Resultados de la Liga')
        print('===============================')
        runLeague(Teams, team, nSim)

#%%
#PANEL DE CONTROL
# COMO USAR
# Reemplazar los valores de las variables con el modo, numero de simulaciones, equipo, presupuesto y formacion

# MODO
#False = Corre la liga sin cambios
#True = Corre la liga sin cambios, despues optimiza la compra de nuevos jugadores y vuelve a correr la liga con los cambios
GetNewTeam = True

# NUMERO DE SIMULACIONES
nSim = 1000

# EQUIPO
MyTeam = 'Leicester City'

# PRESUPUESTO (en millones)
Budget = 39.5

# FORMACION
# Disponible: (4,2,3,1 // 4,3,0,3 // 4,3,1,2)
Defenders = 4
Midfielders = 2
MidAttackers = 3
Forwards = 1


runSimulation(GetNewTeam, nSim, MyTeam, Budget, Defenders, Midfielders, MidAttackers, Forwards)