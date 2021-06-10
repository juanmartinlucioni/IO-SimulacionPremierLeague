#%%
import math, random
# HIGHER RATED TEAM
higher = 1.148698355
# LOWER RATED TEAM
lower = 0.8705505633


# DEFINING THE TEAM CLASS
class Team:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.points = self.gf = self.ga = self.wins = self.draws = self.losses = 0

    def add_goals(self, goals):
        self.gf += goals


# INITIALISING ALL OF THE TEAMS - NAMES AND SKILL LEVELS
arsenal = Team("Arsenal", 16)
aston_villa = Team("Aston Villa", 6)
bournemouth = Team("AFC Bournemouth", 8)
brighton = Team("Brighton and Hove Albion", 5)
burnley = Team("Burnley", 4)
chelsea = Team("Chelsea", 17)
crystal_palace = Team("Crystal Palace", 11)
everton = Team("Everton", 14)
leicester = Team("Leicester City", 12)
liverpool = Team("Liverpool", 19)
man_city = Team("Manchester City", 20)
man_united = Team("Manchester United", 15)
newcastle = Team("Newcastle United", 3)
norwich = Team("Norwich City", 2)
sheffield_united = Team("Sheffield United", 1)
southampton = Team("Southampton", 7)
tottenham = Team("Tottenham Hotspur", 18)
watford = Team("Watford", 9)
west_ham = Team("West Ham United", 10)
wolves = Team("Wolverhampton Wanderers", 13)

# HOME/AWAY TEAMS FOR PLAYING EACH TIME AGAINST EACH OTHER
teams = [arsenal, aston_villa, bournemouth, brighton, burnley, chelsea,
         crystal_palace, everton, leicester, liverpool, man_city, man_united,
         newcastle, norwich, sheffield_united, southampton, tottenham, watford,
         west_ham, wolves]

# PRINT ALL TEAMS' NAME AND SKILL
for team in teams:
    print(team.name, team.skill)

# RANDOM SYSTEM FOR HOME GOALS
def home_score(home, away):
    homeSkill = home.skill / 3
    awaySkill = away.skill / 3

    if homeSkill == awaySkill:
        raise ValueError

    if homeSkill > awaySkill:
        homeGoals = 0
        lambHome = higher ** (homeSkill - awaySkill)
        z = random.random()
        while z > 0:
            z = z - (((lambHome ** homeGoals) * math.exp(-1 * lambHome)) /
                     math.factorial(homeGoals))
            homeGoals += 1
        return (homeGoals - 1)

    if homeSkill < awaySkill:
        homeGoals = 0
        lambHome = higher ** (homeSkill - awaySkill)
        z = random.random()
        while z > 0:
            z = z - (((lambHome ** homeGoals) * math.exp(-1 * lambHome)) /
                     math.factorial(homeGoals))
            homeGoals += 1

        return (homeGoals - 1)

# RANDOM SYSTEM FOR AWAY GOALS
def away_score(home, away):
    homeSkill = home.skill / 3
    awaySkill = away.skill / 3

    if homeSkill == awaySkill:
        return "Teams cannot play themselves!!!"

    if awaySkill > homeSkill:
        awayGoals = 0
        lambAway = lower ** (homeSkill - awaySkill)
        x = random.random()
        while x > 0:
           x = x - (((lambAway ** awayGoals) * math.exp(-1 * lambAway)) /
                    math.factorial(awayGoals))
           awayGoals += 1
        return (awayGoals - 1)

    if awaySkill < homeSkill:
        awayGoals = 0
        lambAway = lower ** (homeSkill - awaySkill)
        x = random.random()
        while x > 0:
           x = x - (((lambAway ** awayGoals) * math.exp(-1 * lambAway)) /
                    math.factorial(awayGoals))
           awayGoals += 1
        return (awayGoals - 1)

# LEAGUE SIZE AND SETTING UP THE LEAGUE
league_size = 20
POINTS = []
GOALS_FOR = []
GOALS_AGAINST = []
WINS =[]
DRAWS = []
LOSSES = []
for x in range(league_size):
    POINTS += [0]
    GOALS_FOR += [0]
    GOALS_AGAINST += [0]
    WINS += [0]
    DRAWS += [0]
    LOSSES += [0]

# PLAYING ALL TEAMS AGAINST EACH OTHER AND UPDATING STATISTICS
for x in range(league_size):
    print("========================================")
    print(teams[x].name + "'s home games: ")
    print("========================================")
    for y in range(league_size):
        error = 0
        try:
            homeScore = home_score(teams[x], teams[y])
        except ValueError:
            pass
            error += 1
        try:
            awayScore = away_score(teams[x], teams[y])
        except ValueError:
            pass
        if error == 0:
            print(teams[x].name, homeScore, ":", awayScore, teams[y].name)
            GOALS_FOR[x] += homeScore
            GOALS_FOR[y] += awayScore
            GOALS_AGAINST[x] += awayScore
            GOALS_AGAINST[y] += homeScore
            if homeScore > awayScore:
                WINS[x] += 1
                LOSSES[y] += 1
                POINTS[x] += 3
            elif homeScore == awayScore:
                DRAWS[x] += 1
                DRAWS[y] += 1
                POINTS[x] += 1
                POINTS[y] += 1
            else:
                WINS[y] += 1
                LOSSES[x] += 1
                POINTS[y] += 3
        else:
            pass


# ASSIGNING STATISTICS TO EACH TEAM
for x in range(league_size):
    teams[x].points = POINTS[x]
    teams[x].gf = GOALS_FOR[x]
    teams[x].ga = GOALS_AGAINST[x]
    teams[x].wins = WINS[x]
    teams[x].draws = DRAWS[x]
    teams[x].losses = LOSSES[x]

sorted_teams = sorted(teams, key=lambda t: t.points, reverse=True)


# PRITNING THE FINAL LEAGUE TABLE
print("| TEAM                      | POINTS | WINS | DRAWS | LOSSES | GOALS FOR | GOALS AGAINST |")
for team in sorted_teams:
    print("|",team.name," "*(24 - len(team.name)),"|  ",team.points," "*(3 - len(str(team.points))),"| ",team.wins," "*(2 - len(str(team.wins))),"|  ",
          team.draws," "*(2 - len(str(team.draws))),"|  ",team.losses," "*(3 - len(str(team.losses))),"|    ",team.gf," "*(4 - len(str(team.gf))),"|     ",
          team.ga," "*(7 - len(str(team.ga))),"|")