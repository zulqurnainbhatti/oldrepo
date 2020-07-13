import requests
import urllib.request
from requests.auth import HTTPBasicAuth

print("Weleche ID wollen Sie löschen von Zone? Bitte geben Zonenname")

zonenname = input("Zonenname: ")
print('Die Zonenname ist', zonenname)

allezone = "https://172.31.1.100/securetrack/api/zones.json"

r = requests.get(url = allezone, auth = HTTPBasicAuth("admin", "tufin123"), verify = False)
data = r.json()
for zone in data["zones"] ["zone"]:
    if zonenname in zone['name']:
        print("Name: " + zone['name'])
        print("ID: " + zone['id'])
        zoneid = zone['id']

# delID = input("DeleteID: ")

deleteurl = "https://172.31.1.100/securetrack/api/zones/" + zoneid

r = requests.delete(url = deleteurl, auth = HTTPBasicAuth("admin", "tufin123"), verify = False)

print(r.status_code)
print("Danke vor Ihrer Zeit. Ihren ID ist Löschet jetzt!")