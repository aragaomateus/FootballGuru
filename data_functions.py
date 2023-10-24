import pandas as pd 
# import json
# import requests

PREMIER_LEAGUE_PLAYER_INFO = pd.read_json('./data/stats/premier_league/premier_player_stats.json')

PREMIER_LEAGUE_GENERAL_STATS = pd.read_json('./data/stats/premier_league/premier_player_general_stats.json')

PREMIER_LEAGUE_GOALKEEPING_STATS= pd.read_json('./data/stats/premier_league/premier_player_goalkeeping_stats.json')

PREMIER_LEAGUE_OFFENSIVE_STATS = pd.read_json('./data/stats/premier_league/premier_player_offensive_stats.json')

PREMIER_LEAGUE_DEFENSIVE_STATS = pd.read_json('./data/stats/premier_league/premier_player_defensive_stats.json')



def premier_goalkeeping_stats(season=None, team=None) -> pd.DataFrame:
    premier_league_goalkeepers = PREMIER_LEAGUE_PLAYER_INFO[PREMIER_LEAGUE_PLAYER_INFO['position']=='Goalkeeper']
    if season == None and team==None: 
        result_df =  premier_league_goalkeepers.merge(PREMIER_LEAGUE_GOALKEEPING_STATS, on=['id', 'season'], how='inner').drop_duplicates()
        return result_df
    elif season != None and team ==None:
        player_info_filtered = premier_league_goalkeepers[premier_league_goalkeepers['season']==season]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_GOALKEEPING_STATS, on=['id'], how='inner').drop_duplicates()
        return result_df
    elif season == None and team !=None:
        player_info_filtered = premier_league_goalkeepers[premier_league_goalkeepers['teamName']==team]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_GOALKEEPING_STATS, on=['id','season'], how='inner').drop_duplicates()
        return result_df
    else: 
        player_info_filtered = premier_league_goalkeepers[(premier_league_goalkeepers['teamName']==team)&(premier_league_goalkeepers['season']==season) ]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_GOALKEEPING_STATS, on=['id','season'], how='inner').drop_duplicates()
        return result_df

def premier_defense_stats(season=None, team=None) -> pd.DataFrame:
    premier_league_defender = PREMIER_LEAGUE_PLAYER_INFO[PREMIER_LEAGUE_PLAYER_INFO['position']=='Defender']
    if season == None and team==None: 
        result_df =  premier_league_defender.merge(PREMIER_LEAGUE_DEFENSIVE_STATS, on=['id', 'season'], how='inner').drop_duplicates()
        return result_df
    elif season != None and team ==None:
        player_info_filtered = premier_league_defender[premier_league_defender['season']==season]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_DEFENSIVE_STATS, on=['id'], how='inner').drop_duplicates()
        return result_df
    elif season == None and team !=None:
        player_info_filtered = premier_league_defender[premier_league_defender['teamName']==team]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_DEFENSIVE_STATS, on=['id','season'], how='inner').drop_duplicates()
        return result_df
    else: 
        player_info_filtered = premier_league_defender[(premier_league_defender['teamName']==team)&(premier_league_defender['season']==season) ]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_DEFENSIVE_STATS, on=['id','season'], how='inner').drop_duplicates()
        return result_df

def premier_offensive_stats(season=None, team=None) -> pd.DataFrame:
    premier_league_offensive = PREMIER_LEAGUE_PLAYER_INFO[(PREMIER_LEAGUE_PLAYER_INFO['position']=='Forward') | (PREMIER_LEAGUE_PLAYER_INFO['position']=='Midfielder') ]
    if season == None and team==None: 
        result_df =  premier_league_offensive.merge(PREMIER_LEAGUE_OFFENSIVE_STATS, on=['id', 'season'], how='inner').drop_duplicates()
        return result_df
    elif season != None and team ==None:
        player_info_filtered = premier_league_offensive[premier_league_offensive['season']==season]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_OFFENSIVE_STATS, on=['id'], how='inner').drop_duplicates()
        return result_df
    elif season == None and team !=None:
        player_info_filtered = premier_league_offensive[premier_league_offensive['teamName']==team]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_OFFENSIVE_STATS, on=['id','season'], how='inner').drop_duplicates()
        return result_df
    else: 
        player_info_filtered = premier_league_offensive[(premier_league_offensive['teamName']==team)&(premier_league_offensive['season']==season) ]
        result_df =  player_info_filtered.merge(PREMIER_LEAGUE_OFFENSIVE_STATS, on=['id','season'], how='inner').drop_duplicates()
        return result_df


print(premier_offensive_stats())