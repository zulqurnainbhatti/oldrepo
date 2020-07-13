import requests
Link = "http://api.deutschebahn.com/stada/v2/stations"
Stadt = input("Stadt eingeben: ")
r = requests.get(url=Link, headers = { "Authorization" : "Bearer cb009ba13126158ad3a38f886a463a41" })
data = r.json()

for line in data['result']:
    if Stadt in line['name']:
        print(line['name'])
        print(line['number'])
        id = line['number']

Link2 = "http://api.deutschebahn.com/stada/v2/stations/" + str(id)
r = requests.get(url=Link2, headers = { "Authorization" : "Bearer cb009ba13126158ad3a38f886a463a41" })
print("-----------------")
data = r.json()
#print(data)
#print(r.status_code)

for line in data['result']:
    if line['hasParking'] is True:
        print("Es gibt Parkplätze")
    else:
        print("Es gibt keine Parkplätze")

    if line['hasPublicFacilities'] is True:
        print("Es hat öffentliche Einrichtungen")
    else:
        print("Es hat keine öffentliche Einrichtungen")

    if line['hasWiFi'] is True:
        print("Es gibt WiFi")
    else:
        print("Es gibt keine WiFi")

    if line['hasTaxiRank'] is True:
        print("Es gibt Taxi Haltestelle")
    else:
        print("Es gibt keine Taxi Haltestelle")

    print(line['hasMobilityService'])
    print(line['timeTableOffice']['email'])
    print(line['szentrale']['name'])
    print(line['szentrale']['publicPhoneNumber'])
    print(line['localServiceStaff']['availability'])
