import subprocess
import random
import os
count = 0

# cities = ['BCN', 'DUB', 'MUC', 'PAR', 'MAD', 'BER', 'FRA', 'DUB', 'JFK', 'BOS', 'JHB', 'TLS', 'NCE', 'WAW', 'AMS', 'BRU','CRL', 'NYC']
cities = ['BRU', 'MAD','MUC', 'BCN', 'FRA', 'PAR', 'BOS', 'TLS']

while True:
    child = subprocess.Popen(['python',"scraping.py"], stdin=subprocess.PIPE)
    # child.communicate(random.choice(cities))
    child.communicate(os.linesep.join(["LHR", "FRA", "2015-03-04", "2015-03-05", 'u2']))
    count +=1
    print 'count is: %d' % count

