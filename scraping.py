import dryscrape
from bs4 import BeautifulSoup
import datetime
import requests
import json
from webkit_server import Server
from time import sleep
import random

total_count = 0
empty_count = 0


def get_data(base, to, depart_date, return_date ,stops=0, time_out='1800-2400', time_in='1800-2400', airline='BA'):
    '''you need to be able to put a list of airports of just one aiport into this function'''
    if type(base) is list:
        base = ','.join(map(str, base))
    if type(to) is list:
        to = ','.join(map(str, to))
    url = 'https://www.google.co.uk/flights/#search;f=%s;t=%s;d=%s;r=%s;s=%s;ti=t%s,t%s;a=%s' % (base, to, depart_date, return_date, stops, time_out, time_in, airline)
    sess = dryscrape.Session()
    sess.set_attribute('auto_load_images', False)
    sess.set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
    sess.visit(url)
    sleep(10)
    print url
    print sess.status_code()

    return sess.body(), base, to


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





destination = raw_input('what airport would you like to go to: ')
origin = raw_input('what airport do you want to fly from: ')
leaving_date = raw_input('what is your leaving date: ')
returning_date = raw_input('what is your returing date: ')
airline = raw_input('what airline are you flying: ')
body = get_data(origin, destination, leaving_date, returning_date, '0', '1800-2400', '1800-2400', airline)
data = make_dict(body[0], body[1], body[2])

