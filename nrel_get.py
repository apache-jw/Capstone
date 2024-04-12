import requests

# Define the API endpoint
url = 'https://developer.nrel.gov/api/altfuelstations/v1/nearest.json'

# Specify the parameters for the API request
params = {
    'api_key': '#########',  
    'location': 'California',
    'fuel_type': 'ELEC',  # Electric charging stations
    'limit': 100,  # Adjust the limit as per your needs
    'radius': 500  # Search radius in miles, adjust if necessary
}

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print('Charging stations in California:', data)
else:
    print('Failed to retrieve data:', response.status_code)
