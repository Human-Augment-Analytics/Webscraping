import plotly.express as px
import json

# Load GeoJSON file for Atlanta zip codes
with open('filtered_ACS_2020_Housing_Gross_Rent.geojson') as f:
    geojson = json.load(f)

# Extract the GEOIDs and assign dummy values for coloring
geojson_features = geojson['features']
dummy_data = {
    'GEOID': ['30084', '30309', '30032', '30033', '30307'],
    'dummy_value': [1, 2, 3, 4, 5]
}

# def process_geojson(data):
#     filtered_features = []
#     for feature in data['features']:
#         properties = feature['properties']
#         print("-" * 50)
#         print(properties['GEOID'])
# process_geojson(geojson)
# print(dummy_data)

# Create a choropleth map
fig = px.choropleth_mapbox(
    dummy_data,
    geojson=geojson,
    locations='GEOID',
    color='dummy_value',
    featureidkey="properties.GEOID",
    mapbox_style="carto-positron",
    center={"lat": 33.7756, "lon": -84.3963},
    zoom=10,
    # opacity=0.5,
    color_continuous_scale="Viridis"
)

# Set Mapbox access token
fig.update_layout(mapbox_accesstoken='pk.eyJ1IjoiYWNhbXBiZWxsOTAiLCJhIjoiY2x3aWFobDFtMGtjdzJqcGY5eGxvaGl4cCJ9.tk36QvzIVB-R66wHhSYFZA')

# Show the map
fig.show()
