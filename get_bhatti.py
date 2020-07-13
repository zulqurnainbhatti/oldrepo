import requests
from requests.auth import HTTPBasicAuth
Bhatti_Url = "https://172.31.1.100/securechangeworkflow/api/securechange/tickets/400.json"
r = requests.get(url=Bhatti_Url, auth=HTTPBasicAuth('bhatti', 'tufin123') , verify = False)
data = r.json()
#print(data)
#print(r.status_code)
#for zone in data:
    #print("Subject:" + zone[0])
    #print("ID:" + zone["id"])
    #print("Priority:" + zone["priority"])
for x,y in data['ticket'].items():
    if "comments" in x:
        print(y)