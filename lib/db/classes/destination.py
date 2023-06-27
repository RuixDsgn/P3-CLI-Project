from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Destination:

    all_destinations = []
    
    def __init__(self, location):
        self.location = location
        Destination.all_destinations.append(self)

    @property 
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location) in range(1, 21):
            self._location = location
        else:
            raise Exception("Location must be a string between 1 and 20 characters.")