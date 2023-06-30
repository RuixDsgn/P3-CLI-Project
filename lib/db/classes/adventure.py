from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/db/travel_log.db')
CURSOR = CONN.cursor()

class Adventure:

    all_adventures = []

    def __init__(self, traveler, location, transportation, cost, traveller_id, id =None): #set validation for transportation to include driving, walking, boat, plane, time machine
        self.traveler = traveler
        self.location = location
        self.transportation = transportation
        self.cost = cost
        self.traveller_id = traveller_id
        Adventure.all_adventures.append(self)

    def __repr__(self):
        return self.__dict__

    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXIST adventures (
                id INTEGER PRIMARY KEY,
                traveler TEXT,
                location TEXT,
                transportation TEXT,
                cost INt,
                traveller_id INT
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
            INSERT INTO adventures (traveler, location, transportation, cost, traveller_id)
            VALUES(?, ?, ?, ?, ?)
        """
        params = (self.traveler, self.location, self.transportation, self.cost, self.traveller_id)
        CURSOR.execute(sql, params)
        CONN.commit()
        print(self)

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, location, transportation, cost, traveller_id, id =None):
        new_adventure = Adventure(location, transportation, cost, traveller_id)
        new_adventure.save()

    @classmethod
    def new_instance_from_db(cls, row):
        return cls(
            id=row[0],
            traveler=row[1],
            location=row[2],
            transportation=row[3],
            cost=row[4],
            traveller_id=row[5]
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
    

