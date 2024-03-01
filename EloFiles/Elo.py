import math
import pandas as pd

df = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

TeamsTemp = [
    'PRO', 'FOR', 'SJU', 'FAR', 'DOV', 'ALB', 'SAS', 'CHM', 'TOL', 'REN',
    'SFS', 'TUC', 'LRO', 'ANC', 'WIC', 'LAR', 'LEX', 'TAC', 'DES', 'BAK',
    'EUG', 'MAN', 'JAC', 'MOB', 'BOI', 'AUG', 'SPR', 'OAK'
]
Teams = {team: {'EloRating': 1000} for team in TeamsTemp}

HomeTeam = list(df['HomeTeam'])
AwayTeam = list(df['AwayTeam'])
Result = list(df['Winner'])

def Probability(rating1, rating2):
    return 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating2 - rating1) / 400))

def EloRating(Ra, Rb, K, d):
    Pb = Probability(Ra, Rb)
    Pa = Probability(Rb, Ra)
    if d == 1:
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
    return Ra, Rb

for i in range(len(df)):
    home_team = HomeTeam[i]
    away_team = AwayTeam[i]
    result = Result[i]

    Ra = Teams[home_team]['EloRating']
    Rb = Teams[away_team]['EloRating']

    if result == 'Home':
        Ra, Rb = EloRating(Ra, Rb, 50, 1)
    elif result == 'Away':
        Ra, Rb = EloRating(Ra, Rb, 50, 0)
    elif result == 'Draw':
        Ra, Rb = EloRating(Ra, Rb, 25, 1 if Ra < Rb else 0)

    Teams[home_team]['EloRating'] = Ra
    Teams[away_team]['EloRating'] = Rb

df_elo = pd.DataFrame.from_dict(Teams, orient='index')

df_elo.reset_index(inplace=True)
df_elo.rename(columns={'index': 'Team'}, inplace=True)

df_elo.to_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\Elos.csv", index=False)

