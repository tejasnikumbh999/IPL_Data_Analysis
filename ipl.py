import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
 
#load data

df = pd.read_csv('https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv')
df=df.drop(columns='id')                                                        #Drop irrelevant columns
#Data cleaning and pre processing
df=df.fillna(0)
mappings={'Rising Pune Supergiant':'Rising Pune Supergiants','Delhi Capitals':'Delhi Daredevils'}
df['team1']=df['team1'].replace(mappings)
df['team2']=df['team2'].replace(mappings)
df['winner']=df['winner'].replace(mappings)
df['toss_winner']=df['toss_winner'].replace(mappings)

#Column to identify the loosing team
loser=[]
for i in range(756):
  if (df.iloc[i,3])!=(df.iloc[i,9]):
    loser.append(df.iloc[i,3])
  elif (df.iloc[i,9])==0:
    loser.append(0)
  else:
    loser.append(df.iloc[i,4])
df['Loser']=loser

#Column to identify the matches played by each team
total={}
count=0
for i in df['team1'].unique():
  for m in range(756):
    if i==df.iloc[m,3]:
      count+=1
    else:
      if i==df.iloc[m,4]:
        count+=1
  total[i]=count
  count=0

#to create a new column of total matches played by the winner over all the seasons
match=[]
for i in df['winner']:
  for j,k in total.items():
    if i==j:
      match.append(k)
    elif i==0:
      match.append(0)
      break

df['Total_matches_played_by_winner']=match

#Replace the year of tournament by season
df['season'].replace([ 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,2018,2019],['Season 1','Season 2',
    'Season 3','Season 4','Season 5','Season 6','Season 7','Season 8','Season 9','Season 10','Season 11','Season 12'],
    inplace=True)
#Drop the column with no winner
df = df[df['winner'] != 0]
df.dropna(inplace=True)

app = dash.Dash(__name__)
server=app.server
 
#Create layout of app
app.layout = html.Div([html.Div([
    html.Audio(src='https://quz1yp-a.akamaihd.net/downloads/ringtones/files/mp3/ayogi-309.mp3',autoPlay=True,controls=True,
              title='IPL Anthem',loop=True,style={'opacity':'30%'}),
    html.Div([html.Img(src='https://i0.wp.com/www.uniquenewsonline.com/wp-content/uploads/2022/01/Tata-Ipl-Log.png?w=1280&ssl=1',
              style={'height':'20%', 'width':'30%',"border":"5px  white solid",'borderRadius': '10px',})],
              style={'class':'rotate','textAlign': 'center'}),
    html.H1(children='Indian Premiur League (IPL) Dashboard',
              style={"color": "white",'backgroundColor':'midnightblue','textAlign': 'center',"border":"2px white solid",
            'borderRadius': '10px','overflow': 'hidden'}),
    html.Br(),
    
    html.Div([dcc.Dropdown(['Best team based on Number of Wins','Best team based on Win by Runs',
            'Best Team based on Win by Wickets','Best Player based on Player of the Match','Luckiest Venue for Each Team',
            'Winning probability by Winning Toss'],'Best team based on Number of Wins',id='Condition',
            style={'textAlign': 'center',"font-weight": "bold",'backgroundColor':'lightcyan'})]),
    html.Br(),
    
    html.Div([dcc.RadioItems(['Overall','Season 1','Season 2','Season 3','Season 4','Season 5','Season 6','Season 7',
            'Season 8','Season 9','Season 10','Season 11','Season 12'],'Overall',id='Season',inline=True)],
             style = {"font-weight": "bold",'display': 'block', 'cursor': 'pointer','textAlign': 'center',
            "margin-right": "100px","color": "black"}),
    html.Br(),
    
    html.Div([dcc.Graph(id='Display',)],style={'opacity':'80%'})]),
    html.Br(),
                       
    html.H3(children='Created by : Tejas Nikumbh | Contact me : tejasnikumbh999@gmail.com',style={"color": "white",'backgroundColor':'#0d195a','textAlign': 'center',
            "border":"2px white solid",'borderRadius': '10px','overflow': 'hidden'})],
            style={"color": "navy",'background-image': 'url("https://www.freewalldownload.com/download/cricket-ball-wallpapers-for-mobile-free-download/")',
            'background-repeat': 'no-repeat','background-size': '1500px 1100px',"border":"5px navy solid",
            'borderRadius': '10px','overflow': 'hidden'})

@app.callback(
    Output('Display','figure'),
    [Input('Condition','value'),Input('Season','value')])

