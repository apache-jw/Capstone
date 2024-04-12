import requests

# Define the API endpoint
url = 'https://api.openchargemap.io/v3/poi/'

# Specify the parameters for the API request
params = {
    'output': 'json',
    'countrycode': 'US',
    'latitude': 36.7783,
    'longitude': -119.4179,
    'maxresults': 100,
    'compact': True,
    'verbose': False,
    'key': '########################'
}

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print('Charging stations in California:', data)
else:
    print('Failed to retrieve data:', response.status_code)
