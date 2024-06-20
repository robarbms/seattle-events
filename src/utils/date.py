from datetime import date, datetime

# List of months as a helper for functions
months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Takes either a full month name (ie. "January") or truncated (ie. "Jan") and returns the month number 1-12
def getMonthDigit(str):
    for x in range(0, len(months)):
        month = months[x]
        if month.startswith(str):
            return x + 1

def getDate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")