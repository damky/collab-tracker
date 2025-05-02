import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from typing import List, Dict

class InfluencerDashboard:
    def __init__(self):
        self.app = dash.Dash(__name__)
        
    def create_layout(self, influencers: List[Dict]):
        df = pd.DataFrame(influencers)
        
        # Create price distribution chart
        price_fig = px.histogram(df, x='price', 
                               title='Distribution of Collaboration Prices',
                               labels={'price': 'Price ($)'})
        
        # Create engagement rate vs price scatter plot
        engagement_fig = px.scatter(df, x='price', y='engagement_rate',
                                  title='Engagement Rate vs Price',
                                  labels={'price': 'Price ($)', 
                                         'engagement_rate': 'Engagement Rate (%)'})
        
        self.app.layout = html.Div([
            html.H1('Influencer Collaboration Dashboard'),
            
            html.Div([
                dcc.Graph(figure=price_fig),
                dcc.Graph(figure=engagement_fig)
            ]),
            
            html.Div([
                html.H3('Influencer List'),
                html.Table([
                    html.Thead(html.Tr([
                        html.Th('Name'),
                        html.Th('Platform'),
                        html.Th('Price'),
                        html.Th('Engagement Rate')
                    ])),
                    html.Tbody([
                        html.Tr([
                            html.Td(inf['name']),
                            html.Td(inf['platform']),
                            html.Td(f"${inf['price']}"),
                            html.Td(f"{inf['engagement_rate']}%")
                        ]) for inf in influencers
                    ])
                ])
            ])
        ])
    
    def run_server(self, debug: bool = True):
        self.app.run_server(debug=debug) 