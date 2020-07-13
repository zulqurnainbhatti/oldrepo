import requests

from requests.auth import HTTPBasicAuth

Link = "http://api.deutschebahn.com/stada/v2/stations"

#zonenname = input("Zonenname: ")
#print('The Zonenname is', zonenname)

r = requests.get(url=Link, headers = {"Authorization": "Bearer cb009ba13126158ad3a38f886a463a41"})
data = r.json()
print(data)

for zone in data["result"]:
    if "München Hbf" in zone["name"]:
        print(zone['name'])
        print(zone['number'])