import requests
import urllib.request

from requests.auth import HTTPBasicAuth

print("Dieses Skript erstellt eine Zone und füllt diese mit IP Adressen. \n")

#Step1
zonenname = input("Zonenname: ")
print('The Zonenname is', zonenname)

# Step 2
# neuer Post Request, neue Zone erstellen mit zonenname

url_new_zone = "https://172.31.1.100/securetrack/api/zones"
url_all_zones = "https://172.31.1.100/securetrack/api/zones.json"

body = {
    "zone": {
        "comment": "test88",
        "name": zonenname
    }
}

r = requests.post(url=url_new_zone, auth=('admin', 'tufin123'), json=body, verify=False)

# 3 + 4 Step, get alle zonen, suche ID von zonnenname
r = requests.get(url=url_all_zones, auth=HTTPBasicAuth('admin', 'tufin123'), verify=False)
data = r.json()

for zone in data['zones']['zone']: # schleife
    if zonenname in zone['name']: # verzweigung
        print("Name: " + zone['name'])
        print("ID: " + zone['id'])
        zoneid = zone['id']

# zoneid

# 5. Step
# url ../zoneid/entries
#
url_add_entries = "https://172.31.1.100/securetrack/api/zones/" + zoneid + "/entries"
url_liste = ("https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt")

print(url_add_entries)

for line in urllib.request.urlopen(url_liste):
    if not line.decode('utf-8').strip().startswith("#"):
        body1 = {
                "zone_entry": {
                    "ip": line.decode('utf-8').strip(),
                    "prefix": "24"
                }
            }
        r = requests.post(url=url_add_entries, auth=('admin', 'tufin123'), json=body1, verify=False)
        print(body1)
        print(r.status_code)


print("Fertig!")
