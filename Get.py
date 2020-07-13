# importing the requests library
import requests

# api-endpoint
URL = "https://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "Aerasec"

# defining a params dict for the parameters to be sent to the API
PARAMS = {
    'key': 'AIzaSyAPm-obGT3376mC74icgKm8-sMZub8pp00',
    'address': location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

# print(data)

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
formatted_Telefonnummer = data['results'][0]['formatted_Telefonnummer']

print(data['status'])

# printing the output
print("Latitude:%s\n Longitude:%s\n Formatted Address:%s"
      %(latitude, longitude,formatted_address))
