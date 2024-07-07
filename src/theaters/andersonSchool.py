from bs4 import BeautifulSoup
from utils import getPage, getDate

def getAndersonSchool():
    andersonSchool = {
        'name': 'Anderson School Theater',
        'url': 'https://www.mcmenamins.com/anderson-school',
        'location': {
            'distance': 5.2,
            'travelTime': 25,
        },
        'data-options': {
            'url': 'https://www.mcmenamins.com/anderson-school/anderson-school-theater',
            'frequency': 24 * 60,
            'last_updated': getDate()
        }
    }
    response = getPage(andersonSchool['data-options']['url'])

    if isinstance(response, BeautifulSoup):
        soup = response
        movies = []

        movie_wrapper = soup.find_all('div', {'class': 'tm-card-content'})[1]
        title = movie_wrapper.find('h4').text

        times = []
        movie_times = movie_wrapper.find_all('button')

        for time in movie_times:
            times.append(time.text)

        movies.append({
            'title': title,
            'times': times
        })

        andersonSchool['movies'] = movies
    
    return andersonSchool
