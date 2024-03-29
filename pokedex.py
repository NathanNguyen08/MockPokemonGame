# Pokedex Module (NamedTuple just kidding)

# Imports
from collections import namedtuple
from random import randrange
from pokemon_team import Pokemon

Pokemon_entry = namedtuple("Pokemon_entry", "ID name type description moves stats")

Bulbasaur = Pokemon_entry(
    ID="001",
    name="Bulbasaur",
    type="Grass",
    description="Grass mon",
    moves=["Tackle", "Growl", "Vine Whip", "None"],
    stats={"MAX HP": 105, "CURRENT HP": 105, "SPD":45})
Charmander = Pokemon_entry(
    ID="004",
    name="Charmander",
    type="Fire",
    description="Fire mon",
    moves=["Scratch", "Growl", "Ember", "None"],
    stats={"MAX HP": 99, "CURRENT HP": 99, "SPD":65})
Squirtle = Pokemon_entry(
    ID="007",
    name="Squirtle",
    type="Water",
    description="Water mon",
    moves=["Tackle", "Tail Whip", "Water Gun", "None"],
    stats={"MAX HP": 104, "CURRENT HP": 104, "SPD":43})
Pidgey = Pokemon_entry(
    ID="016",
    name="Pidgey",
    type="Normal",
    description="Normal and Flying mon",
    moves=["Tackle", "Tail Whip", "Quick Attack", "None"],
    stats={"MAX HP": 100, "CURRENT HP": 100, "SPD":54})
Ratata = Pokemon_entry(
    ID="019",
    name="Ratata",
    type="Normal",
    description="Normal mon",
    moves=["Tackle", "Sand Attack", "Gust", "Quick Attack"],
    stats={"MAX HP": 90, "CURRENT HP": 90, "SPD":72})


# Containers of stuff 
pokedex_list = [Bulbasaur, Charmander, Squirtle, Pidgey, Ratata]
moves_dict = {"NONE": 0, "TACKLE": 20, "GROWL": .15, "VINE WHIP": 30, "EMBER":30, "WATER GUN": 30, 
                    "TAIL WHIP": .15, "QUICK ATTACK": 20, "GUST": 30, "SAND ATTACK": .15} # Quick Attack
health_items_dict = {"POTION": 20, "SUPER POTION": 60, "HYPER POTION": 150}
catch_items_dict = {"POKE BALL": 5, "GREAT BALL": 7, "ULTRA BALL": 9}


# Prints Pokedex 
def read_pokedex():
    for entry in pokedex_list:
        print(f'{entry.ID} - {entry.name}')

# Add Pokemon to Pokedex?
        
# Routes Pokemon 
def route_pokemon(user_route_number):
    routes = {"Route 1": ["Ratata", "Pidgey"],
              "Route 2": ["Ratata", "Pidgey", "Weedle", "Caterpie"]}
    
    for route_name, list_route_pokemon in routes.items():
        if route_name == user_route_number: # Goes through dictionary and finds the route_number that the user is on 
            num_pokemon = len(list_route_pokemon) # Total unique Pokemon here
            route_encounter_name = list_route_pokemon[randrange(0, num_pokemon)].capitalize() # Takes a random Pokemon name from list
            route_encounter_object = initialize_pokemon(route_encounter_name) # Creates an object of that encounter
            return route_encounter_object

# Creates a Pokemon Object
def initialize_pokemon(pokemon_name):
    for entry in pokedex_list:
        if entry.name == pokemon_name:
            return Pokemon(entry.ID, entry.name, entry.type, entry.description, entry.moves, entry.stats)  # Creates Pokemon Object with the right settings     
