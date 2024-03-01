import csv
import json

def calculate_averages(data):
    return [sum(column) / len(data) for column in zip(*data)]

def main():
    csv_file_path = r'C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv'
    
    ## PUT TEAM NAME HERE
    team_name = "WIC"

    columns_average = ["HomeScore","AwayScore","Home_xG", "Away_xG", "Home_shots", "Away_shots",
                          "Home_corner", "Away_corner", "Home_PK_Goal",
                          "Away_PK_Goal", "Home_PK_shots", "Away_PK_shots",
                          "Home_ToP"]

    with open(csv_file_path, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)

        indices = {column: header.index(column) for column in columns_average}
        home_team_index = header.index('HomeTeam')
        away_team_index = header.index('AwayTeam')

        home_data = [[float(row[indices[column]]) for column in columns_average] 
                     for row in reader if row[home_team_index] == team_name]

        file.seek(0)
        next(reader) 

        away_data = [[float(row[indices[column]]) for column in columns_average] 
                     for row in reader if row[away_team_index] == team_name]

    if not home_data:
        print(f"Type the name correctly pls '{team_name}'.")
    else:
        home_averages = calculate_averages(home_data)

        home_dict = {
            'Home': {
                'HomeScore': home_averages[0],
                'AwayScore': home_averages[1],
                'Home_xG': home_averages[2],
                'Away_xG': home_averages[3],
                'Home_shots': home_averages[4],
                'Away_shots': home_averages[5],
                'Home_corner': home_averages[6],
                'Away_corner': home_averages[7],
                'Home_PK_Goal': home_averages[8],
                'Away_PK_Goal': home_averages[9],
                'Home_PK_shots': home_averages[10],
                'Away_PK_shots': home_averages[11],
                'Home_ToP': home_averages[12],
                'Home_GS_percentage': home_averages[0] / home_averages[4] if home_averages[4] != 0 else 0,
                'Away_GS_percentage': home_averages[1] / home_averages[5] if home_averages[5] != 0 else 0,
            }
        }

    if not away_data:
        print(f"No away data found for team '{team_name}'.")
    else:
        away_averages = calculate_averages(away_data)

        away_dict = {
            'Away': {
                'HomeScore': away_averages[0],
                'AwayScore': away_averages[1],
                'Home_xG': away_averages[2],
                'Away_xG': away_averages[3],
                'Home_shots': away_averages[4],
                'Away_shots': away_averages[5],
                'Home_corner': away_averages[6],
                'Away_corner': away_averages[7],
                'Home_PK_Goal': away_averages[8],
                'Away_PK_Goal': away_averages[9],
                'Home_PK_shots': away_averages[10],
                'Away_PK_shots': away_averages[11],
                'Home_ToP': away_averages[12],
                'Home_GS_percentage': away_averages[0] / away_averages[4] if away_averages[4] != 0 else 0,
                'Away_GS_percentage': away_averages[1] / away_averages[5] if away_averages[5] != 0 else 0,
            }
        }

    print(f"{team_name} = ")
    team_data = {
        'Home': home_dict['Home'],
        'Away': away_dict['Away']
    }
    print(json.dumps(team_data, indent=4))

if __name__ == "__main__":
    main()
