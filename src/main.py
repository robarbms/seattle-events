from theaters.getTheaters import getTheaters
from events.getEvents import getEvents
from food.getFood import getFood
from food.ridgecrest import getRidgecrest

def main():
    theaterInfo = getTheaters()
    eventInfo = getEvents()
    foodInfo = getFood()

    data = {
        'movies': theaterInfo,
        'events': eventInfo,
        'food': foodInfo
    }

if __name__ == "__main__":
    main()
    pass
