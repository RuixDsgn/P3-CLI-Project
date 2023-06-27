from ipdb import set_trace
from traveler import Traveler
from destination import Destination
from adventure import Adventure

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