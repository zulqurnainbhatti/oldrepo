import requests
from requests.auth import HTTPBasicAuth

API_ENDPOINT = "https://172.31.1.100/securetrack/api/zones"

body = {
	"zone": {
		"comment": "testzone",
		"name": "Test12"
	}
}

r = requests.post(url=API_ENDPOINT, auth=('admin', 'tufin123'), data=body, verify=False)

#pastebin_url = r.text
#print("The pastebin URL is:%s" % pastebin_url)
print(r.status_code)