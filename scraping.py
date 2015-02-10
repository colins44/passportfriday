import dryscrape
from bs4 import BeautifulSoup
import datetime
import requests
import json
from time import sleep

def get_data(base, to, depart_date, return_date ,stops=0, time_out='1800-2400', time_in='1800-2400'):
    '''you need to be able to put a list of airports of just one aiport into this function'''
    if type(base) is list:
        base = ','.join(map(str, base))
    if type(to) is list:
        to = ','.join(map(str, to))
    url = 'https://www.google.co.uk/flights/#search;f=%s;t=%s;d=%s;r=%s;s=%s;ti=t%s,t%s' % (base, to, depart_date, return_date, stops, time_out, time_in)
    sess = dryscrape.Session(base_url=url)
    sess.set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
    sess.visit('')
    sleep(1)
    print url
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


to_city = raw_input('what city would you like to go to: ')
body = get_data('LHR', to_city, '2015-02-24', '2015-02-27', '0', '1800-2400', '1800-2400')
data = make_dict(body[0], body[1], body[2])
# data = json.dumps(data)
# url = 'http://192.168.57.102:8000/admin/'
# r = requests.post(url, data=json.dumps(data))


# sess = dryscrape.Session(base_url = 'https://www.google.co.uk/flights/#search;f=LHR;t=CDG;d=2015-02-24;r=2015-02-27;s=0;ti=t0600-2400,t0600-2400')
# sess.set_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
# sess.visit('')
# body = sess.body()
# soup = BeautifulSoup(body, 'html.parser')
# prices = soup.findAll("div", { "class" : "KFHXXID-c-ob" })
# times = soup.find_all('span',{'tooltip':True}) #returns a list twice as long, one value from leaving another for arrival time
# airlines = soup.find_all('div', {'class': "KFHXXID-c-j"})
# route = soup.find_all('div', {'class': "KFHXXID-c-wb"})
# length = soup.find_all('div', {'class': "KFHXXID-c-y"})
#
# ''''now make into a dict for posting to the passprt fridays api'''
#
# for price in prices:
#     index = prices.index(price)
#     post = {
#         'price': price,
#         'airline': airlines(index),
#         'departure_time': departure_time,
#         'departure_airport': departure_airport,
#         'arrival_airport': arrival_airport,
#         'arrival_time': arrival_time,
#         'flight_time': length(index),
#     }

#
# search_term = 'dryscrape'
#
# # set up a web scraping session
# sess = dryscrape.Session(base_url = 'http://192.168.57.102:8000/')
#
# # visit homepage and search for a term
# sess.visit('/admin/')
# q = sess.at_xpath('//*[@name="q"]')
# q.set(search_term)
# q.form().submit()
#
# for link in sess.xpath('//a[@href]'):
# for link in sess.xpath("//h3"):
# for link in sess.xpath("//*[contains(@class, 'KFHXXID-c-ob')]"):
#     print link['href']
# sess.at_css('.KFHXXID-c-ob')
#   print link['href']
