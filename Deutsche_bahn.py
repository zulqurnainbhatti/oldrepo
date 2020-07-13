import requests
import datetime

bahn = "https://api.deutschebahn.com/freeplan/v1/arrivalBoard/8000261?date=2020-02-18"

r = requests.get(url = bahn, verify = False)
data = r.json()
print(data)
print(r.status_code)
for zone in data:
    print("Name: " + zone["name"])
    print("StopName: " + zone["stopName"])
    print("Origin: " + zone["origin"])
    print("Track: " + zone["track"])
    #print("DateTime: " + zone["dateTime"])
    print("DateTime: " + str(datetime.datetime.strptime(zone['dateTime'], '%Y-%m-%dT%H:%M')))
    print("------------------")
