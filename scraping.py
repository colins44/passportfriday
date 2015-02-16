import dryscrape
from bs4 import BeautifulSoup
import datetime
import requests
import json
from webkit_server import Server
from time import sleep
import random

def get_data(base, to, depart_date, return_date ,stops=0, time_out='1800-2400', time_in='1800-2400'):
    '''you need to be able to put a list of airports of just one aiport into this function'''
    if type(base) is list:
        base = ','.join(map(str, base))
    if type(to) is list:
        to = ','.join(map(str, to))
    url = 'https://www.google.co.uk/flights/'
    visit = '#search;f=%s;t=%s;d=%s;r=%s;s=%s;ti=t%s,t%s' % (base, to, depart_date, return_date, stops, time_out, time_in)
    sess = dryscrape.Session(base_url=url)
    sess.set_attribute('auto_load_images', False)
    sess.set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
    sess.visit(visit)
    print sess.status_code()
    sleep(5)
    body =  sess.body()
    sess.reset()
    print url

    return body, base, to


def make_dict(body, base, to):
    '''function takes the html body of the webpage to be scraped and retuns
    a dict ready to be posted to the API'''
    soup = BeautifulSoup(body, 'html.parser')
    prices = soup.findAll("div", { "class" : "KFHXXID-c-ob" })
    airlines = soup.find_all('div', {'class': "KFHXXID-c-j"})
    routes = soup.find_all('div', {'class': "KFHXXID-c-wb"})
    times = soup.find_all('span',{'tooltip':True})
    departure_times = times[::2]
    arrival_times = times[1::2]
    flight_times = soup.find_all('div', {'class': "KFHXXID-c-y"})
    flights = {}
    for price in prices:
        index = prices.index(price)
        # route = routes[index].contents[0].split('-')
        flight = {
        'airline': airlines[index].contents[0],
        'price': prices[index].contents[0],
        'departure_time': departure_times[index].contents[0],
        'departure_airport': base,
        'flight_time': flight_times[index].contents[0],
        'arrival_time': arrival_times[index].contents[0],
        'arrival_airport': to,
        }
        flights[index] = flight
    print flights
    return flights

airports = ['CDG', "TXL", 'SXF', 'BER', 'PAR', 'BCN', 'YJB', 'MAD', 'XOC', 'DUB', 'MUC', 'AGB', 'PMI', 'LIS', 'POA']

while True:
    to_city = random.choice(airports)
    body = get_data('LHR', to_city, '2015-02-24', '2015-02-27', '0', '1800-2400', '1800-2400')
    data = make_dict(body[0], body[1], body[2])
    sleep(30)


# to_city = raw_input('what city would you like to go to: ')
# body = get_data('LHR', to_city, '2015-02-24', '2015-02-27', '0', '1800-2400', '1800-2400')
# data = make_dict(body[0], body[1], body[2])
# data = json.dumps(data)
# url = 'http://192.168.57.102:8000/admin/'
# r = requests.post(url, data=json.dumps(data))


