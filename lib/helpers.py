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
    
    first_input = input("Select an Option by typing in a number: ")
    if first_input in menu_options:
        print(f'You ve selected {first_input}')

        if first_input == "2":
            print_adventure_list(Adventure.get_all())
            main_menu()

    def print_adventure_list(adventure_list):
        for adventure in adventure_list:
      #  display one adventure
            print(f'''
                traveler => {adventure.traveler}
                location => {adventure.destination}
                transportation => {adventure.transportation}
                cost => {adventure.cost}
                
            ''')