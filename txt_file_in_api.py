import requests
from requests.auth import HTTPBasicAuth
import urllib.request

ip = input("Ip : ")
print("Die IP ist", ip)

Link = "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt"

#r = requests.get(url=Link)
#data = r.json()
#print(data)

for line in urllib.request.urlopen(Link):
    if not line.decode('utf-8').strip().startswith("#"):
        body1 = {
                "zone_entry": {
                    "ip": line.decode('utf-8').strip(),
                    "prefix": "24"
                }
            }
        print(body1)
        # print(r.status_code)





#for zone in data['zones']['zone']:
    #print("IP:" + zone['ip'])
   # print("------------------")


pastebin_url = "https://pastebin.com/api/api_post.php"

r =  requests.post(url = pastebin_url, data = {"api_dev_key": "e23965221a7fce052cf6870bdfebd630","api_paste_code": body1 , "api_paste_private": "1", "api_option": "paste", "api_paste_expire_date": "1H"})
print(r.status_code)
print(r.text)