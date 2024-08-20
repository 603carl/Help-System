from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def register_callbacks(app, df):
    @app.callback(
        [Output('event-map', 'figure'),
         Output('event-timeline', 'figure'),
         Output('event-types-chart', 'figure'),
         Output('severity-heatmap', 'figure'),
         Output('threat-actor-pie', 'figure'),
         Output('cumulative-impact-chart', 'figure'),
         Output('event-types-area-chart', 'figure')],
        [Input('date-range-picker', 'start_date'),
         Input('date-range-picker', 'end_date'),
         Input('event-type-dropdown', 'value'),
         Input('severity-dropdown', 'value'),
         Input('location-dropdown', 'value'),
         Input('target-sector-dropdown', 'value')]
    )
    def update_graphs(start_date, end_date, event_types, severities, locations, target_sectors):
        filtered_df = df

        if start_date and end_date:
            filtered_df = filtered_df[(filtered_df['Date'] >= start_date) & (filtered_df['Date'] <= end_date)]
        if event_types:
            filtered_df = filtered_df[filtered_df['EventType'].isin(event_types)]
        if severities:
            filtered_df = filtered_df[filtered_df['Severity'].isin(severities)]
        if locations:
            filtered_df = filtered_df[filtered_df['Location'].isin(locations)]
        if target_sectors:
            filtered_df = filtered_df[filtered_df['TargetSector'].isin(target_sectors)]

        # Event Map
        event_map = px.scatter_mapbox(filtered_df, lat="Latitude", lon="Longitude", color="EventType",
                                      size="ImpactScore", hover_name="EventType", zoom=1)
        event_map.update_layout(mapbox_style="carto-positron")

        # Event Timeline
        event_timeline = px.scatter(filtered_df, x="Timestamp", y="ImpactScore", color="EventType",
                                    size="ImpactScore", hover_data=["EventType", "Severity"])

        # Event Types Chart
        event_types_chart = px.bar(filtered_df['EventType'].value_counts(), orientation='h')

        # Severity Heatmap
        severity_heatmap = px.density_heatmap(filtered_df, x="TargetSector", y="Severity", z="ImpactScore",
                                              histfunc="avg")

        # Threat Actor Pie Chart
        threat_actor_pie = px.pie(filtered_df, names="ThreatActor", values="ImpactScore")

        # Cumulative Impact Chart
        cumulative_impact = filtered_df.groupby("Date")['ImpactScore'].sum().cumsum().reset_index()
        cumulative_impact_chart = px.line(cumulative_impact, x="Date", y="ImpactScore")

        # Event Types Area Chart
        event_types_area = px.area(filtered_df, x="Date", y="ImpactScore", color="EventType")

        return event_map, event_timeline, event_types_chart, severity_heatmap, threat_actor_pie, cumulative_impact_chart, event_types_area

    return app
    return app