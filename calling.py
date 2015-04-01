import subprocess
import random
import os
import requests
import json
count = 0
#
# # cities = ['BCN', 'DUB', 'MUC', 'PAR', 'MAD', 'BER', 'FRA', 'DUB', 'JFK', 'BOS', 'JHB', 'TLS', 'NCE', 'WAW', 'AMS', 'BRU','CRL', 'NYC']
# cities = ['BRU', 'MAD','MUC', 'BCN', 'FRA', 'PAR', 'BOS', 'TLS']
#
# while True:
#     child = subprocess.Popen(['python',"scraping.py"], stdin=subprocess.PIPE)
#     # child.communicate(random.choice(cities))
#     child.communicate(os.linesep.join(["LHR", "FRA", "2015-03-04", "2015-03-05", 'u2']))
#     count +=1
#     print 'count is: %d' % count

url = 'http://192.168.59.103:8000/api/routes/'
r = requests.get(url)
data = json.loads(r.content)

for x in data['objects']:
    for inbound_flight in x['inbound_flights']:
        return_date = inbound_flight['departure_time'][:10]

    for x in x['outbound_flights']:
        print x
        child = subprocess.Popen(['python',"scraping.py"], stdin=subprocess.PIPE)

        child.communicate(os.linesep.join([x['departure_airport'], x['arrival_airport'], x['departure_time'][:10], return_date, x['carrier_code'], str(x['pk'])]))

