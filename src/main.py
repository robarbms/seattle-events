from theaters.getTheaters import getTheaters
from events.getEvents import getEvents
from food.getFood import getFood
import json
import os

def main():
    outDir = 'output/'
    fileName = 'events.json'
    filePath = os.path.join(outDir, fileName)

    # Load output file if it exists
    if (os.path.exists(filePath)):
        print("Found output file: ", filePath)
        pass
    else:
        theaterInfo = getTheaters()
        eventInfo = getEvents()
        foodInfo = getFood()

        data = {
            'movies': theaterInfo,
            'events': eventInfo,
            'food': foodInfo
        }
        with open(filePath, 'w') as f:
            json.dump(data, f, indent=4)

        print("JSON data has been written to", filePath)

if __name__ == "__main__":
    main()

