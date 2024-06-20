from bs4 import BeautifulSoup
from utils import getPage, getDate

def getCinebarre ():
    cinebarre = {
        'name': 'Cinebarre',
        'url': 'https://www.regmovies.com/theatres/regal-cinebarre-mountlake-1958',
        'location': {
            'distance': 2.1,
            'travelTime': 10,
        },
        'data-options': {
            'url': 'https://www.regmovies.com/theatres/regal-cinebarre-mountlake-1958',
            'frequency': 24 * 60,
            'last_updated': getDate()
        }
    }
    response = getPage(cinebarre['url'])

    if (isinstance(response, BeautifulSoup)):
        soup = response
        movies = []

        for movie_wrapper in soup.find_all('div', {'class': 'epue2pm32'}):
            type = movie_wrapper.find('div', {'class': 'epue2pm35'})
            isPreorder = type.text.lower().find('pre-order') >= 0
        
            if not isPreorder:
                title = movie_wrapper.find('h4').text
                print("Found movie: ", title)
                print("Getting movie times...")
                times = movie_wrapper.find_all('button', { 'class': 'epue2pm30'})
                print("Found ", len(times), " show times")
                timeStrings = []
                for time in times:
                    timeStrings.append(time.text)
                movies.append({
                    'title': title,
                    'times': timeStrings
                })
        cinebarre['movies'] = movies

    return cinebarre
