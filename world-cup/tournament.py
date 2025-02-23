# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000

def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # TODO: Read teams into memory from file

    teams = []

    file = sys.argv[1]
    with open(file, 'r') as csv_file:
        csv_DictReader_object = csv.DictReader(csv_file)
        for row in csv_DictReader_object:
            teams.append(dict(row))

    for team in teams:
        team['rating'] = int(team['rating'])

    counts = {}

    for k in teams:
        addteam = k['team']
        counts[addteam] = 0

    for x in range(0, N):
        result = simulate_tournament(teams)
        counts[result] += 1

    # TODO: Simulate N tournaments and keep track of win counts

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []


    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):

    x = len(teams)

    if(x > 8):
        teams = simulate_round(teams)
        x = len(teams)

    if(x==8):
        teams = simulate_round(teams)
        x = len(teams)

    if(x==4):
        teams = simulate_round(teams)
        x = len(teams)

    if(x==2):
        winner = simulate_round(teams)
        winningteam = winner[0]['team']
        return winningteam

    """Simulate a tournament. Return name of winning team."""

    # TODO


if __name__ == "__main__":
    main()
