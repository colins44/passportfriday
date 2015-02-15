import subprocess
import random
count = 0

# cities = ['BCN', 'DUB', 'MUC', 'PAR', 'MAD', 'BER', 'FRA', 'DUB', 'JFK', 'BOS', 'JHB', 'TLS', 'NCE', 'WAW', 'AMS', 'BRU','CRL', 'NYC']
cities = ['BRU', 'MAD','MUC', 'BCN', 'FRA', 'PAR', 'BOS', 'TLS']

while True:
    child = subprocess.Popen(['python',"scraping.py"], stdin=subprocess.PIPE)
    child.communicate(random.choice(cities))
    count +=1
    print 'count is: %d' % count

