from ipdb import set_trace
from os import system
from db.classes.traveler import Traveler
from db.classes.destination import Destination
from db.classes.adventure import Adventure
from helpers import *

if __name__ == "__main__":
    system("clear")
    print('''
______    _____    _       
| ___ \  |_   _|  (_)      
| |_/ /   _| |_ __ _ _ __  
|  __/ | | | | '__| | '_ \    
| |  | |_| | | |  | | |_) |
\_|   \__, \_/_|  |_| .__/ 
       __/ |        | |    
      |___/         |_|    
      

      _
         -=\`\
     |\ ____\_\__
   -=\c`""""""" "`)
jgs   `~~~~~/ /~~`
        -==/ /
          '-'
      
    ''')
    print("Welcome to PyTrip!")

main_menu()