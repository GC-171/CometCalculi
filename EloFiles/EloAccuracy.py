import pandas as pd

Data = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\Elos.csv")
Matches = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

TeamNames = list(Data['Team'])
ELO = list(Data['EloRating'])
TeamRatings = dict(zip(TeamNames, ELO))

correct = 0
MatchupsPredicted = {
    'Home Team': [],
    'Away Team': [],
    'Predicted Result': [],
    'Actual Result': []
}

for i in range(len(Matches)):
    home_team = Matches.loc[i, 'HomeTeam']
    away_team = Matches.loc[i, 'AwayTeam']
    result = Matches.loc[i, 'Winner']

    home_rating = TeamRatings[home_team]
    away_rating = TeamRatings[away_team]

    elo_diff = abs(home_rating - away_rating)
    draw_threshold = 0

    if elo_diff < draw_threshold:
        predicted_winner = 'Draw'
    elif home_rating > away_rating:
        predicted_winner = 'Home'
    else:
        predicted_winner = 'Away'

    if predicted_winner == result:
        correct += 1

    MatchupsPredicted['Home Team'].append(home_team)
    MatchupsPredicted['Away Team'].append(away_team)
    MatchupsPredicted['Predicted Result'].append(predicted_winner)
    MatchupsPredicted['Actual Result'].append(result)

print("Number of Correct Predictions:", correct)

df = pd.DataFrame.from_dict(MatchupsPredicted)

df.to_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Documents\ELOResults.csv", index=False)
