from ipdb import set_trace
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
    a2 = Adventure("Carla", "Brazil", "Car", 800)
    a3 = Adventure("Louis", "Germany", "Boat", 1500)

    a1.save()
    a2.save()
    a3.save()

