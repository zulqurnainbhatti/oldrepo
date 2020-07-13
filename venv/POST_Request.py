import requests
# import json
from requests.auth import HTTPBasicAuth

url = "https://172.31.1.100/securetrack/api/zones"

body = {
	"zone": {'comment': "test_zone", 'name': "azubi12"}
}


r = requests.post(url, auth=('admin', 'tufin123'), json=body, verify=False)

#print(response.json())
print(r.status_code)

#print (req.text)
#print("The pastebin URL is:%s" % pastebin_url)