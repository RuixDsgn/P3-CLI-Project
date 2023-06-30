from ipdb import set_trace
from faker import Faker
from db.classes.traveler import Traveler
from db.classes.destination import Destination
from db.classes.adventure import Adventure

if __name__ == "__main__":

    Adventure.drop_table()
    Traveler.drop_table()
    Destination.drop_table()

    Adventure.create_table()
    Traveler.create_table()
    Destination.create_table()

    a1 = Adventure("Layne", "Japan", "Plane", 500)
    a2 = Adventure("Carla")
    a3 = Adventure("Louis")

