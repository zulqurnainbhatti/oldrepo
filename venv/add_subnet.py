import requests

from requests.auth import HTTPBasicAuth

url = "https://172.31.1.100/securetrack/api/zones/151/entries"

# https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt

# data = ('file' : open (r' C:\\Users\zbhatti\Desktop\blocklist.txt')
# for line in file : print(line);

file = open(r"C:\Users\zbhatti\Desktop\blocklist.txt","r")
for line in file:
    #print(line)
    if not line.strip().startswith("#"):
        body = {
            "zone_entry": {
                "ip": line.strip(),
                "netmask": "255.255.255.255",
                "description": "neue IP"
            }
        }
        print(body)
        r = requests.post(url, auth=('admin', 'tufin123'), json=body, verify=False)

# url = "https://172.31.1.100/securetrack/api/zones"
#
# body = {
# 	"zone": {'comment': "body", 'name': "Alle_IP"}
# }


#r = requests.post(url, auth=('admin', 'tufin123'), json=body, verify=False)

#print(body)

# print(body)

#r = requests.post(url=Tufin, auth=('admin', 'tufin123'), json=body, verify=False);

#print(r.status_code)