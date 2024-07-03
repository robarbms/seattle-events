from bs4 import BeautifulSoup
from utils import getPage, getMonthDigit, getDate
import re
import json
from datetime import datetime
import time
import requests
from utils.dataCleaning import dataCleaning

def getRidgecrest():

    ridgecrest = {
        'name': 'Ridgecrest Public House',
        'url': 'https://www.ridgecrest.pub/',
        'location': {
            'distance': 2.5,
            'travelTime': 10
        },
        'data-options': {
            'url': 'https://www.ridgecrest.pub/foodtruckcalendar',
            'json-url': lambda month, year: 'https://www.ridgecrest.pub/api/open/GetItemsByMonth?month={month}-{year}&collectionId=5500c4c8e4b02a9dabd0f3c5&crumb=BYkrXApYapcgMjMyZTNlMTQ1MmVlZmFlM2IwZjRlNzgzYzk0NmY4'.format(month=month, year=year),
            'frequency': 30 * 24 * 60, # Fetch once per month
            'last_updated': getDate()
        },
        'trucks': []
    }

    now = datetime.now()

    current_month = now.strftime("%m")
    current_year = now.year
    jsonFeedUrl = ridgecrest['data-options']['json-url'](month=current_month, year=current_year)
    print(jsonFeedUrl)
    request_headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    print("Getting page for {0}...".format(jsonFeedUrl))
    response = requests.get(jsonFeedUrl, headers=request_headers)
    if response.status_code == 200:
        print("Page successfully downloaded.")
        json_doc = response.text
        print("Received {0} bytes.".format(len(json_doc)))
        print("Parsing page...")
        parsed_json = json.loads(json_doc)
        for entry in parsed_json:
            title = entry['title']
            start_date = datetime.fromtimestamp(entry['startDate']/1000),
            start_date = start_date[0]
            end_date = datetime.fromtimestamp(entry['endDate']/1000)
            ridgecrest['trucks'].append({
                'title': title.strip(),
                'date': {
                    'day': start_date.day,
                    'month': start_date.month,
                    'year': start_date.year,
                },
                'start_time': start_date.strftime("%I:%M %p"),
                'end_time': end_date.strftime("%I:%M %p")
            })
        
    return dataCleaning(ridgecrest)