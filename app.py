import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.express as px
import pandas as pd
from summarizer import Summarizer

#df = pd.read_csv('scraped_articles.csv')

df = pd.read_csv('scraped_articles.csv', sep=';')

print(df.text)

#s = Summarizer()
#test_summary = s.summarize(text = df.text[0])
test_summary = "Chatbots were the main headliners at the Mobile World Congress 2017. The only question around chatbots was who would monopolize the field, not whether chatbots would take off in the first place. There isn’t even an ecosystem for a platform to dominate. The big divide is text vs. speech."

text_word_count = []

# populate the lists with sentence lengths
for i in df['text']:
    if(pd.notna(i)):
        text_word_count.append(len(i.split()))

length_df = pd.DataFrame({'text':text_word_count})

#fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig = px.histogram(length_df, x="text")

# set up dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Hello World',
                        className='nine columns'),
                html.Img(
                    src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
                    className='three columns',
                    style={
                        'height': '15%',
                        'width': '15%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),
                html.Div(children='''
                        Dash: A web application framework for Python.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure=fig
                )
                ], className= 'six columns'
                ),

                html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure=fig
                )
                ], className= 'six columns'
                )
            ], className="row"
            
        ),

        html.Div(
            [
                html.Div(
                        [
                            html.Div(
                                [html.H6(id="tile1_1_text"), html.P(test_summary)],
                                id="tile1_1",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                                
                            ),
                            html.Div(
                                [html.H6(id="tile1_2_text"), html.P(test_summary)],
                                id="tile1_2",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                            ),
                            html.Div(
                                [html.H6(id="tile1_3_text"), html.P(test_summary)],
                                id="tile1_3",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                            ),
                            html.Div(
                                [html.H6(id="tile1_4_text"), html.P(test_summary)],
                                id="tile1_4",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                            ),
                        ],
                        id="info-container-1",
                        className="twelve columns",
                        ),
            ], className="row"
            
        ),

        html.Div(
            [
                html.Div(
                        [
                            html.Div(
                                [html.H6(id="tile2_1_text"), html.P(test_summary)],
                                id="tile2_1",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                                
                            ),
                            html.Div(
                                [html.H6(id="tile2_2_text"), html.P(test_summary)],
                                id="tile2_2",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                            ),
                            html.Div(
                                [html.H6(id="tile2_3_text"), html.P(test_summary)],
                                id="tile2_3",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                            ),
                            html.Div(
                                [html.H6(id="tile2_4_text"), html.P(test_summary)],
                                id="tile2_4",
                                style={'width': '20%', 'display': 'inline-block'},
                                className="mini_container",
                            ),
                        ],
                        id="info-container-2",
                        className="twelve columns",
                        ),
            ], className="row"
            
        )
    ], className='ten columns offset-by-one')
)

if __name__ == '__main__':
    app.run_server(debug=True)