import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import folium
import plotly.graph_objects as go
import plotly.express as px
# import opendatasets as od
import os
import dash
from dash import dcc
from dash import html
import time
from dash.dependencies import Input, Output


merge_race_result = pd.read_csv('merge_race_result.csv')
best_team_pit_stop = pd.read_csv('best_team_pit_stop.csv')

merge_race_result['continents'] = merge_race_result['continents'].str.lower()
merge_race_result['continents'] = merge_race_result['continents'].replace({'north_america' : 'north america',
                                                                           'south_america' : 'south america'})

############################################################################################

# colors = {
#     'background': '#353435',
#     'text': '#afb5bb'
#     }

markdown_map = '''
### Cartes sur le nombre de Grand Prix
C'est 2 cartes servent à illuster le nombre de Grand Prix aillant eu lieux sur chaque circuit à travers le monde.

La carte de gauche est dynamique dans le temps et montre l'evolution du nombre de courses saison après saison. Celle de droite
elle ne permet que de visualiser de façon statique toute les courses qui ont eu lieux sur chaque circuit.

*Grace au callback vous pouvez changer de scope et choisir le continent qui vous interresse dans le premier dropdown de la toolbar à gauche de la page*
'''

############################################################################################
#creation du dashboard
app = dash.Dash(__name__)
app.layout = html.Section(id = 'container_div', style={'background-color': '#F5F3F4',
                                                   'margin' : '0'},
    children=[
        ########################################################################
        #division de la partie haute
        html.Section(id = 'upper_div', style = {'background-color' : '#F5F3F4',
                                                'display' : 'flex',
                                                'flex-flow' : 'row',
                                                }, children=[
            ########################################################################
            #left tool bar
            html.Div(id = 'left_tool_bar', style = {'background-color' : '#B1A7A6',
                                                    'width': '20%',
                                                    'display' : 'flex',
                                                    'flex-flow' : 'column',
                                                    # 'justify-content' : 'space-around',
                                                    'padding-top' : '0.5%',
                                                    'align-items' : 'center'}, children=[

                html.H2(children = 'Tool-bar pour la gestion des callbacks', style={'text-align' : 'center', 'color' : '#161A1D'}),
                ########################################################################
                #dropdown
                html.Div(children=[
                    html.Label('Dropdown selection du continent', style = {'color' : '#0B090A', 'font-size' : '1.1em'}),
                    dcc.Dropdown(id = 'continent_dropdown',
                        options=[
                            {'label': u'Europe', 'value': 'europe'},
                            {'label': 'Africa', 'value': 'africa'},
                            {'label': 'North America', 'value': 'north america'},
                            {'label': 'South America', 'value': 'south america'},
                            {'label' : 'World', 'value' : 'world'},
                            {'label': 'Asia', 'value': 'asia'}
                        ],
                        value='world',
                        style = {'background' : '#E5383B',
                                 'color' : '#0B090A'}
                    ),
                ], style = {'width' : '85%'}#, 'margin' : 'auto'
                ),
                ########################################################################

                ########################################################################
                #multiple dropdaown
                html.Div(children = [
                    html.Label("Selection multiple de constructeurs", style = {'color' : '#0B090A', 'font-size' : '1.1em'}),
                    dcc.Dropdown(id = 'constru_dropdown',
                        options=[
                            {'label': 'Mercedes', 'value': 'Mercedes'},
                            {'label': u'Red Bull', 'value': 'Red Bull'},
                            {'label': 'Ferrari', 'value': 'Ferrari'},
                            {'label': 'Renault', 'value': 'Renault'},
                            {'label': 'Force India', 'value': 'Force India'},
                            {'label': 'Williams', 'value': 'Williams'},
                            {'label': 'McLaren', 'value': 'McLaren'}
                        ],
                        value=['Red Bull', 'Mercedes'],
                        style = {'background' : '#E5383B',
                                 'color' : '#0B090A'},
                        multi=True
                    ),
                    ],style = {'width' : '85%', 'padding-top' : '8%',}#, 'margin' : 'auto'
                ),
                ########################################################################
            ],),
            ########################################################################

            ########################################################################
            #right part of upper part
            html.Div(id = 'right_part', style = {'background-color' : '#F5F3F4',
                                                 'width': '80%',
                                                 'display' : 'flex',
                                                 'flex-flow' : 'column'}, children=[

                ########################################################################
                #header logo division
                html.Div(id = 'header_logo', style = {'display' : 'flex',
                                                      'flex-flow' : 'row',
                                                      'margin-top'  : '0.7%'}, children=[

                    html.Img(id = 'logo', style={'width' : '170px',
                                                 'height' : 'auto',
                                                 'margin-left' : '8%'}, src = "https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-2-2.png"),
                    html.Div(id = 'title', style = {'margin-left' : '5%', 'justify-content' : 'center'}, children=[
                        html.H1(children='Formula1 1950 to 2021 Dashboard', style={'textAlign': 'center',
                                                                                   'color': '#A4161A',
                                                                                   'font-size' : '2em',
                                                                                   'justify-content' : 'center'}),

                        html.Div(children='''
                            This dashboard is going to give you some completary information abour Formula 1.
                            ''',
                            style={'textAlign': 'center',
                                   'color': '#161A1D',
                                   'font-size' : '1.4em'}),
                    ],),
                ],),
                ########################################################################


                    html.Div(id= 'text_and_graph', style={'display' : 'flex',
                                                          'flex-flow' : 'column'}, children = [

                    dcc.Markdown(children=markdown_map, style={'padding-top' : '3%',
                                                               'padding-right' : '20%',
                                                               'padding-left' : '2%',
                                                               'color' : '#161A1D'}),

                    html.Div(id = 'div_graph', style = {'display' : 'flex',
                                                        'flex-flow' : 'row',
                                                        'justify-content' : 'space-around',
                                                        'margin-top' : '1%'},
                        children =[

                            dcc.Graph(
                                id='din_gp_map',
                                figure={},
                                style={'width' : '47%',
                                       'display' : 'inline-block',
                                       'border' : '2px solid #B1A7A6',
                                       'border-radius' : '3%'}
                            ),
                            dcc.Graph(
                                id='stat_gp_map',
                                figure={},
                                style={'width' : '47%',
                                       'display' : 'inline-block',
                                       'border' : '2px solid #B1A7A6',
                                       'border-radius' : '3%'}
                            ),
                        ]
                    ),
                ],),
            ],),
            ########################################################################
        ],),
        ########################################################################

        ########################################################################
        #division partie basse
        html.Section(id = 'down_div', style = {'background-color' : '#red',
                                               'flex-flow' : 'row'},children=[

            html.Div(id = 'div_histo_pit_stop', style = {'padding-top' : '1%',
                                                         'padding-left' : '2%',
                                                         'padding-right' : '3%'},
                children =[
                    dcc.Graph(
                        id='histo_pit_stop',
                        figure={},
                        style={'width' : '40%',
                               'display' : 'inline-block',
                               'border' : '2px solid #B1A7A6',
                               'border-radius' : '3%'}
                    ),
                ]
            ),
        ],),
    ],


)#, style={'columnCount': 2})


