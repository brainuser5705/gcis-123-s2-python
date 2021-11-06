import random

def get_players():

    with open("./players.txt") as file:
        return [player.strip() for player in file]

def get_random_player_number(player_list):

    return random.randrange(0, len(player_list)-1)

def create_teams(player_list, num_teams):

    teams = [] # set is not hashable
    players_per_team = len(player_list) // num_teams

    for _ in range(num_teams):

        current_team = set()
        teams.append(current_team)

        players_added = 0
        while players_added != players_per_team:
            player = player_list[get_random_player_number(player_list)]
            if (not is_already_recruited(teams, player)):
                current_team.add(player)
                players_added += 1

    return teams


def is_already_recruited(teams, player):
    for team in teams:
        if player in team:
            return True
    return False

def main():
    players = get_players()
    tournament = create_teams(players, 10)

    for team in tournament:
        print(len(team))

if __name__ == '__main__':
    main()