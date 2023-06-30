from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/db/travel_log.db')
CURSOR = CONN.cursor()

class Destination:

    all_destinations = []
    
    def __init__(self, destination):
        self.destination = destination
        Destination.all_destinations.append(self)

    def __repr__(self):
        return str(self.__dict__)

    @property 
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        if isinstance(destination, str) and len(destination) in range(1, 21):
            self._destination = destination
        else:
            raise Exception("Location must be a string between 1 and 20 characters.")
        
    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS destination (
                id INTEGER PRIMARY KEY,
                destination TEXT
            )
            """
        CURSOR.execute(create_table_sql)
        print("creating adventure table...")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS destination"
        CURSOR.execute(sql)
        print("dropping table...")

    def save(self):
        sql = """
            INSERT INTO destination (destination)
            VALUES(?)
        """
        params = (self.destination,)
        CURSOR.execute(sql, params)
        CONN.commit()
        print(self)

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, destination):
        new_destination = Destination(destination, )
        new_destination.save()

    @classmethod
    def new_instance_from_db(cls, row):
        return cls(
            id=row[0],
            destination=row[1],
            
        )


    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM destination"
        response = CURSOR.execute(sql)
        all_destination_list = response.fetchall()
        return [Destination.new_instance_from_db(row) for row in all_destination_list]
    
    @classmethod
    def find_by_destination(cls, search):
        sql = """
            SELECT * FROM adventures WHERE destination = ?
        """
        response = CURSOR.execute(sql, (search, ))
        row = response.fetchone()
        return Destination.new_instance_from_db(row)
    
    @classmethod
    def find_by_id(cls, search_id):
        sql = """
            SELECT * FROM destinations WHERE id = ?
        """
        row = CURSOR.execute(sql, (search_id, )).fetchone()
        return Destination.new_instance_from_db(row)if row else None
