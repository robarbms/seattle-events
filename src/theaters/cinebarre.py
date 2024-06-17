from bs4 import BeautifulSoup
from utils import getPage

def getCinebarre ():
    url = 'https://www.regmovies.com/theatres/regal-cinebarre-mountlake-1958'
    response = getPage(url)

    theater = {
        'name': 'Cinebarre',
        'distance': '2.1mi',
        'travelTime': 10
    }

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
        theater['movies'] = movies

    return theater
