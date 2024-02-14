# Pokemon Game??? 

# Imports 
from pokemon_team import Pokemon
from pokedex import pokedex_list

# Initialize Variables 

# Introduction 
def introduction_cutscene():
    print("Welcome to Pokemon")


# Choose Starter Pokemon
def i_choose_you():
    starter_Pokemon = False
    while not starter_Pokemon:
        starter = input("Choose your starter [CHARMANDER] [BULBASAUR] [SQUIRTLE] ")

        for entry in pokedex_list:  # Checks every Pokemon in Pokedex
            if starter.capitalize() == entry.name:
                print(f'You chose the {entry.type}y Pokemon {entry.name}!!')
                print("Now go out and explore the wonderful world of POKEMONN")
                starter_Pokemon = True
                return Pokemon(entry.ID, entry.name, entry.type, entry.description, entry.moves)  # Creates Pokemon Object with the right settings     

# Home Function
def home():
    pass


# Shop Function
def shop():
    pass

# Route 1
def route_1():
    pass


# Pallet Town 
def pallet_town():
    pallet_town_options = ["Home", "Shop", "Route1"]
    pallet_town = True
    while pallet_town:
        user_option = input("Where would you like to go? [HOME] [SHOP] [ROUTE1]").capitalize()
        if user_option in pallet_town_options:
            if user_option == "Home":
                home()
            elif user_option == "Shop":
                shop()
            elif user_option == "Route1":
                route_1()
                pallet_town = False


# Pokemon Battle
def battle():
    pass


# If name is main
if __name__ == "__main__":
    introduction_cutscene()
    user_pokemon_1 = i_choose_you()

        


