import json
import requests 
import pandas as pd 
from datetime import datetime

start_time = datetime.now()

with open('./data/bundesliga_seasons_teams.json', 'r') as file:
    laliga_seasons_teams = json.load(file)

from tqdm import tqdm

years = [y for y in range(2001,2024)]

player_stats = []
defensive_stats = []
general_stats = []
offensive_stats = []
goalkeeping_stats = []

for idx,team in enumerate(laliga_seasons_teams):
    elapsed_time = datetime.now() - start_time



    if team['season']>=2003:
        print(f"\rProcessing team {idx + 1} out of {len(laliga_seasons_teams)}, Season {team['season']}. Elapsed Time: {elapsed_time}", end="\n", flush=True)
        
        url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/ger.1/seasons/"+str(team['season'])+"/teams/"+team['id']+"/athletes"
        resp = requests.get(url)
        data = resp.json()
        
        for item in data['items']:
            
            defensive_stat = {}
            general_stat = {}
            offensive_stat = {}
            goalkeeping_stat = {}

            resp = requests.get(item['$ref'])
            data = resp.json()
         
            weight = 0
            height = 0
            position = ''
            citizenship = ''
            try:
                weight =data["weight"]
            except:
                weight =None
            try:
                height =data["height"]
            except:
                height =None 

            try: 
                position = data['position']['name']
            except: 
                position =None

            try: 
                citizenship= data['citizenship']

            except: 
                citizenship = None
            try: 
                player_stat = {'id': data["id"],
                            "season":team['season'],      
                            "teamName":team['name'],
                            "fullName":data["fullName"],
                            "position":position,
                            "weight":weight,
                            "height":height,
                            "citizenship" : citizenship
                            }
            except: 
                print('#',end ='')
                continue
                        
            defensive_stat['id'] = data['id']
            defensive_stat['season'] = team['season']

            general_stat['id'] = data['id']
            general_stat['season'] = team['season']

            offensive_stat['id'] = data['id']
            offensive_stat['season'] = team['season']


            goalkeeping_stat['id'] = data['id']
            goalkeeping_stat['season'] = team['season']

            try:
                resp = requests.get(data['statistics']['$ref'])
                data_athlete_stats = resp.json()

                defensive = data_athlete_stats['splits']['categories'][0]
                for stat in defensive['stats']:
                    defensive_stat[stat['name']] = stat['value']

                general = data_athlete_stats['splits']['categories'][1]
                for stat in general['stats']:
                    general_stat[stat['name']] = stat['value']

                goalkeeping = data_athlete_stats['splits']['categories'][2]
                for stat in goalkeeping['stats']:
                    goalkeeping_stat[stat['name']] = stat['value']
                
                offensive = data_athlete_stats['splits']['categories'][3]
                for stat in offensive['stats']:
                    offensive_stat[stat['name']] = stat['value']

            except:
                print('*',end='')


            player_stats.append(player_stat)
            defensive_stats.append(defensive_stat)
            general_stats.append(general_stat)
            goalkeeping_stats.append(goalkeeping_stat)
            offensive_stats.append(offensive_stat)

            print(".",end="")
        print()


print(player_stats)
file_path = 'data/stats/bundesliga_player_stats.json'

# Open the file in write mode ('w') and write the JSON data
with open(file_path, 'w') as file:
    json.dump(player_stats, file)

print(defensive_stats)
file_path = 'data/stats/bundesliga_player_defensive_stats.json'

# Open the file in write mode ('w') and write the JSON data
with open(file_path, 'w') as file:
    json.dump(defensive_stats, file)

print(goalkeeping_stats)
file_path = 'data/stats/bundesliga_player_goalkeeping_stats.json'

# Open the file in write mode ('w') and write the JSON data
with open(file_path, 'w') as file:
    json.dump(goalkeeping_stats, file)

print(offensive_stats)
file_path = 'data/stats/bundesliga_player_offensive_stats.json'

# Open the file in write mode ('w') and write the JSON data
with open(file_path, 'w') as file:
    json.dump(offensive_stats, file)

print(general_stats)
file_path = 'data/stats/bundesliga_player_general_stats.json'

# Open the file in write mode ('w') and write the JSON data
with open(file_path, 'w') as file:
    json.dump(general_stats, file)
