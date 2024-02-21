# Pokemon Game??? 

# Imports 
from random import randint
from pokemon_team import Pokemon
from pokedex import pokedex_list, route_pokemon
from pokemon_team import bag, user_team
from pokemon_battle import battle
from pokemon_general_commands import error_statement

# Initialize Variables


# Introduction 
def introduction_cutscene():
    print("Hello there!\nWelcome to the world of POKEMON ")
    # What is your name, gender


# Saves Pokemon to a file
def pokemon_team_file(pokemon_class):
    pokemon_hp = pokemon_class.stats["HP"]
    file = open("pokemon_team_file", "a")
    file.write(f'{pokemon_class.name} - {pokemon_hp}/{pokemon_hp} HP\n')
    file.close()


# Load Save File Option 


# Choose Starter Pokemon
def i_choose_you():
    starter_Pokemon_acquired = False
    while not starter_Pokemon_acquired:
        starter = input("Choose your starter [CHARMANDER] [BULBASAUR] [SQUIRTLE] ").capitalize()

        # try:
        for entry in pokedex_list:  # Checks every Pokemon in Pokedex (List of all Pokemon)
            if starter == entry.name: #
                print(f'You chose the {entry.type}y Pokemon {entry.name}!!')
                print("Now go out and explore the wonderful world of POKEMONN")
                starter_pokemon = Pokemon(entry.ID, entry.name, entry.type, entry.description, entry.moves, entry.stats)
                pokemon_team_file(starter_pokemon)
                starter_Pokemon_acquired = True
                return starter_pokemon # Creates Pokemon Object with the right settings 
        #     raise Exception # Raises exception if a Pokemon isn't found in Pokedex and object not created
        # except Exception:
        #     error_statement()


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

        if item not in bag: # Error statement for when item can't be found
            error_statement()
            continue

        for item_name, item_count in bag.items(): # bag = {"Pokeballs": 0, "Potions": 0}
            if item == item_name: # Basically finds the item name in the dictionary 
                item_count += 1
                bag.update({item_name: item_count})
                print(f'PURCHASED x1 {item_name.upper()}')  # Maybe let users buy multiple ? 
            
        continue_shopping = input("Would you like to continue shopping? ").lower()

        if continue_shopping == "yes":
            continue 
        elif continue_shopping == "no":
            shopKey = False
        # else:
        #     error_statement()


# Route 1
def route_1():
    encounter_found = False

    while not encounter_found:
        # tile_prob = randint(15, 25) 
        # encounter_prob = randint(0, 255)
        tile_prob = randint(500, 1000) 
        encounter_prob = randint(0, 255)
        if encounter_prob >= tile_prob:
            input("Walking through the grass... ")
        elif encounter_prob < tile_prob:
            user_encounter = route_pokemon("Route 1") # Makes this into a Pokemon Object
            battle(user_encounter)
            continue


# Pallet Town 
def pallet_town():
    pallet_town_options = ["Home", "Shop", "Route1"]
    pallet_town = True
    been_to_mom_house = False

    while pallet_town:
        user_option = input("\nWhere would you like to go? [HOME] [SHOP] [ROUTE1] ").capitalize()

        # try:
        if user_option == "Home":
            running_shoes = home(been_to_mom_house)
            been_to_mom_house = True
        elif user_option == "Shop":
            shop()
        elif user_option == "Route1":
            route_1()
            pallet_town = False
            # else: 
            #     raise Exception
        # except Exception:
        #     error_statement()


# If name is main
if __name__ == "__main__":
    # introduction_cutscene()
    total_pokemon = 0
    user_pokemon_1 = i_choose_you()
    user_team.append(user_pokemon_1)
    pallet_town()
    # route_1()
    print("End code for now")

        


