import os
import pandas as pd

import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly
import dash
import plotly.graph_objects as go
import dash_auth
import re

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
app.Title = 'World Bank Poverty & Equity'
USER_PASSWORD_PAIRS = [['username','ofcourse123']]
auth = dash_auth.BasicAuth(app,USER_PASSWORD_PAIRS)
server = app.server


poverty = pd.read_csv('data/poverty.csv', low_memory=False)


gini = 'GINI index (World Bank estimate)'
gini_df = poverty[poverty[gini].notna()]


poverty_data = pd.read_csv('data/PovStatsData.csv')


regions = ['East Asia & Pacific', 'Europe & Central Asia',
           'Fragile and conflict affected situations', 'High income',
           'IDA countries classified as fragile situations',
           'IDA total', 'Latin America & Caribbean', 'Low & middle income',
           'Low income', 'Lower middle income', 'Middle East & North Africa',
           'Middle income', 'South Asia', 'Sub-Saharan Africa',
           'Upper middle income', 'World']


population_df = poverty_data[~poverty_data['Country Name'].isin(regions) &
                             (poverty_data['Indicator Name']== 'Population, total')]


income_share_df = poverty.filter(regex='Country Name|^year$|Income share.*?20').dropna()
income_share_df = income_share_df.rename(columns={
    'Income share held by lowest 20%': '1 Income share held by lowest 20%',
    'Income share held by second 20%': '2 Income share held by second 20%',
    'Income share held by third 20%': '3 Income share held by third 20%',
    'Income share held by fourth 20%': '4 Income share held by fourth 20%',
    'Income share held by highest 20%': '5 Income share held by highest 20%'
}).sort_index(axis=1)


income_share_df.columns = [re.sub('\d Income share held by ', '', col).title()
                           for col in income_share_df.columns]
income_share_cols = income_share_df.columns[:-2]

categories = ['Region', 'Income Group']



app.layout = dbc.Container([
    html.H1('World Bank Poverty And Equity', style={'color': 'white','fontSize': '40px'}),
    html.Br(),
    html.H3('World Population',style={'color':'#000000','backgroundColor':'#ADD8E6','textAlign': 'center'}),
    html.Br(),
    dbc.Row(
        dbc.Col([
            dcc.Dropdown(id='year_dropdown',
#                                   value='2010',
                         options=[{'label': year, 'value': str(year)}
                                           for year in range(1974, 2019)],
                         placeholder='Select Year',
                         style = dict(color='#000000')
                                 ),
            html.Br(),
            dcc.Graph(id='population_chart')
                ])
            ),
    html.Br(),
    html.H3('Gini Index - World Bank Data',
            style={'color':'#000000','backgroundColor':'#ADD8E6','textAlign': 'center'}),
    html.H6("""Gini index measures the extent to which the distribution
                of income (or, in some cases, consumption expenditure)
                among individuals or households within an economy
                deviates from a perfectly equal distribution. A Lorenz
                curve plots the cumulative percentages of total income
                received against the cumulative number of recipients,
                starting with the poorest individual or household. The
                Gini index measures the area between the Lorenz curve
                and a hypothetical line of absolute equality, expressed
                as a percentage of the maximum area under the line. Thus
                a Gini index of 0 represents perfect equality, while an
                index of 100 implies perfect inequality."""),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='gini_year_dropdown',
                         options=[{'label': y, 'value': y}
                                  for y in gini_df['year'].drop_duplicates().sort_values()],
                         placeholder='Select Year',
                         style = dict(color='#000000',backgroundColor='#ADD8E6')
                        ),
            html.Br(),
            dcc.Graph(id='gini_year_barchart')
        ]),
        dbc.Col([
            dcc.Dropdown(id='gini_country_dropdown',
                         multi=True,
                         options=[{'label': country, 'value': country} for
                                  country in gini_df['Country Name'].unique()],
                        placeholder='Select Country',
                        style = dict(color='#000000',backgroundColor='#ADD8E6')
                        ),
            html.Br(),
            dcc.Graph(id='gini_country_barchart')
        ]),
    ]),
    html.Br(),
    html.H3('Income Share Distribution', style={'color':'#000000','backgroundColor':'#ADD8E6','textAlign': 'center'}),
    html.Br(),
    dbc.Row(dbc.Col([
            dcc.Dropdown(id='income_share_country_dropdown',
                         options=[{'label': country, 'value': country}
                                   for country in income_share_df['Country Name'].unique()],
                        placeholder='Select Country',
                        style = dict(color='#000000',backgroundColor='#ADD8E6')
                        ),
            html.Br(),
            dcc.Graph(id='income_share_country_barchart')

                    ])
           ),
    dbc.Tabs([
          dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li(
                        [
                        'Author:  ',
                         html.A('Waleed',href='https://www.linkedin.com/in/waleedabdulla/')
                        ]
                       ),
                html.Li('Job Title: Data Analyst (actively looking for work)'),
                html.Li(['LinkedIn: ',
                             html.A('Waleed on LinkedIn',
                             href='https://github.com/Waleed18574/Waleed_Python_Data_Analysis_and_Data_Science_Portfolio_Projects')
                            ]),
                html.Li(['GitHub: ',
                             html.A('Waleed on Github',
                             href='https://www.linkedin.com/in/waleedabdulla/')
                            ]),
                html.Br(),
                html.Br()
                    ]
                   )
                 ],
            label='Author Info'),
          dbc.Tab([
           html.Ul([html.Li(['Data Source: ',
                             html.A('World Bank Poverty & Equity Dataset',
                             href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                            ]),
                    html.Li('Number of Economies: 170'),
                    html.Li('Temporal Coverage: 1974 - 2019'),
                    html.Li('Update Frequency: Quarterly'),
                    html.Li('Last Updated: March 18, 2020')

                    ]
                   ),
                  ],
            label='Project Key Facts'
                  )
            ]
           )
    ], style = {'backgroundColor':'#000000'})


