from bs4 import BeautifulSoup
from utils import getPage, getDate

def getCrest():
    crest = {
        'name': 'Landmark Crest Cinema Center',
        'url': 'https://www.landmarktheatres.com/our-locations/x00mt-landmark-crest-cinema-center-shoreline/',
        'location': {
            'distance': 2.1,
            'travelTime': 10,
        },
        'data-options': {
            'url': 'https://www.landmarktheatres.com/showtimes/',
            'frequency': 24 * 60,
            'last_updated': getDate()
        },
        'movies': []
    }
    response = getPage(crest['data-options']['url'])

    if (isinstance(response, BeautifulSoup)):
        print(response)
        movie_details = response.find_all('div', {'class': 'css-kg1qlu'});
        print(movie_details)
        for movie in movie_details:
            print(movie)
