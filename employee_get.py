import requests
from requests.auth import HTTPBasicAuth

url_employee = "http://dummy.restapiexample.com/api/v1/employee/9"
r = requests.get(url = url_employee,headers ={'User-Agent': 'Bhatti'})
data = r.json()

# print(r.status_code)
# print(r)
#
# print(data['status'])
# print(data['data'])

for status in data:
    print (status)