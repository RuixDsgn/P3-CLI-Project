# from ipdb import set_trace
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
        
    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXIST adventures (
                id INTEGER PRIMARY KEY,
                traveler TEXT,
                )
            """
        CURSOR.execute(create_table_sql)
        print("creating traveler table...")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS adventures"
        CURSOR.execute(sql)
        print("dropping table...")

    def save(self):
        sql = """
            INSERT INTO adventures (traveler)
            VALUES(?)
        """
        params = (self.traveler)
        CONN.commit()
        print(self)

        self.id = CURSOR.lastrowid

    @classmethod
    def create(traveler, id=None):
        new_adventure = Traveler(traveler)
        new_adventure.save()

    @classmethod
    def new_instance_from_db(cls, row):
        return cls(
            id=row[0],
            traveler=row[1]
        )

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM travelers"
        response = CURSOR.execute(sql)
        all_travelers_list = response.fetchall()
        return [Traveler.new_instance_from_db(row) for row in all_travelers_list]
    
    @classmethod
    def find_by_traveler(cls, search):
        sql = """
            SELECT * FROM adventures WHERE traveler = ?
        """
        response = CURSOR.execute(sql, (search, ))
        row = response.fetchone()
        return Traveler.new_instance_from_db(row)
    
    @classmethod
    def find_by_id(cls, search_id):
        sql = """
            SELECT * FROM adventures WHERE id = ?
        """
        row = CURSOR.execute(sql, (search_id, )).fetchone()
        return Traveler.new_instance_from_db(row)if row else None
    
        
        