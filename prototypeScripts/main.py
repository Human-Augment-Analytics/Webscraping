import plotly.express as px
import pandas as pd
import json
from shapely.geometry import shape, Point

# Data with coordinates
df = pd.read_csv('atlanta_neighborhoods_with_coordinates.csv')

# Load GeoJSON file for Atlanta neighborhoods
with open('atlanta.geojson') as f:
    geojson = json.load(f)

# Function to find the neighborhood for a given point
def find_neighborhood(lat, lon, geojson):
    point = Point(lon, lat)
    for feature in geojson['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return feature['properties']['name']
    return None

# Add the neighborhood column based on coordinates
df['geojson_neighborhood'] = df.apply(lambda row: find_neighborhood(row['latitude'], row['longitude'], geojson), axis=1)

# Drop rows where the neighborhood could not be found
df = df.dropna(subset=['geojson_neighborhood'])

# Create a choropleth map
fig = px.choropleth_mapbox(
    df,
    geojson=geojson,
    locations='geojson_neighborhood',
    color='rent_price',
    featureidkey="properties.name",
    mapbox_style="carto-positron",
    center={"lat": 33.7490, "lon": -84.3880},
    zoom=10,
    opacity=0.5
)

# Set Mapbox access token
fig.update_layout(mapbox_accesstoken='<mapbox api key>') #todo replace with env var

# Show the map
fig.show()
