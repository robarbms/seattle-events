from .cinebarre import getCinebarre
from .andersonSchool import getAndersonSchool

"""
    Fetches theater information
"""

def getTheaters():
    theaters = []
    theaters.append(getCinebarre())
    theaters.append(getAndersonSchool())

    return theaters
