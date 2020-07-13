# importing the requests library
import requests
from requests.auth import HTTPBasicAuth

# api-endpoint
URL = "https://172.31.1.100/securetrack/api/devices.json"

# get request and save the response as response object
r = requests.get(url=URL, auth=HTTPBasicAuth('admin', 'tufin123'), verify=False)

data = r.json()

print(data)

for device in data['devices']['device']:
    print("Name: " + device['name'])
    print("Vendor: " + device['vendor'])
    print("IP: " + device['ip'])
    print("Model" + device['model'])
    print("ID" + device['id'])

anzahl = data['devices']['total']

print("Es gibt " + str(anzahl) + " Devices insgesamt.")

