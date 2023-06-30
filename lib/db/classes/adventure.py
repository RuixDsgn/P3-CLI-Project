from ipdb import set_trace

import sqlite3

CONN = sqlite3.connect('lib/db/travel_log.db')
CURSOR = CONN.cursor()

class Adventure:

    all_adventures = []

    def __init__(self, transportation, cost, traveler_id, destination_id, id=None): #set validation for transportation to include driving, walking, boat, plane, time machine
        self.transportation = transportation
        self.cost = cost
        self.traveler_id = traveler_id
        self.destination_id = destination_id
        Adventure.all_adventures.append(self)
    
    @property
    def traveler_id(self):
        return self._traveler_id

    @traveler_id.setter
    def traveler_id(self, traveler_id):
        from classes.traveler import Traveler
        if isinstance(traveler_id, int):
            self._traveler_id = traveler_id
        else:
            raise Exception("not good")
        
    
    @property
    def destination_id(self):
        return self._destination_id
    
    @destination_id.setter
    def destination_id(self, destination_id):
        if isinstance(destination_id, int):
            self._destination_id = destination_id
        else:
            raise Exception()

    @property
    def traveler(self):
        return self._traveler

    @traveler.setter
    def traveler(self, traveler):
        from classes.traveler import Traveler
        if isinstance(traveler, Traveler):
            self._traveler = traveler
        else:
            raise Exception()
        
    
    @property
    def destination(self):
        from classes.destination import Destination
        return Destination.find_by_id(self.destination_id)
        
    
    @destination.setter
    def destination(self, destination):
        from classes.destination import Destination
        if isinstance(destination, Destination):
            self._destination = destination
        else:
            raise Exception()

    def __repr__(self):
        return str(self.__dict__)
    
    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS adventures (
                id INTEGER PRIMARY KEY,
                transportation TEXT,
                cost INT,
                traveler_id INT,
                destination_id INT
            )
            """
        CURSOR.execute(create_table_sql)
        print("creating adventure table...")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS adventures"
        CURSOR.execute(sql)
        print("dropping table...")

    def save(self):
        sql = """
            INSERT INTO adventures (transportation, cost, traveler_id, destination_id)
            VALUES(?, ?, ?, ?)
        """
        params = (self.transportation, self.cost, self.traveler_id, self.destination_id)
        CURSOR.execute(sql, params)
        CONN.commit()
        print(self)

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, destination, transportation, cost, id=None):
        new_adventure = Adventure(destination, transportation, cost)
        new_adventure.save()

    @classmethod
    def new_instance_from_db(cls, row):
        return cls(
            id=row[0],
            traveler=row[1],
            destination=row[2],
            transportation=row[3],
            cost=row[4],
            
        )


    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM adventures"
        response = CURSOR.execute(sql)
        all_adventures_list = response.fetchall()
        return [Adventure.new_instance_from_db(row) for row in all_adventures_list]
    
    @classmethod
    def find_by_traveler(cls, search):
        sql = """
            SELECT * FROM adventures WHERE traveller = ?
        """
        response = CURSOR.execute(sql, (search, ))
        row = response.fetchone()
        return Adventure.new_instance_from_db(row)
    
    @classmethod
    def find_by_id(cls, search_id):
        sql = """
            SELECT * FROM adventures WHERE id = ?
        """
        row = CURSOR.execute(sql, (search_id, )).fetchone()
        return Adventure.new_instance_from_db(row)if row else None
    
    
