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
lc_stats_skills = pd.read_csv('LC_player_stats.csv')
bundes_player_stats = pd.read_csv('bundesliga-players-stats.csv')

#Funciones de Graficos
#Dibujo de Cancha con jugadores
#Source: https://fcpython.com/visualisation/drawing-pitchmap-adding-lines-circles-matplotlib
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
    #TODO - Podriamos agregar que dependan de la formacion a traves de una variable if
    #Players
    playername = []
    tempName = []
    for i in range(len(playernames)):
        tempName.append(playernames[i].partition(" ")[2])
        playername.append(tempName[i].partition("\\")[0])

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
# TODO - Funciones de graficos 


# TODO - Funcion  Skills


# TODO -Funcion para simular la liga


# TODO - Funcion traer own team
def myTeam(teamname):
    #FW
    df_FW_players = pd.DataFrame(bundes_player_stats,  columns=['Player','Squad', '90s', 'Pos', 'xG', 'SoT', 'Price'])
    MyFWPlayers = []
    for i in range(505):
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
    df_MFFW_players = pd.DataFrame(bundes_player_stats, columns=['Player', 'Squad', '90s', 'Pos', 'xG', 'SoT', 'KP', 'Cmp%', 'Price'])
    MyMFFWPlayers = []
    for i in range(505):
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
    df_MF_players = pd.DataFrame(bundes_player_stats, columns=['Player', 'Squad', '90s', 'Pos', 'Tkl', 'Cmp%', 'KP', 'Price'])
    MyMFPlayers = []
    for i in range(505):
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
    df_DF_players = pd.DataFrame(bundes_player_stats, columns=['Player','Squad','90s', 'Pos', 'Tkl', 'Blocks', 'Cmp%', 'Price'])
    MyDFPlayers = []
    for i in range(505):
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
    df_GK_players = pd.DataFrame(bundes_player_stats, columns=['Player', 'Squad','90s', 'Pos', 'Save%', 'Price'])
    MyGKPlayers = []
    for i in range(27):
        Posi = df_GK_players.at[i, 'Pos']
        Squad = df_GK_players.at[i, 'Squad']
        if Posi == 'GK' and Squad == teamname:
            MyGKPlayers.append(df_GK_players.loc[i])
    SP_MyGK = []
    for i in range(len(MyGKPlayers)):
        SP_MyGK.append(MyGKPlayers[i][3])
    print(len(MyMFPlayers)+len(MyMFFWPlayers) +
          len(MyDFPlayers)+len(MyFWPlayers)+len(MyGKPlayers))
    return MyFWPlayers, MyMFFWPlayers, MyMFPlayers, MyDFPlayers, MyGKPlayers, xG_MyFW, SoT_MyFW, xG_MyMFFW, SoT_MyMFFW, KP_MyMFFW, CMP_MyMFFW, KP_MyMF, CMP_MyMF, TKL_MyMF, CMP_MyDF, TKL_MyDF, B_MyDF, SP_MyGK
# TODO - Funcion para optimizar starting XI


# TODO - Funcion Merge Players to buy 


team = 'Bayern Munich'
myTeam(team)
