# import dash

import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

USERNAME_PASSWORD_PAIRS = [
    ['tejas', 'tejas'], ['guvi', 'guvi']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server

# load data

import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv")
df['season'].replace([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
                      2019], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)
df.drop(['id', 'date', 'umpire3'], axis=1, inplace=True)
df.dropna(inplace=True)

app.layout = html.Div([html.Div([
    html.Audio(src='https://quz1yp-a.akamaihd.net/downloads/ringtones/files/mp3/ayogi-309.mp3', controls=True,
               autoPlay=True, title='IPL Anthem', loop=True),
    html.H1(children='Indian Premiur League (IPL) Dashboard',
            style={
                "color": "white",
                'backgroundColor': 'midnightblue',
                'textAlign': 'center'
            }),
    html.Br(),
    html.Label('Best team based on the wins'),
    dcc.Dropdown(
        options=[
            {'label': 'Overall', 'value': '0'},
            {'label': 'Season 1', 'value': '1'},
            {'label': 'Season 2', 'value': '2'},
            {'label': 'Season 3', 'value': '3'},
            {'label': 'Season 4', 'value': '4'},
            {'label': 'Season 5', 'value': '5'},
            {'label': 'Season 6', 'value': '6'},
            {'label': 'Season 7', 'value': '7'},
            {'label': 'Season 8', 'value': '8'},
            {'label': 'Season 9', 'value': '9'},
            {'label': 'Season 10', 'value': '10'},
            {'label': 'Season 11', 'value': '11'},
            {'label': 'Season 12', 'value': '12'}
        ],
        placeholder="Select the season",
        style={"color": "crimson", 'backgroundColor': 'green'}
    ),
    html.Br(),
    html.Label('Best player of the season based on the man of the match rewards'),
    dcc.Dropdown(
        options=[
            {'label': 'Overall', 'value': '0'},
            {'label': 'Season 1', 'value': '1'},
            {'label': 'Season 2', 'value': '2'},
            {'label': 'Season 3', 'value': '3'},
            {'label': 'Season 4', 'value': '4'},
            {'label': 'Season 5', 'value': '5'},
            {'label': 'Season 6', 'value': '6'},
            {'label': 'Season 7', 'value': '7'},
            {'label': 'Season 8', 'value': '8'},
            {'label': 'Season 9', 'value': '9'},
            {'label': 'Season 10', 'value': '10'},
            {'label': 'Season 11', 'value': '11'},
            {'label': 'Season 12', 'value': '12'}
        ],
        placeholder="Select the season",
        value='Overall',
        style={"color": "crimson", 'backgroundColor': 'green'}
    ),
    html.Br(),
    html.Label('Best player of the team based on the man of the match rewards'),
    dcc.Dropdown(
        options=[
            {'label': 'Sunrisers Hyderabad', 'value': '0'},
            {'label': 'Mumbai Indians', 'value': '1'},
            {'label': 'Gujarat Lions', 'value': '2'},
            {'label': 'Rising Pune Supergiant', 'value': '3'},
            {'label': 'Kolkata Knight Riders', 'value': '4'},
            {'label': 'Royal Challengers Bangalore', 'value': '5'},
            {'label': 'Kings XI Punjab', 'value': '6'},
            {'label': 'Chennai Super Kings', 'value': '7'},
            {'label': 'Rajasthan Royals', 'value': '8'},
            {'label': 'Deccan Chargers', 'value': '9'},
            {'label': 'Kochi Tuskers Kerala', 'value': '10'},
            {'label': 'Pune Warriors', 'value': '11'},
            {'label': 'Rising Pune Supergiants', 'value': '12'},
            {'label': 'Delhi Capitals', 'value': '13'}
        ],
        placeholder="Select the team",
        style={"color": "navy", 'backgroundColor': 'green'}
    ),
    html.Br(),
    html.Label('Luckiest venue for each team'),
    dcc.Dropdown(
        options=[
            {'label': 'Sunrisers Hyderabad', 'value': '0'},
            {'label': 'Mumbai Indians', 'value': '1'},
            {'label': 'Gujarat Lions', 'value': '2'},
            {'label': 'Rising Pune Supergiant', 'value': '3'},
            {'label': 'Kolkata Knight Riders', 'value': '4'},
            {'label': 'Royal Challengers Bangalore', 'value': '5'},
            {'label': 'Kings XI Punjab', 'value': '6'},
            {'label': 'Chennai Super Kings', 'value': '7'},
            {'label': 'Rajasthan Royals', 'value': '8'},
            {'label': 'Deccan Chargers', 'value': '9'},
            {'label': 'Kochi Tuskers Kerala', 'value': '10'},
            {'label': 'Pune Warriors', 'value': '11'},
            {'label': 'Rising Pune Supergiants', 'value': '12'},
            {'label': 'Delhi Capitals', 'value': '13'}
        ],
        placeholder="Select the team",
        style={"color": "crimson", 'backgroundColor': 'green'}
    ),
    html.Br(),
    html.Br(),
    html.Label('Probability of a team winning match provided the win toss'),
    dcc.Dropdown(
        options=[
            {'label': 'Overall', 'value': '0'},
            {'label': 'Season 1', 'value': '1'},
            {'label': 'Season 2', 'value': '2'},
            {'label': 'Season 3', 'value': '3'},
            {'label': 'Season 4', 'value': '4'},
            {'label': 'Season 5', 'value': '5'},
            {'label': 'Season 6', 'value': '6'},
            {'label': 'Season 7', 'value': '7'},
            {'label': 'Season 8', 'value': '8'},
            {'label': 'Season 9', 'value': '9'},
            {'label': 'Season 10', 'value': '10'},
            {'label': 'Season 11', 'value': '11'},
            {'label': 'Season 12', 'value': '12'}
        ],
        placeholder="Select the season",
        style={"color": "purple", 'backgroundColor': 'green'}),
    html.Br(),
], style={'padding': 10, 'flex': 1}),
    html.H1(children='IPL Funzone',
            style={
                "color": "white",
                'backgroundColor': '#0d195a',
                'textAlign': 'center'
            }),
    html.Div([html.H1(children='KKR Anthem'),
              html.Audio(
                  src='https://www.downloadmobileringtones.com/mp3ringtone/KKR-Theme-Song-Ipl-2021-Ringtone-Download-dmr.mp3',
                  controls=True, title='KKR')]),
    html.Div([html.H1(children='KKR Anthem'),
              html.Audio(
                  src='https://www.downloadmobileringtones.com/mp3ringtone/KKR-Theme-Song-Ipl-2021-Ringtone-Download-dmr.mp3',
                  controls=True, title='KKR')
              ])
], style={"color": "yellow", 'backgroundColor': 'chocolate'})

if __name__ == '__main__':
    app.run_server(debug='True')