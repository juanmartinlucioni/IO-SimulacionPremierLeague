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
    #TODO - Podriamos agregar que dependan de la formacion a traves de una variable if
    #Players
    playername = []
    tempName = []
    # TODO - arreglar para nombres simples 'RODRI' 'FRED', no aparecen
    for i in range(len(playernames)):
        tempName.append(playernames[i].partition(" ")[2])
        playername.append(tempName[i].partition("\\")[0])
    if d == 4 and m == 3 and ma == 1 and f == 2 :
        print('formacion 4312')
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
        print('formacion 4231')
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
        print('formacion 4303')
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


# TODO - Funcion  Skills


# TODO -Funcion para simular la liga


# TODO - Funcion traer own team
def myTeam(teamname,d,m,ma,f):
    #FW
    df_FW_players = pd.DataFrame(pl_players_stats_skills,  columns=['Player','Squad', '90s', 'Pos', 'xG', 'SoT', 'Price'])
    MyFWPlayers = []
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
    MyMFFWPlayers = []
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
    MyMFPlayers = []
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
    MyDFPlayers = []
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
    MyGKPlayers = []
    for i in range(532):
        Posi = df_GK_players.at[i, 'Pos']
        GPi = df_GK_players.at[i, '90s']
        Squad = df_GK_players.at[i, 'Squad']
        if Posi == 'GK' and Squad == teamname and GPi > 10:
            MyGKPlayers.append(df_GK_players.loc[i])
    SP_MyGK = []
    for i in range(len(MyGKPlayers)):
        SP_MyGK.append(MyGKPlayers[i][4])
    print('suma =',len(MyMFPlayers)+len(MyMFFWPlayers) +
          len(MyDFPlayers)+len(MyFWPlayers)+len(MyGKPlayers))
    #Formacion
    formationDF = d
    formationMF = m
    formationMFFW = ma
    formationFW = f
    #LC Best XI
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
    MystartingXI = []

    for i in range(len(MyFWPlayers)):
        currentx = round(f[i])
        if currentx == 1:
            MystartingXI.append(MyFWPlayers[i][0])
            xGToReplace.append(MyFWPlayers[i][3])
            SoTToReplace.append(MyFWPlayers[i][4])
    for i in range(len(MyMFFWPlayers)):
        currenty = round(mffw[i])
        if currenty == 1:
            MystartingXI.append(MyMFFWPlayers[i][0])
            xGToReplace.append(MyMFFWPlayers[i][3])
            KPToReplace.append(MyMFFWPlayers[i][5])
            SoTToReplace.append(MyMFFWPlayers[i][4])
            CMPToReplace.append(MyMFFWPlayers[i][4])
    for i in range(len(MyMFPlayers)):
        currentz = round(mf[i])
        if currentz == 1:
            MystartingXI.append(MyMFPlayers[i][0])
            KPToReplace.append(MyMFPlayers[i][5])
            CMPToReplace.append(MyMFPlayers[i][4])
            TKLToReplace.append(MyMFPlayers[i][3])
    for i in range(len(MyDFPlayers)):
        currentw = round(df[i])
        if currentw == 1:
            MystartingXI.append(MyDFPlayers[i][0])
            CMPToReplace.append(MyDFPlayers[i][5])
            TKLToReplace.append(MyDFPlayers[i][3])
            BToReplace.append(MyDFPlayers[i][4])
    for i in range(len(MyGKPlayers)):
        currentv = round(gk[i])
        if currentv == 1:
            MystartingXI.append(MyGKPlayers[i][0])
            SPToReplace.append(MyGKPlayers[i][3])
    print(MystartingXI)
    createPitch(MystartingXI,d,m,ma,f)
    # MyStartingXI_xG = sum(xGToReplace)
    # MyStartingXI_SoT = sum(SoTToReplace)
    # MyStartingXI_KP = sum(KPToReplace)
    # MyStartingXI_CMP = sum(CMPToReplace)/len(CMPToReplace)
    # MyStartingXI_TKL = sum(TKLToReplace)
    # MyStartingXI_B = sum(BToReplace)
    # MyStartingXI_SP = sum(SPToReplace)
# TODO - Funcion para optimizar starting XI


# TODO - Funcion Merge Players to buy 


Team = 'Leicester City'
myTeam(Team,4,2,3,1)
# Team = 'Chelsea'
# myTeam(Team,4,2,3,1)
# Team = 'Liverpool'
# myTeam(Team,4,3,0,3)
# Team = 'Manchester City'
# myTeam(Team,4,3,0,3)
# Team = 'Manchester Utd'
# myTeam(Team,4,2,3,1)

#%%


