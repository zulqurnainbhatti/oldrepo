import requests
import datetime
from requests.auth import HTTPBasicAuth

#hofname = input("BahnHofname : ")
#print('Die Zonenname ist', hofname)

zonename = input("Zonenname : ")
print('Die Zonenname ist', zonename)


#bahn_url = "https://api.deutschebahn.com/freeplan/v1/location/" + hofname
#r = requests.get(url = bahn_url, data ={"api_dev_key": "e23965221a7fce052cf6870bdfebd630",
                                            #"api_paste_code": "", "api_paste_private": "1"})
#data = r.json()

URL = "https://172.31.1.100/securetrack/api/zones.json"
r =  requests.get(url= URL, auth = HTTPBasicAuth('admin', 'tufin123'), verify=False)
data = r.json()
print(data)

for zone in data['zones']['zone']:

    print("Name: " + zone['name'])

    print("ID:" + zone['id'])
    print("------------------")









# print(data)
# print(r.status_code)
# print(data[0]['id'])

# for zone in data:
#      print("Name: " + zone["name"])
#      print("ID: " + str(zone["id"]))
#
#      print("------------------")

# arrival_url = "https://api.deutschebahn.com/freeplan/v1/arrivalBoard/" + str(data[0]['id']) + "?date=2020-02-20"
#
# r = requests.get(url = arrival_url)
#
# print(r.json())

pastebin_url = "https://pastebin.com/api/api_post.php"

r =  requests.post(url = pastebin_url, data = {"api_dev_key": "e23965221a7fce052cf6870bdfebd630","api_paste_code": r.text, "api_paste_private": "1", "api_option": "paste", "api_paste_expire_date": "1H"})
print(r.status_code)
print(r.text)