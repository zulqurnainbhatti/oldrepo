import requests
from requests.auth import HTTPBasicAuth

print("Bitte gaben Sie ganze Informationen")

# empolyee = input("Empolyeename : ")
# salary = input("Salary : ")
# age = input("Age : ")


data = {'name': "Test" }


url_create = "http://dummy.restapiexample.com/api/v1/update/2"
r = requests.put(url = url_create, headers = {'User-Agent': 'Bhatti'}, json=data)
#data = r.json()
print(data)
print(r.status_code)
print(r.text)