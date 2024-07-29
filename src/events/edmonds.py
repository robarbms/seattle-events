from bs4 import BeautifulSoup, element
from utils import getPage, getDate


def getEdmonds():
    edmonds = {
        'title': 'Edmonds',
        'url': 'https://exploreedmonds.com/',
        'location': {
            'distance': 6.5,
            'travelTime': 25
        },
        'data-options': {
            'url': 'https://exploreedmonds.com/events/',
            'frequency': 24 * 60, # Fetch once per month
            'last_updated': getDate()
        },
        'events': []
    }


    edmondsFeed = getPage(edmonds['url'])
    if isinstance(edmondsFeed, BeautifulSoup):
        for event in edmondsFeed.find_all('article'):
            hasDate = event.find('time')
            if hasDate:
                date = hasDate.text
                dateTimeParts = date.split('T')
                dateParts = dateTimeParts[0].split('-')
                time = event.find('h5', {'class': 'post-author'}).text
                title = event.find('h5', {'class': 'post-title'}).text
                description = event.find('p')
                if isinstance(description, element.Tag):
                    description = description.text
                edmonds['events'].append({
                    'title': title,
                    'time': time,
                    'date': {
                        'day': int(dateParts[2]),
                        'month':int(dateParts[1]),
                        'year': int(dateParts[0])
                    },
                    'description': description
                })

    return edmonds
