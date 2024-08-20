import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_intelligence_data():
    np.random.seed(42)
    date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='H')
    n_events = len(date_range)

    data = {
        'Timestamp': date_range,
        'EventType': np.random.choice(['Cyber Attack', 'Physical Intrusion', 'Data Breach', 'Insider Threat', 'Social Engineering'], n_events),
        'Severity': np.random.choice(['Low', 'Medium', 'High', 'Critical'], n_events, p=[0.4, 0.3, 0.2, 0.1]),
        'Location': np.random.choice(['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'], n_events),
        'TargetSector': np.random.choice(['Government', 'Finance', 'Healthcare', 'Energy', 'Technology', 'Manufacturing'], n_events),
        'ThreatActor': np.random.choice(['Nation State', 'Organized Crime', 'Hacktivist', 'Insider', 'Unknown'], n_events),
        'ImpactScore': np.random.randint(1, 101, n_events)
    }

    df = pd.DataFrame(data)

    # Add some calculated fields
    df['Date'] = df['Timestamp'].dt.date
    df['Hour'] = df['Timestamp'].dt.hour
    df['DayOfWeek'] = df['Timestamp'].dt.day_name()
    df['Month'] = df['Timestamp'].dt.to_period('M')
    df['Quarter'] = df['Timestamp'].dt.to_period('Q')
    df['Year'] = df['Timestamp'].dt.year

    # Calculate cumulative impact score
    df['CumulativeImpact'] = df.groupby('Year')['ImpactScore'].cumsum()

    # Add latitude and longitude for map visualization
    location_coords = {
        'North America': (40, -100),
        'South America': (-15, -60),
        'Europe': (50, 10),
        'Asia': (35, 105),
        'Africa': (0, 20),
        'Australia': (-25, 135)
    }
    df['Latitude'] = df['Location'].map(lambda x: location_coords[x][0] + np.random.normal(0, 5))
    df['Longitude'] = df['Location'].map(lambda x: location_coords[x][1] + np.random.normal(0, 5))

    return df

if __name__ == "__main__":
    df = generate_intelligence_data()
    df.to_csv('intelligence_data.csv', index=False)
    print("Data preparation complete. CSV file 'intelligence_data.csv' has been created.")