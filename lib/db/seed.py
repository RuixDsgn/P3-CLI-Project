from ipdb import set_trace
from classes.traveler import Traveler
from classes.destination import Destination
from classes.adventure import Adventure

if __name__ == "__main__":

    Adventure.drop_table()
    Traveler.drop_table()
    Destination.drop_table()

    Adventure.create_table()
    Traveler.create_table()
    Destination.create_table()

    t1 = Traveler("Layne")
    t2 = Traveler("Carla")
    t3 = Traveler("Louis")

    d1 = Destination("Japan")
    d2 = Destination("Brazil")
    d3 = Destination("Germany")

    t1.save()
    t2.save()
    t3.save()

    d1.save()
    d2.save()
    d3.save()

    a1 = Adventure("Plane", 500, t1.id, d1.id)
    a2 = Adventure("Car", 800, t2.id, d2.id)
    a3 = Adventure("Boat", 1500, t3.id, d3.id)

    # set_trace()

    a1.save()
    a2.save()
    a3.save()

  



