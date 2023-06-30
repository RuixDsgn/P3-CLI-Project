from ipdb import set_trace
from db.classes.traveler import Traveler
from db.classes.destination import Destination
from db.classes.adventure import Adventure

# The helper file is where we will define all of our functions
def main_menu():
    # Print the menu options
    menu_options = ('1', '2', '3', '4', 'X')
    print(f'''
          1. Go on an Adventure!
          2. View all Adventures
          3. View all Travelers
          4. View all Destinations
          X. Exit PyTrip
          ''')