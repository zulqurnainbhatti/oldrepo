import requests
import urllib.request

from requests.auth import HTTPBasicAuth

url = "https://172.31.1.100/securetrack/api/zones/151/entries"

Link = ("https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt")

# response = urllib.request.urlopen(Link)
# data = response.read()
# print(data)

for line in urllib.request.urlopen(Link):

    if not line.decode('utf-8').strip().startswith("#"):
        body = {
                "zone_entry": {
                    "ip": line.decode('utf-8').strip(),
                    "netmask": "255.255.255.255",
                    "description": "My new IP"
                }
            }
        print(body)
    # r = requests.post(url, auth=('admin', 'tufin123'), json=body, verify=False)