import streamlit as st
import pandas as pd
import os

file_path = "data/seasons_teams.json"

LEAGUES = ["LaLiga","Premier League"]


# players = 
def league_picker(league_name):
    # Loop through all files in the current directory
    
    for filename in os.listdir('data'):
        # Check if the file is a JSON file and matches the desired name pattern
        if filename.endswith('.json') and league_name.lower().split(" ")[0] in filename:
            # Open and read the file (you can modify this part based on what you want to do with the file)
            return  pd.read_json('data/'+filename)
        else:
            print(f"No JSON file with name containing '{league_name}' was found.")
            
col1, col2, col3, col4 = st.columns(4)

league_name = col1.selectbox('Select a Year', options=list(LEAGUES))

league = league_picker(league_name)

# Create a dropdown menu for selecting a year
year = col2.selectbox('Select a Year', options=list(league['season'].unique()))

# Create a dropdown menu for selecting a team from the selected year
team = col3.selectbox('Select a Team', options=league[league['season'] == year]['name'])


player_stats = pd.DataFrame()

for filename in os.listdir('data/stats'):
        # Check if the file is a JSON file and matches the desired name pattern
        if filename.endswith('.json') and league_name.lower().split(" ")[0] in filename:
            # Open and read the file (you can modify this part based on what you want to do with the file)
            player_stats = pd.read_json('data/stats/'+filename)
        else:
            print(f"No JSON file with name containing '{league_name}' was found.")
        
player = col4.selectbox('Select a Player', options=player_stats[(player_stats["season"]==year) & (player_stats["teamName"]==team)]["fullName"].unique())

st.write(f'You selected {team} from {year}.')

st.write(player_stats[ (player_stats["fullName"]==player)])




