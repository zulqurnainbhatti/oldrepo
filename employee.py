import sys

import requests
#from requests.auth import HTTPBasicAuth

employer_url = "http://dummy.restapiexample.com/api/v1/employees"

r = requests.get(url=employer_url, headers={'User-Agent': 'Bhatti'})

data = r.json()

print(r.status_code)
print(r)

print(data['status'])
print(data['data'])

#
# for status in data:
#     print(status[0])


    # print("ID: " + status['id'])
    #
    # print("Name: " + status['employee_name'])
    #
    # print("Salary:" + status['employee_salary'])
    #
    # print("Age:" + status['employee_age'])
    #
    # print("------------------")