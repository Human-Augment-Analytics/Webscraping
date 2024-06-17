import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json

def generate_choropleth_map():
    # Load GeoJSON file for Atlanta zip codes
    with open('filtered_ga_georgia_zip_codes_geo.geojson') as f:
        geojson = json.load(f)

    # Load the CSV data
    df = pd.read_csv('filtered_ACS_2020_Housing_Gross_Rent.csv')

    # Define the midpoints for each rent range
    rent_midpoints = {
        '# Gross rent less than $500, 2020': 250,
        '# Gross rent $500 to $999, 2020': 750,
        '# Gross rent $1,000 to $1,499, 2020': 1250,
        '# Gross rent $1,500 to $1,999, 2020': 1750,
        '# Gross rent $2,000 to $2,499, 2020': 2250,
        '# Gross rent $2,500 to $2,999, 2020': 2750,
        '# Gross rent $3,000 or more, 2020': 3250  # Assuming $3,250 for $3,000 or more
    }

    # Function to calculate the average rent
    def calculate_average_rent(row):
        weighted_sum = 0
        total_units = row['# Renter-occupied housing units, 2020']
        for column, midpoint in rent_midpoints.items():
            units = row[column]
            weighted_sum += units * midpoint
        average_rent = weighted_sum / total_units
        return average_rent

    # Calculate average rent for each row in the dataframe
    df['average_rent'] = df.apply(calculate_average_rent, axis=1)

    # Create a data frame for the choropleth map
    choropleth_data = df[['Geographic ID for geographic unit', 'average_rent']]
    choropleth_data.columns = ['ZCTA5CE10', 'average_rent']

    # Create a choropleth map
    fig = px.choropleth_mapbox(
        choropleth_data,
        geojson=geojson,
        locations='ZCTA5CE10',
        color='average_rent',
        featureidkey="properties.ZCTA5CE10",
        mapbox_style="open-street-map",
        center={"lat": 33.7756, "lon": -84.3963},
        zoom=10,
        opacity=0.3,  # Make the heatmap more transparent
        color_continuous_scale="Viridis"
    )

    # Add a marker at the center of Georgia Tech
    georgia_tech_center = {"lat": 33.7756, "lon": -84.3963}
    fig.add_trace(
        go.Scattermapbox(
            lat=[georgia_tech_center["lat"]],
            lon=[georgia_tech_center["lon"]],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=14,
                color='rgb(184, 134, 11)'  # Old gold color
            ),
            text=["Georgia Tech"],
            name="Georgia Tech"
        )
    )

    # Set Mapbox access token
    fig.update_layout(mapbox_accesstoken='pk.eyJ1IjoiYWNhbXBiZWxsOTAiLCJhIjoiY2x3aWFobDFtMGtjdzJqcGY5eGxvaGl4cCJ9.tk36QvzIVB-R66wHhSYFZA')

    # Return the figure as JSON
    return fig.to_json()


