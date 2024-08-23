import pandas as pd
from datetime import datetime

# Player name
player = 'PlotoZypresse'

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
        # Handling incorrect format or already formatted dates
        try:
            datetime.strptime(date_str, '%d/%m/%Y, %H:%M:%S')  # Check if it is already in the correct format
            return date_str
        except ValueError:
            return "Invalid date format"


def update_csv(input_csv, output_csv):
    #read csv file
    data = pd.read_csv(input_csv)

    

    # Filter the DataFrame for 'pathOfLegend' games
    pathOfLegends = 'pathOfLegend'
    filteredData = data.loc[data['type'] == pathOfLegends]

    # Extract columns from filtered data
    gamemode = filteredData['type']
    playerCrowns = filteredData['team_0_crowns']
    playerName = filteredData['team_0_name']
    opponentCrowns = filteredData['opponent_0_crowns']
    opponentName = filteredData['opponent_0_name']
    timeStamp = filteredData['battleTime']

    # Create a new DataFrame using a dictionary
    df = pd.DataFrame({
        'Game Mode': gamemode,
        'Player Crowns': playerCrowns,
        'Player Name': playerName,
        'Opponent Crowns': opponentCrowns,
        'Opponent Name': opponentName,
        'Battle Time': timeStamp
    })

    # determione winner of the game
    df['Winner'] = df.apply(
        lambda row: row['Player Name'] if row['Player Crowns'] > row['Opponent Crowns'] else row['Opponent Name'], axis=1
    )

    # convert battle time to readable format
    df['Battle Time'] = df['Battle Time'].apply(timeConvert)

    #load existing data from stats.csv or create a new dataframe
    try:
        existing_df = pd.read_csv(output_csv)
        if existing_df.empty:
            existing_df = pd.DataFrame() # Empty DataFrame if file is empty
        else:
            #ensure date format is the right format to compare
            existing_df['Battle Time'] = existing_df['Battle Time'].apply(timeConvert)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        existing_df = pd.DataFrame() #empty data frame if file is not found

    # find new entries
    if 'Battle Time' in existing_df.columns:
        new_entries = df[~df['Battle Time'].isin(existing_df['Battle Time'])]
    else:
        new_entries = df

    # append new entries to existing file or create
    if not existing_df.empty:
        combined_df = pd.concat([existing_df, new_entries], ignore_index=True)
    else:
        combined_df = new_entries

    # save combined data to stats.csv
    combined_df.to_csv(output_csv, index=False)

    print(combined_df)

def winPercent(player_name, stats_csv='stats.csv'):
    
    # load data
    df = pd.read_csv(stats_csv)

    #ensure right date format
    df['Battle Time'] = df['Battle Time'].apply(timeConvert)


    wins = df[df['Winner'] == player_name].shape[0]
    total_games = df.shape[0]
    win_percent = (wins / total_games)*100 if total_games > 0 else 0

    print(f"Win percentage for {player}: {win_percent:.2f}%")


update_csv('test2.csv', 'stats.csv')

winPercent(player)