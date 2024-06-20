from .lakeForestParkTC import getLFPTC
from .edmonds import getEdmonds

def getEvents():
    events = []
    events.append(getLFPTC())
    events.append(getEdmonds())
    return events