@app.callback(Output('population_chart', 'figure'),
              [Input('year_dropdown', 'value')])
def plot_countries_by_population(year):
    if not year:
        raise PreventUpdate
    fig = go.Figure()
    year_df = population_df[['Country Name', year]].sort_values(year, ascending=False)[:20]
    fig.add_bar(x=year_df['Country Name'], y=year_df[year])
    fig.layout.title = f'Top twenty countries by population - {year}'
    fig.layout.template='plotly_dark'
    return fig


@app.callback(Output('gini_year_barchart', 'figure'),
              Input('gini_year_dropdown', 'value'))
def plot_gini_year_barchart(year):
    if not year:
        raise PreventUpdate
    df = gini_df[gini_df['year'].eq(year)].sort_values(gini).dropna(subset=[gini])
    n_countries = len(df['Country Name'])
    fig = px.bar(df,
                 x=gini,
                 y='Country Name',
                 orientation='h',
                 template='plotly_dark',
                 height=200 + (n_countries*20),
                 title=gini + ' ' + str(year))
    return fig


@app.callback(Output('gini_country_barchart', 'figure'),
              Input('gini_country_dropdown', 'value'))
def plot_gini_country_barchart(countries):
    if not countries:
        raise PreventUpdate
    df = gini_df[gini_df['Country Name'].isin(countries)].dropna(subset=[gini])
    fig = px.bar(df,
                 x=gini,
                 y='year',
                 orientation='h',
                 height=100 + (250*len(countries)),
                 labels={gini: 'Gini Index'},
                 template='plotly_dark',
                 color='Country Name',
                 title=''.join([gini, '<br>', '<b>',
                                ', '.join(countries), '</b>']))
    return fig

@app.callback(Output('income_share_country_barchart', 'figure'),
              Input('income_share_country_dropdown', 'value'))
def plot_income_share_barchart(country):
    if country is None:
        raise PreventUpdate
    fig = px.bar(income_share_df[income_share_df['Country Name']==country].dropna(),
                 x=income_share_cols,
                 y='Year',
                 barmode='stack',
                 height=600,
                 hover_name='Country Name',
                 title=f'Income Share Quintiles - {country}',
                 template='plotly_dark',
                 orientation='h')
    fig.layout.legend.title = None
    fig.layout.legend.orientation = 'h'
    fig.layout.legend.x = 0.2
    fig.layout.xaxis.title = 'Percent of Total Income'
    return fig


app.run_server()
