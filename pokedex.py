# Pokedex Module (NamedTuple just kidding)

from collections import namedtuple
from random import randrange
from pokemon_team import Pokemon

Pokemon_entry = namedtuple("Pokemon_entry", "ID name type description moves")

Bulbasaur = Pokemon_entry(ID="001", name="Bulbasaur", type="Grass", description="Grass mon", moves=["Tackle", "Growl", "Vine Whip", None])
Charmander = Pokemon_entry(ID="004", name="Charmander", type="Fire", description="Fire mon", moves=["Scratch", "Growl", "Ember", None]) 
Squirtle = Pokemon_entry(ID="007", name="Squirtle", type="Water", description="Water mon", moves=["Tackle", "Tail Whip", "Water Gun", None])
Pidgey = Pokemon_entry(ID="016", name="Pidgey", type="Normal", description="Normal and Flying mon", moves=["Tackle", "Tail Whip", "Quick Attack", None])
Ratata = Pokemon_entry(ID="019", name="Ratata", type="Normal", description="Normal mon", moves=["Tackle", "Sand Attack", "Gust", "Quick Attack"])

pokedex_list = [Bulbasaur, Charmander, Squirtle, Pidgey, Ratata]

# Prints Pokedex 
def read_pokedex():
    for entry in pokedex_list:
        print(f'{entry.ID} - {entry.name}')

# Add Pokemon to Pokedex?
        
# Routes Pokemon 
def route_pokemon(route_number):
    routes = {"Route 1": ["Ratata", "Pidgey"],
              "Route 2": ["Ratata", "Pidgey", "Weedle", "Caterpie"]}
    
    for route_name, list_route_pokemon in routes.items():
        if route_number == route_name:
            num_pokemon = len(list_route_pokemon) # 2 
            route_encounter_name = list_route_pokemon[randrange(0, num_pokemon)]
            route_encounter = initialize_pokemon(route_encounter_name)
            
            return route_encounter

# Creates a Pokemon Object
def initialize_pokemon(pokemon_name):
    for entry in pokedex_list:
        if pokemon_name.capitalize() == entry.name:
            return Pokemon(entry.ID, entry.name, entry.type, entry.description, entry.moves)  # Creates Pokemon Object with the right settings     
    
        