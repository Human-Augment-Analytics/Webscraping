import requests
import pandas as pd

# Function to get coordinates for a given neighborhood
def get_coordinates(neighborhood, api_key):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': f'{neighborhood}, Atlanta, GA',
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

# Your Google Maps API key
api_key = '<google maps api key>' #todo replace with env var

# Read the CSV file
df = pd.read_csv('atlanta_rent_prices.csv')

# Lists to store the coordinates
latitudes = []
longitudes = []

# Loop through each neighborhood and get the coordinates
for index, neighborhood in enumerate(df['neighborhood']):
    lat, lng = get_coordinates(neighborhood, api_key)
    latitudes.append(lat)
    longitudes.append(lng)
    # Print the result for tracking progress
    print(f"{index + 1}: {neighborhood} -> Latitude: {lat}, Longitude: {lng}")

# Add the coordinates to the DataFrame
df['latitude'] = latitudes
df['longitude'] = longitudes

# Save the updated DataFrame to a new CSV
df.to_csv('atlanta_neighborhoods_with_coordinates.csv', index=False)

# Display the updated DataFrame
print(df)
