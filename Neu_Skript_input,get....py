import requests
import urllib.request
from requests.auth import HTTPBasicAuth
print("Diese Skript erstellt wir für neu Zone und die erstellen mit alle IP zusammen.")

#step1 input zonenname()

zonenname = input("Zonenname: ")
print('Die Zonenname ist', zonenname)

zonenname_neu = input("Neuer Zonenname: ")
print('Die Zonenname ist', zonenname_neu)

#step2 Post: (Neu zonenname erstellen in zone)

allezone_url = "https://172.31.1.100/securetrack/api/zones.json"

#step3+4 Get und Post: (Get alle zone und dann schauen, ob ihren zone gibt)

r = requests.get(url = allezone_url, auth = HTTPBasicAuth("admin", "tufin123"), verify = False)
data = r.json()
for zone in data["zones"] ["zone"]:
    if zonenname in zone['name']:
        print("Name: " + zone['name'])
        print("ID: " + zone['id'])
        zoneid = zone['id']

#step5 Entries : (add zone entries und schauen ob ihren IP gibt)

add_entries = "https://172.31.1.100/securetrack/api/zones/" + zoneid

body = {
    "zone" : {
        "comment" : "abc123zone",
        "name" : zonenname_neu
    }
}
r =  requests.put(url = add_entries, auth = HTTPBasicAuth("admin", "tufin123"),json = body,  verify = False)
print(r.status_code)
print("Danke vor Ihrer Zeit. Jetzt Programm Fertig!")


