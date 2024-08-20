import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Intelligence Analysis Dashboard", className="text-center mb-4"), width=12)
        ]),
        
        dbc.Row([
            dbc.Col([
                dcc.DatePickerRange(
                    id='date-range-picker',
                    start_date_placeholder_text="Start Date",
                    end_date_placeholder_text="End Date",
                    calendar_orientation='horizontal',
                    className="mb-3"
                ),
                dcc.Dropdown(
                    id='event-type-dropdown',
                    multi=True,
                    placeholder="Select Event Types",
                    className="mb-3"
                ),
                dcc.Dropdown(
                    id='severity-dropdown',
                    multi=True,
                    placeholder="Select Severity Levels",
                    className="mb-3"
                ),
                dcc.Dropdown(
                    id='location-dropdown',
                    multi=True,
                    placeholder="Select Locations",
                    className="mb-3"
                ),
                dcc.Dropdown(
                    id='target-sector-dropdown',
                    multi=True,
                    placeholder="Select Target Sectors",
                    className="mb-3"
                )
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Event Map", className="card-title"),
                        dcc.Graph(id="event-map")
                    ])
                ], className="mb-4"),
                
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Event Timeline", className="card-title"),
                        dcc.Graph(id="event-timeline")
                    ])
                ])
            ], width=9)
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Event Types", className="card-title"),
                        dcc.Graph(id="event-types-chart")
                    ])
                ])
            ], width=4),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Severity by Target Sector", className="card-title"),
                        dcc.Graph(id="severity-heatmap")
                    ])
                ])
            ], width=4),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Threat Actor Distribution", className="card-title"),
                        dcc.Graph(id="threat-actor-pie")
                    ])
                ])
            ], width=4)
        ], className="mt-4"),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Cumulative Impact Over Time", className="card-title"),
                        dcc.Graph(id="cumulative-impact-chart")
                    ])
                ])
            ], width=6),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Event Types Over Time", className="card-title"),
                        dcc.Graph(id="event-types-area-chart")
                    ])
                ])
            ], width=6)
        ], className="mt-4")
    ], fluid=True)