from bs4 import BeautifulSoup
from utils import getPage

def getAndersonSchool():
    url = 'https://www.mcmenamins.com/anderson-school/anderson-school-theater'
    response = getPage(url)

    theater = {
        'name': 'Anderson School Theater',
        'distance': '5.2mi',
        'travelTime': 20
    }

    if (isinstance(response, BeautifulSoup)):
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

        theater['movies'] = movies
    
    return theater
