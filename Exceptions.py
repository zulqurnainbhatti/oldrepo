import requests
import sys
#import urllib.request

from requests.auth import HTTPBasicAuth

zonenname = input("Zonenname: ")

url_all_zones = "https://172.31.1.100/securetrack/api/zones.json"

r = requests.get(url=url_all_zones, auth=HTTPBasicAuth('admin', 'tufin123'), verify=False)
data = r.json()

zoneid = 0

for zone in data['zones']['zone']:
    if zonenname in zone['name']:
        print("Name: " + zone['name'])
        print("ID: " + zone['id'])
        #print("IP: " + zone['ip'])
        zoneid = zone['id']

if zoneid == 0:
    print("Zone existiert nicht. Bitte Probieren noch einmal. Danke :)")
    sys.exit(0)

else:
    url2 = "https://172.31.1.100/securetrack/api/zones/" + str(zoneid) + "/entries.json"

    r = requests.get(url=url2, auth=HTTPBasicAuth('admin', 'tufin123'), verify=False)
    data = r.json()

    for line in data['zone_entries']['zone_entry']:
        print(line)