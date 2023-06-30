from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/db/travel_log.db')
CURSOR = CONN.cursor()

class Destination:

    all_destinations = []
    
    def __init__(self, destination):
        self.destination = destination
        Destination.all_destinations.append(self)

    @property 
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        if isinstance(destination, str) and len(destination) in range(1, 21):
            self._destination = destination
        else:
            raise Exception("Location must be a string between 1 and 20 characters.")