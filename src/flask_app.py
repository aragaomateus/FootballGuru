from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)

LEAGUES = ["LaLiga","Premier League"]

def league_picker(league_name):
    for filename in os.listdir('../data'):
        if filename.endswith('.json') and league_name.lower().split(" ")[0] in filename:
            return pd.read_json('../data/' + filename)
        
@app.route("/", methods=['GET', 'POST'])
def select_league():
    if request.method == 'POST':
        league_name = request.form.get('league_name')
        return redirect(url_for('select_year', league_name=league_name))
    return render_template('select_league.html', leagues=LEAGUES)

@app.route("/select_year/<league_name>", methods=['GET', 'POST'])
def select_year(league_name):
    league = league_picker(league_name)
    if request.method == 'POST':
        year = request.form.get('year')
        return redirect(url_for('select_team', league_name=league_name, year=year))
    return render_template('select_year.html', years=league['season'].unique(), league_name=league_name)

@app.route("/select_team/<league_name>/<year>", methods=['GET', 'POST'])
def select_team(league_name, year):
    league = league_picker(league_name)
    print(league,year)
    teams = league[league['season'] == int(year)]['name'].tolist()
    print(teams)
    if request.method == 'POST':
        team = request.form.get('team')
        return redirect(url_for('display_results', league_name=league_name, year=year, team=team))
    return render_template('select_team.html', teams=teams, league_name=league_name, year=year)

@app.route('/display/<league_name>/<year>', defaults={'team': None})
@app.route('/display/<league_name>/<year>/<team>')
def display_results(league_name, year, team=None):
    player_stats = pd.DataFrame()
    
    for filename in os.listdir('../data/stats'):
        if filename.endswith('.json') and league_name.lower().split(" ")[0] in filename:
            player_stats = pd.read_json('../data/stats/' + filename)
            
    if not player_stats.empty and "season" in player_stats.columns and "teamName" in player_stats.columns:
        players_data = player_stats[(player_stats["season"]==int(year)) & (player_stats["teamName"]==team)]
    else:
        players_data = pd.DataFrame()
    print(players_data)
    return render_template('display_results.html', league_name=league_name, year=year, team=team, players_data=players_data.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)