# ------------------------------------------------------------------------------
#première partie du dashboard permettant de choisir un continent en fonction des
#input recupere dans le dropdown

#creation du callback 'input'/'Output'
@app.callback(
    Output('din_gp_map','figure'),
    Output('stat_gp_map', 'figure'),
    Input('continent_dropdown','value'))
#fonction de generation de la carte en fonction de la région choisi ('world' par defaut)
def update_figure(select_continent):
    container = "The continent chosen by user was: {}".format(select_continent)
    #differenciation des cas en world et le reste l'affichage est différent
    if select_continent == 'world':
        #creation de la premiere map
        fig = px.scatter_geo(merge_race_result,
                             lon = 'longitude',
                             lat = 'latitude',
                             color = 'nombre_GP', color_continuous_scale = 'ylorrd',
                             hover_name = 'name',
                             size = 'nombre_GP',
                             animation_frame = 'year',
                             projection="natural earth1",
                             template = 'plotly_dark')
        #creation de la deuxieme map
        fig2 = go.Figure()
        fig2.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = merge_race_result['longitude'],
            lat = merge_race_result['latitude'],
            text = merge_race_result['name'] + '<br>Fastest lap : ' + merge_race_result['GP_fastes_lap'] + 'min' + '<br>By : ' + merge_race_result['full_name'],
            marker = dict(
                    size = (merge_race_result['nombre_GP']**2)/20,
                opacity = 0.8,
                colorscale = 'ylorrd',
                cmin = 1,
                color = merge_race_result['nombre_GP'],
                cmax = merge_race_result['nombre_GP'].max(),
                colorbar_title="Nombre de GP<br>1950-2021",
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
                )
            ))

        #mise a jour du layout de la premiere map
        fig.update_layout(
            title_text = 'Evolution du nombre de courses par GP <br>de 1950 à 2021 dans le monde',
            geo = dict(
                scope = 'world',
                landcolor = 'rgb(217, 217, 217)',
                )
            )
        #mise a jour de layoutde la 2eme map
        fig2.update_layout(
            title_text = 'Emplacement et nombre de GP de chaque circuit<br>dans le monde',
            geo = dict(
                scope = 'world',
                landcolor = 'rgb(217, 217, 217)',
                ),
            template = 'plotly_dark'
            )
    #affichage qui depend de la nouvelle partie selectionné par l'utilisateur
    else:
        dff = merge_race_result.copy()
        dff = dff[dff['continents'] == select_continent]
        #creation de la premiere map
        fig = px.scatter_geo(dff,
                             lon = 'longitude',
                             lat = 'latitude',
                             color = 'nombre_GP', color_continuous_scale = 'ylorrd',
                             hover_name = 'name',
                             size = 'nombre_GP',
                             animation_frame = 'year',
                             projection="natural earth1",
                             template = 'plotly_dark')

        #creation de la deuxieme map
        fig2 = go.Figure()
        fig2.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = dff['longitude'],
            lat = dff['latitude'],
            text = dff['name'] + '<br>Fastest lap : ' + dff['GP_fastes_lap'] + 'min' + '<br>By : ' + dff['full_name'],
            marker = dict(
                    size = (dff['nombre_GP']**2)/20,
                opacity = 0.8,
                colorscale = 'ylorrd',
                cmin = 1,
                color = dff['nombre_GP'],
                cmax = dff['nombre_GP'].max(),
                colorbar_title="Nombre de GP<br>1950-2021",
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
                )
            ))
        #mise a jour du layout de la premiere map
        fig.update_layout(
            title_text = 'Evolution du nombre de courses par GP<br> de 1950 à 2021 en ' + select_continent,
            geo = dict(
                scope = select_continent,
                landcolor = 'rgb(217, 217, 217)',
                ),
            )
        #mise a jour du layout de la deuxieme map
        fig2.update_layout(
            title_text = 'Emplacement et nombre de GP de chaque circuit<br>en ' + select_continent,
            geo = dict(
                scope = select_continent,
                landcolor = 'rgb(217, 217, 217)',
                ),
            template = 'plotly_dark'
            )
    #retourne la map dinamic en fonction du scope choisi pas l'utilisateur
    return fig, fig2
    # /!\WARNING/!\
    #il n'est pas possible de scope du l'oceanie car il ne fait pas partie des scope de la fonction
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#première partie du dashboard permettant de choisir un continent en fonction des
#input recupere dans le dropdown

#creation du callback 'input'/'Output'
@app.callback(
    Output('histo_pit_stop', 'figure'),
    Input('constru_dropdown','value'))
#fonction de generation de la carte en fonction de la région choisi ('world' par defaut)
def update_figure2(select_constructor):
    container = "Constructors chosen by user were: {}".format(select_constructor)

    dff = best_team_pit_stop.copy()
    new_df = dff[dff['constructors'].isin(select_constructor)]
    #creation de la premiere map
    fig = px.histogram(new_df, x="seconds", y="one", color="constructors",
                   marginal="violin", # or violin, rug
                   hover_data=new_df.columns)

    #mise a jour du layout de la premiere map
    fig.update_layout(barmode='overlay',
                      template = 'plotly_dark')
    fig.update_traces(opacity=0.75)

    #retourne la map dinamic en fonction du scope choisi pas l'utilisateur
    return fig
    # /!\WARNING/!\
    #il n'est pas possible de scope du l'oceanie car il ne fait pas partie des scope de la fonction
# ------------------------------------------------------------------------------


#partie de selectiond de ce qui sera lancer a l'execution
if __name__ == '__main__':
    app.run_server(debug=True)
