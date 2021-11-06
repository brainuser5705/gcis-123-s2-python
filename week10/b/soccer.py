import random

def get_players():
    """
    Creates a list of the players from the `players.txt` file.
    """
    # TODO:
    # Use list comprehension
    with open("players.txt") as p:
     players = [x.strip() for x in p]

    return players

def get_random_player_number(player_list):
    """
    Gets a random index from the player list
    :param: player_list - the player list to choose from
    """
    return random.randrange(0, len(player_list)-1)

def create_teams(player_list, num_teams):
    """
    Creates a list of sets representing the teams. Each team
    has a unique set of players
    :param: player_list - the player list to choose from
    :param: num_teams - number of teams to make
    """
    
    teams = []
    # TODO:
    ppt = len(player_list)//num_teams
    
    for i in range(num_teams):

        st = set()
        teams.append(st)

        count = 0
        while count != ppt:
            rand = get_random_player_number(player_list)
            if is_already_recruited(teams,player_list[rand]) == False:
                st.add(player_list[rand])
                count += 1

    return teams


def is_already_recruited(teams, player):
    """
    Determine if player is already in one of the teams
    :param: teams - the teams already made
    :param: player - the player to check
    """
    # TODO: 

    for i in teams:
        if player in i:
            return True
    return False


def main():
    players = get_players()
    #print(players)
    tournament = create_teams(players, 10)

    for team in tournament:
         print(len(team))

if __name__ == '__main__':
    main()