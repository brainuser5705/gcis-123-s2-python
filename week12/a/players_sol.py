""" Practice Problems
"""

import csv

"""
Create a player class that has these following attributes:
name, goals, assists

Use slots, str and repr
"""
class Player:
    # Implement slots
    __slots__ = ['name', 'goals', 'assists']

    # Implement the constructor
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists


    """These functions are used to print out the string--either shorthand or full-- 
    representations of the objects

    print(team) or str(team) would print out the __str__ representation of the object

    repr(team) would print out the __repr__ representation
    """
    def __str__(self):
        return "Player{%s}" % (self.name)

    def __repr__(self):
        return "Player{name=%s, goals=%s, assists=%s}" % (self.name, self.goals, self.assists)

"""
Create a team class that has these following attributes:
a team number and an empty list of players

We do not want to start with a predefined list of players, so when
you are implementing this class, make sure that only team_num is passed
into the constructor but also contains the players attribute

^ The problem statement is pretty confusing so pls forgive me

Use slots, str and repr
"""
class Team:
    __slots__ = ['players', 'team_num']

    def __init__(self, team_num):
        self.team_num = team_num
        self.players = []

    def __str__(self):
        return "Team{%s}" % (self.team_num)

    def __repr__(self):
        return "Player{team_num=%s, players=%s}" % (self.team_num, self.players)


"""
Note: The solution to this problem has been given out. If you want to try to attempt
this on your own, please try not to look at the code and just get rid of it 

Create a function that reads from player.csv and adds 3 players to a Team.
Your function should return a list of 4 teams with 3 players on each team

Verify that each team is properly being added by running main

For this question, I suggest that you write pseudo code (mapping out how
you want the logic of the function to play out in plain words/steps) if you tend
to get stuck with long problems

# Hint: 
Once you create a new team, make sure you also include the player for the next team in
the current row 

Also make sure to cast the appropriate records when you create a new Player class if you
decide to implement the next function. It took us a long time to figure out because of the
semantic error hahahaha
"""
def create_team(filename):
    teams = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        
        num_team = 1
        new_team = Team(num_team)
        count_player = 0
        
        for record in reader:
            if (count_player == 3):
                teams.append(new_team)
                num_team += 1
                new_team = Team(num_team)
                count_player = 0
            player = Player(record[0], int(record[1]), int(record[2]))
            new_team.players.append(player)
            count_player += 1

        teams.append(new_team)
                            
    return teams



"""
Optional: Using the list of Teams, get the team that has the most
goals and return the team and total goals.

You should get the third team as the winning player with these players:
Robin van Persie,423,9
Andrea Pirlo,653,8
Yaya Toure,3,67

The num goals of the winning team should be (423 + 653 + 3) goals
"""
def get_winning_team(teams):
    
    winning_sum = 0
    winning_team = None

    for team in teams:
        team_sum = 0

        for player in team.players:
            team_sum += int(player.goals)

        if team_sum > winning_sum:
            winning_sum = team_sum
            winning_team = team
            
    return (winning_sum, winning_team)

def main():

    player = Player("Bobby St. Jacques", 2, 10)
    print(player)

    # Uncomment the docstring for testing out the Team class
    team = Team(2)
    team.players.append(player)
    print(repr(team))
    
    # Uncomment the docstring for testing out create_team
    teams = create_team("players.csv")
    
    print(len(teams))
    for team in teams:
        print("Team #" + str(team.team_num))

        for player in team.players:
            print("   - ", player)
        print()

    # Uncomment this if you want to test get_winning_team
    winning_sum, winning_team = get_winning_team(teams)
    
    print("Winning team with %s goals: Team #%s" % (winning_sum, winning_team.team_num))

    for players in winning_team.players:
        print(players)

main()