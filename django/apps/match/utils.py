
def get_rankings(matches)->list:
    """
    Given a list of matches, returns a dictionary of team names and 
    their respective ranks and points.

    Point Assign Logic: A draw (tie) is worth 1 point and a win is worth
    3 points. A loss is worth 0 points. 

    Ranking Logic:  If two or more teams have the same number of points,
    they should be ranked based on their points, and teams with the same
    number of points should be ordered alphabetically.

    Return: list of sorted ranks
    """
    team_records = {}

    # Loop through all the matches and update each team's points in the team_records dictionary
    for match in matches:
        winner = match.winner
        loser = match.loser
        if winner or loser: #win or lose case
            team_records[winner] = team_records.get(winner, 0) + 3
            team_records[loser] = team_records.get(loser, 0)
        else: # draw(tie) case
            team_records[match.team_1] = team_records.get(match.team_1, 0) + 1
            team_records[match.team_2] = team_records.get(match.team_2, 0) + 1

    # Sort the team_records dictionary based on both of points data and team name alphabetically
    sorted_records = sorted(team_records.items(), key=lambda x: (-x[1], x[0]))
    
    #assign a rank to each team
    return [
        {'rank': rank + 1, 'team': team[0], 'points': team[1]}
        for rank, team in enumerate(sorted_records)
    ]