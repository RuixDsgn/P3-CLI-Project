from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/db/travel_log.db')
CURSOR = CONN.cursor()

class Traveler:

    all_travelers = []
    
    def __init__(self, traveler):
        self.traveler = traveler
        Traveler.all_travelers.append(self)

    def __repr__(self):
        return self.__dict__

    @property 
    def traveler(self):
        return self._traveler

    @traveler.setter
    def traveler(self, traveler):
        if isinstance(traveler, str) and len(traveler) in range(1, 21):
            self._traveler = traveler
        else:
            raise Exception("Traveler must be a string between 1 and 20 characters.")
        
        