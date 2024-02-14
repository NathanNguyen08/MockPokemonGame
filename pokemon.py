# Pokemon Game??? 

# Imports 
from pokemon_team import Pokemon
from pokedex import pokedex_list
from pokemon_team import bag

# Initialize Variables 

# Introduction 
def introduction_cutscene():
    print("Hello there!\nWelcome to the world of POKEMON ")
    # What is your name, gender


# Choose Starter Pokemon
def i_choose_you():
    starter_Pokemon = False
    while not starter_Pokemon:
        starter = input("Choose your starter [CHARMANDER] [BULBASAUR] [SQUIRTLE] ")

        if starter not in pokedex_list:
            error_message()
            continue

        for entry in pokedex_list:  # Checks every Pokemon in Pokedex
            if starter.capitalize() == entry.name:
                print(f'You chose the {entry.type}y Pokemon {entry.name}!!')
                print("Now go out and explore the wonderful world of POKEMONN")
                starter_Pokemon = True
                return Pokemon(entry.ID, entry.name, entry.type, entry.description, entry.moves)  # Creates Pokemon Object with the right settings     

# Home Function
def home(shoes_aquired):
    if not shoes_aquired:
        input("You slowly walked back to your mom's house and entered the front door ")
        input("Mom: Hi honey! Here, take some running shoes before you leave! ")
        input("[You have obtained the Basic Running Shoes! You can now escape wild Pokemon.] ")
    else:
        input("You walk up to the front door of your mom's house... But it's locked! ")
    return True


# Shop Function
def shop():
    shopKey = True
    continue_shopping = "yes"

    while shopKey:
        item = input("What would you like to buy today? [POKEBALLS] [POTIONS] ").capitalize()

        if item not in bag:
            error_message()
            continue

        for item_name, item_count in bag.items():
            if item == item_name:
                item_count += 1
                bag.update({item_name: item_count})
                print(f'PURCHASED x1 {item_name.upper()}')  # Maybe let users buy multiple ? 

        continue_shopping = input("Would you like to continue shopping? ").lower()
        if continue_shopping == "yes":
            continue 
        elif continue_shopping == "no":
            break
        else:
            error_message()



# Route 1
def route_1():
    pass


# Pallet Town 
def pallet_town():
    pallet_town_options = ["Home", "Shop", "Route1"]
    pallet_town = True
    been_to_mom_house = False

    while pallet_town:
        user_option = input("\nWhere would you like to go? [HOME] [SHOP] [ROUTE1] ").capitalize()
        if user_option in pallet_town_options:
            if user_option == "Home":
                running_shoes = home(been_to_mom_house)
                been_to_mom_house = True
            elif user_option == "Shop":
                shop()
            elif user_option == "Route1":
                route_1()
                pallet_town = False


# Pokemon Battle
def battle():
    pass


# Error Statement
def error_message():
    input("Error. Invalid Input.\n")


# If name is main
if __name__ == "__main__":
    # introduction_cutscene()
    # user_pokemon_1 = i_choose_you()
    pallet_town()

        


