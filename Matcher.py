import csv
from Dictionary import *

def main():
    csv_file_path = r'C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Documents\NSL_Group_Round_Games - NSL_Group_Round_Games.csv'

    updated_data = update_csv_data(csv_file_path)

    write_updated_data(csv_file_path, updated_data)

def update_csv_data(csv_file_path):

    HomeTeam = EUG
    HomeTeamName = 'EUG'

    AwayTeam = SJU
    AwayTeamName = 'SJU'

    match_data = calculate_match_averages(HomeTeam, AwayTeam)

    updated_data = []
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['HomeTeam'] == HomeTeamName and row['AwayTeam'] == AwayTeamName:
                row['Home_xG'] = match_data['match_home_xG']
                row['Away_xG'] = match_data['match_away_xG']
                row['Home_shots'] = match_data['match_home_shots']
                row['Away_shots'] = match_data['match_away_shots']
                row['Home_corner'] = match_data['match_home_corner']
                row['Away_corner'] = match_data['match_away_corner']
                row['Home_PK_Goal'] = match_data['match_home_PK_Goal']
                row['Away_PK_Goal'] = match_data['match_away_PK_Goal']
                row['Home_PK_shots'] = match_data['match_home_PK_shots']
                row['Away_PK_shots'] = match_data['match_away_PK_shots']
                row['Home_ToP'] = match_data['match_home_ToP']
                row['Home_GS_percentage'] = match_data['match_home_GS_percentage']
                row['Away_GS_percentage'] = match_data['match_away_GS_percentage']
            updated_data.append(row)
    return updated_data

def calculate_match_averages(HomeTeam, AwayTeam):
    home_home_xG = HomeTeam["Home"]["Home_xG"]
    away_home_xG = AwayTeam["Away"]["Home_xG"]
    home_away_xG = HomeTeam["Home"]["Away_xG"]
    away_away_xG = AwayTeam["Away"]["Away_xG"]

    home_home_shots = HomeTeam["Home"]["Home_shots"]
    away_home_shots = AwayTeam["Away"]["Home_shots"]
    home_away_shots = HomeTeam["Home"]["Away_shots"]
    away_away_shots = AwayTeam["Away"]["Away_shots"]

    home_home_corner = HomeTeam["Home"]["Home_corner"]
    away_home_corner = AwayTeam["Away"]["Home_corner"]
    home_away_corner = HomeTeam["Home"]["Away_corner"]
    away_away_corner = AwayTeam["Away"]["Away_corner"]

    home_home_PK_Goal = HomeTeam["Home"]["Home_PK_Goal"]
    away_home_PK_Goal = AwayTeam["Away"]["Home_PK_Goal"]
    home_away_PK_Goal = HomeTeam["Home"]["Away_PK_Goal"]
    away_away_PK_Goal = AwayTeam["Away"]["Away_PK_Goal"]

    home_home_PK_shots = HomeTeam["Home"]["Home_PK_shots"]
    away_home_PK_shots = AwayTeam["Away"]["Home_PK_shots"]
    home_away_PK_shots = HomeTeam["Home"]["Away_PK_shots"]
    away_away_PK_shots = AwayTeam["Away"]["Away_PK_shots"]

    home_home_ToP = HomeTeam["Home"]["Home_ToP"]
    home_home_GS_percentage = HomeTeam["Home"]["Home_GS_percentage"]
    away_home_GS_percentage = AwayTeam["Away"]["Home_GS_percentage"]

    away_away_ToP = AwayTeam["Away"]["Home_ToP"]
    home_away_GS_percentage = HomeTeam["Home"]["Away_GS_percentage"]
    away_away_GS_percentage = AwayTeam["Away"]["Away_GS_percentage"]   

    match_home_xG = (home_home_xG + away_home_xG) / 2
    match_away_xG = (home_away_xG + away_away_xG) / 2
    match_home_shots = (home_home_shots + away_home_shots) / 2
    match_away_shots = (home_away_shots + away_away_shots) / 2
    match_home_corner = (home_home_corner + away_home_corner) / 2
    match_away_corner = (home_away_corner + away_away_corner) / 2
    match_home_PK_Goal = (home_home_PK_Goal + away_home_PK_Goal) / 2
    match_away_PK_Goal = (home_away_PK_Goal + away_away_PK_Goal) / 2
    match_home_PK_shots = (home_home_PK_shots + away_home_PK_shots) / 2
    match_away_PK_shots = (home_away_PK_shots + away_away_PK_shots) / 2
    match_home_ToP = (home_home_ToP + away_away_ToP) / 2
    match_home_GS_percentage = (home_home_GS_percentage + away_home_GS_percentage) / 2
    match_away_GS_percentage = (home_away_GS_percentage + away_away_GS_percentage) / 2

    return {
        'match_home_xG': match_home_xG,
        'match_away_xG': match_away_xG,
        'match_home_shots': match_home_shots,
        'match_away_shots': match_away_shots,
        'match_home_corner': match_home_corner,
        'match_away_corner': match_away_corner,
        'match_home_PK_Goal': match_home_PK_Goal,
        'match_away_PK_Goal': match_away_PK_Goal,
        'match_home_PK_shots': match_home_PK_shots,
        'match_away_PK_shots': match_away_PK_shots,
        'match_home_ToP': match_home_ToP,
        'match_home_GS_percentage': match_home_GS_percentage,
        'match_away_GS_percentage': match_away_GS_percentage
    }

def write_updated_data(csv_file_path, updated_data):
    with open(csv_file_path, 'w', newline='') as file:
        fieldnames = updated_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)

if __name__ == "__main__":
    main()
