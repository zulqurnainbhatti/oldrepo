import requests

from requests.auth import HTTPBasicAuth

Tufin = "https://172.31.1.100/securetrack/api/zones"

body = {
	"zone": {
		"comment": "test88",
		"name": zonenname
	}
}

r = requests.post(url=Tufin, auth=('admin', 'tufin123'), json=body, verify=False)

print(r.status_code)

