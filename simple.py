from bs4 import BeautifulSoup
import requests
from pandas import DataFrame


def datascrap():
    r = requests.get("https://www.python.org/events/python-events")
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    event_list = [elem.find('a').contents[0] for elem in soup.find_all('h3', {'class': 'event-title'})]

    time_list = [elem.contents[0] for elem in soup.find_all('time')]

    location_list = [elem.contents[0] for elem in soup.find_all('span', {'class': 'event-location'})]

    return event_list, time_list, location_list


def output():
    dff = DataFrame({'Event': ds[0], 'Where': ds[2], 'When': ds[1]})

    dff.to_excel('test.xlsx', sheet_name='sheet1', index=False)


ds = datascrap()
output()
