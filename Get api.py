
import requests
from requests.auth import HTTPBasicAuth

URL = "https://10.3.62.134/securetrack/api/zones.json"

r = requests.get(url=URL, auth=HTTPBasicAuth('admin', 'splat123'), verify=False)
data = r.json()
print(data)

for zone in data['zones']['zone']:

    print("Name: " + zone['name'])

    print("ID:" + zone['id'])