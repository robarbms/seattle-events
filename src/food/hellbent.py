from bs4 import BeautifulSoup
from utils import getPage, getDate
import re

def getHellbent():

    hellbent = {
        'name': 'Hellbent Brewing Company',
        'url': 'https://hellbentbrewingcompany.com/',
        'location': {
            'distance': 3,
            'travelTime': 15,
        },
        'data-options': {
            'url': 'https://hellbentbrewingcompany.com/food-trucks/',
            'frequency': 30 * 24 * 60, # Fetch once per month
            'last_updated': getDate()
        },
        'trucks': [],
    }

    foodTruckCalendar = getPage(hellbent['data-options']['url'])

    if isinstance(foodTruckCalendar, BeautifulSoup):
        for truck in foodTruckCalendar.find_all('li', {'class': 'simcal-event'}):
            title = truck.find('span', {'class': 'simcal-event-title'}).text
            data = truck.find_all('p')
            date_time = data[1].find_all('span')
            date = re.match(r'^([a-zA-Z]*) (\d{1,2}), (\d{4})', date_time[0].text)
            month = date[1]
            day = date[2]
            year = date[3]
            start = date_time[1].text
            end = date_time[2].text
            hellbent['trucks'].append({
                'title': title,
                'date': {
                    'day': day,
                    'month': month,
                    'year': year,
                },
                'start_time': start,
                'end_time': end
            })
    return hellbent