def update_graph(Condition,Season):
  if Condition=='Best team based on Number of Wins':
    if Season=='Overall':
      Best_team=px.pie(data_frame=df,names='winner',title='Best team based on Number of Wins',hole=0.3,hover_data=['Total_matches_played_by_winner'])
      Best_team.update_traces(textinfo="label+value",textposition='inside')
      Best_team.update_layout(margin=dict(t=70, b=20, l=10, r=10))
      Best_team.add_layout_image(dict(source="https://raw.githubusercontent.com/tejasnikumbh999/IPL_Analysis/main/Daco_4737816.png",
      xref="paper", yref="paper",x=0.532, y=0.387,sizex=0.22, sizey=0.22,xanchor="right", yanchor="bottom"))
      return Best_team
    else:
      df1 = df[df['season'] == Season]
      Best_team=px.pie(data_frame=df1,names='winner',title='Best team based on Number of Wins',hole=0.3)
      Best_team.update_traces(textinfo="label+value",textposition='inside')
      Best_team.update_layout(margin=dict(t=70, b=20, l=10, r=10))
      Best_team.add_layout_image(dict(source="https://raw.githubusercontent.com/tejasnikumbh999/IPL_Data_Analysis/main/Daco_4737816.png",
      xref="paper", yref="paper",x=0.532, y=0.387,sizex=0.22, sizey=0.22,xanchor="right", yanchor="bottom"))
      return Best_team
        
  elif Condition== 'Best team based on Win by Runs':
    if Season=='Overall':
      Win_run=px.scatter(df,x='winner',y='win_by_runs',color='Loser',size='win_by_runs',title='Best team based on Win by Runs')
      Win_run.update_layout(margin=dict(t=70, b=20, l=10, r=10))
      return Win_run
    else:  
      df1 = df[df['season'] == Season]
      Win_run=px.scatter(df1,x='winner',y='win_by_runs',color='Loser',size='win_by_runs',title='Best team based on Win by Runs')
      Win_run.update_layout(margin=dict(t=70, b=20, l=10, r=10))
      return Win_run

  elif Condition== 'Best Team based on Win by Wickets':
    if Season=='Overall':
      Win_Wick=px.scatter(df,x='winner',y='win_by_wickets',color='Loser',size='win_by_wickets',title='Best team based on Win by Wickets')
      Win_Wick.update_layout(margin=dict(t=70, b=20, l=10, r=10))
      return Win_Wick
    else:
      df2 = df[(df['season'] == Season) & (df["win_by_wickets"]>0)]
      Win_Wick=px.scatter(df2,x='winner',y='win_by_wickets',color='Loser',size='win_by_wickets',title='Best team based on Win by wickets')
      Win_Wick.update_layout(margin=dict(t=70, b=20, l=10, r=10))
      return Win_Wick
        
  elif Condition== 'Best Player based on Player of the Match':
    if Season=='Overall':
      Best_Player=px.histogram(df,x='player_of_match',color='player_of_match',title='Best Player based on Player of the Match')
      Best_Player.update_layout(xaxis={'categoryorder':'total descending'},margin=dict(t=70, b=20, l=10, r=10))
      return Best_Player
    else:
      df3 = df[df['season'] == Season]
      Best_Player=px.histogram(df3,x='player_of_match',color='player_of_match',title='Best Player based on Player of the Match')
      Best_Player.update_layout(xaxis={'categoryorder':'total descending'},margin=dict(t=70, b=20, l=10, r=10))
      return Best_Player
        
  elif Condition== 'Luckiest Venue for Each Team':
    if Season=='Overall':
      Lucky_venue=px.histogram(df,x='venue',color='venue',title='Luckiest Venue for Each Team',animation_frame='winner',barmode='relative')
      Lucky_venue.update_xaxes(showticklabels=False) # Hide x axis ticks 
      Lucky_venue.update_layout(xaxis={'categoryorder':'total descending'},margin=dict(t=70, b=20, l=10, r=10))
      Lucky_venue['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 10)
      Lucky_venue['layout']['sliders'][0]['pad']=dict(r= 10, t= 20,)
      return Lucky_venue
    else:
      df4 = df[df['season'] == Season]
      Lucky_venue=px.histogram(df4,x='venue',color='venue',title='Luckiest Venue for Each Team',animation_frame='winner',barmode='relative')
      Lucky_venue.update_xaxes(showticklabels=False) # Hide x axis ticks
      Lucky_venue.update_layout(xaxis={'categoryorder':'total descending'},margin=dict(t=70, b=20, l=10, r=10),title={'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
      Lucky_venue['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 10)
      Lucky_venue['layout']['sliders'][0]['pad']=dict(r= 10, t= 20,)
      return Lucky_venue

  elif Condition== 'Winning probability by Winning Toss':
    if Season=='Overall':
      Win_prob= px.sunburst(df, path=['toss_winner', 'winner','toss_decision'],title='Winning probability by Winning Toss')
      Win_prob.update_layout(margin = dict(t=70, b=20, l=10, r=10))
      Win_prob.update_traces(textinfo="label+percent parent+value",insidetextorientation='radial')
      return Win_prob
    else:
      df5 = df[df['season'] == Season]
      Win_prob= px.sunburst(df5, path=['toss_winner', 'winner'],title='Winning probability by Winning Toss')
      Win_prob.update_layout(margin = dict(t=70, b=20, l=10, r=10))
      Win_prob.update_traces(textinfo="label+percent parent+value",insidetextorientation='radial')
      return Win_prob
    
if __name__ == '__main__':
    app.run_server(debug='True')
