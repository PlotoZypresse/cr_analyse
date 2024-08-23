import pandas as pd
from datetime import datetime

#read csv file
data = pd.read_csv('cr_gameData.csv')

# Player name
player = 'PlotoZypresse'

# Filter the DataFrame for 'pathOfLegend' games
pathOfLegends = 'pathOfLegend'
filteredData = data.loc[data['type'] == pathOfLegends]

gamemode = filteredData['type']
playerCrowns = filteredData['team_0_crowns']
playerName = filteredData['team_0_name']
opponentCrowns = filteredData['opponent_0_crowns']
opponentName = filteredData['opponent_0_name']
timeStamp = filteredData['battleTime']

def winPercent(player_name):
    wins = df[df['Winner'] == player_name].shape[0]
    total_games = df.shape[0]
    win_percent = (wins / total_games)*100 if total_games > 0 else 0
    return win_percent

def timeConvert(date_str):
    """
    Converts a date time string of format YYYYMMDDTHHMMSS to 
    YYYY-MM-DD HH:MM:SS
    """
    try:   
        # Remove the 'Z' from the string if present
        date_str = date_str.rstrip('Z')

        date_obj = datetime.strptime(date_str, '%Y%m%dT%H%M%S.%f')
        readable_date = date_obj.strftime('%d/%m/%Y, %H:%M:%S')
        return readable_date
    except ValueError:
        return "Invalid date format"


# Create a new DataFrame using a dictionary
df = pd.DataFrame({
    'Game Mode': gamemode,
    'Player Crowns': playerCrowns,
    'Player Name': playerName,
    'Opponent Crowns': opponentCrowns,
    'Opponent Name': opponentName,
    'Battle Time': timeStamp
})

df['Winner'] = df.apply(
    lambda row: row['Player Name'] if row['Player Crowns'] > row['Opponent Crowns'] else row['Opponent Name'], axis=1
)

df['Battle Time'] = df['Battle Time'].apply(timeConvert)



# print data
print(df)

print(f"Win percentage for {player}: {winPercent(player):.2f}%")

df.to_csv("stats.csv", index=False)