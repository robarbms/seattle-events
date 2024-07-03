from bs4 import BeautifulSoup
from utils import getPage, getMonthDigit, getDate
import re

def getLFPTC():
    lfptc = {
        'name': 'Town Center at Lake Forest Park',
        'url': 'https://www.thirdplacecommons.org/',
        'location': {
            'distance': 0.9,
            'travelTime': 5,
        },
        'data-options': {
            'url': 'https://www.thirdplacecommons.org/calendar/',
            'frequency': 30 * 24 * 60, # Fetch once per month
            'checked': getDate()
        },
        'links': [
            {
                'name': 'Town Center at Lake Forest Park',
                'url': 'https://www.towncenteratlakeforest.com/'
            },
            {
                'name': 'Third Place Commons',
                'url': 'https://www.thirdplacecommons.org/'
            }
        ],
        'events': [],
        'music': []
    }

    eventsFeed = getPage('https://www.calendarwiz.com/calendars/rssfeeder.xml?crd=thirdplacecommonsevents&len=200&days=30&events=100&title=Third%20Place%20Commons%20Calendar%20Events&cat=25374')
    if isinstance(eventsFeed, BeautifulSoup):
        for event in eventsFeed.find_all('item'):
            title_text = event.find('title').text
            date_time_stamp = re.match(r'^\d{2}\.\d{2}\.\d{2} \d{1,2}:\d{2}', title_text)
            title_no_stamp = title_text.replace(date_time_stamp[0], '')
            title = re.match(r' *(.*(?= \- (Mon|Tue|Wed|Thu|Fri|Sat|Sun)))', title_no_stamp)[0]
            event_info = title_no_stamp.replace(title, '')
            date_time = re.match(r' \- (Mon|Tue|Wed|Thu|Fri|Sat|Sun), (([a-zA-Z]{3}) (\d{1,2})), (\d{4}) (\d{1,2}:\d{2}(am|pm)) - (\d{1,2}:\d{2}(am|pm)) @ (.*)', event_info)
            weekday = date_time[1]
            month_day = date_time[2]
            month = getMonthDigit(date_time[3])
            day = date_time[4]

            year = date_time[5]
            start = date_time[6]
            end = date_time[8]
            location = date_time[10]
            title = title.strip()

            event = {
                'title': title,
                'date': {
                    'day': day,
                    'month': month,
                    'year': year
                },
                'start_time': start,
                'end_time': end,
                'location': location
            }

            lfptc['events'].append(event)
        
    musicFeed = getPage('https://www.calendarwiz.com/calendars/rssfeeder.xml?crd=thirdplacecommonsevents&len=200&days=30&events=100&title=Third%20Place%20Commons%20Calendar%20Events&cat=34461')
    if isinstance(musicFeed, BeautifulSoup):
         for entry in musicFeed.find_all('item'):
            title_text = entry.find('title').text
            date_time_stamp = re.match(r'^\d{2}\.\d{2}\.\d{2} \d{1,2}:\d{2}', title_text)
            title_no_stamp = title_text.replace(date_time_stamp[0], '')
            title = re.match(r' *(.*(?= \- (Mon|Tue|Wed|Thu|Fri|Sat|Sun)))', title_no_stamp)[0]
            event_info = title_no_stamp.replace(title, '')
            date_time = re.match(r' \- (Mon|Tue|Wed|Thu|Fri|Sat|Sun), (([a-zA-Z]{3}) (\d{1,2})), (\d{4}) (\d{1,2}:\d{2}(am|pm)) - (\d{1,2}:\d{2}(am|pm)) @ (.*)', event_info)
            weekday = date_time[1]
            month_day = date_time[2]
            day = date_time[4]
            title = title.strip()
            title = title.replace(' - Live Music brought to you by Third Place Commons!', '')
            title_parts = re.match(r'^(.*)( \- )([^\-]*)$', title)
            if (title_parts):
                print(title_parts)
                band = title_parts[1]
                genre = title_parts[3]
                year = date_time[5]
                start = date_time[6]
                end = date_time[8]
                location = date_time[10]

                music = {
                    'title': title,
                    'band': band,
                    'genre': genre,
                    'date': {
                        'day': day,
                        'month': month,
                        'year': year
                    },
                    'start_time': start,
                    'end_time': end,
                    'location': location
                }

                lfptc['events'].append(music)

    return lfptc
