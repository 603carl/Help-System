import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dashboard_layout import create_layout
from callbacks import register_callbacks

# Load the data
df = pd.read_csv('intelligence_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Set the layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app, df)

if __name__ == '__main__':
    app.run_server(debug=True)