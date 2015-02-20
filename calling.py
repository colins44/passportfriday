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
    child = subprocess.Popen(['python',"scraping.py"], stdin=subprocess.PIPE)

    child.communicate(os.linesep.join([x['outbound_flight']['departure_airport'], x['outbound_flight']['arrival_airport'], x['outbound_flight']['departure_time'][:10], x['inbound_flight']['departure_time'][:10], x['outbound_flight']['carrier_code'], str(x['pk'])]))
    print '$$$$$$$$$'
    print '$$$$$$$$$'
    print '$$$$$$$$$'
    print '$$$$$$$$$'
    print x['outbound_flight']