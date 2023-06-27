from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Adventure:

    all_adventures = []

    def __init__(self, traveler, location, transportation): #set validation for transportation to include driving, walking, boat, plane, time machine
        self.traveler = traveler
        self.location = location
        self.transportation = transportation
        Adventure.all_adventures.append(self)