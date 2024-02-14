# Pokedex Module (NamedTuple just kidding)

from collections import namedtuple

Pokemon_entry = namedtuple("Pokemon_entry", "ID name type description moves")

Bulbasaur = Pokemon_entry(ID="001", name="Bulbasaur", type="Grass", description="Grass mon", moves=["Tackle", "Growl", "Vine Whip", None])
Charmander = Pokemon_entry(ID="004", name="Charmander", type="Fire", description="Fire mon", moves=["Scratch", "Growl", "Ember", None]) 
Squirtle = Pokemon_entry(ID="007", name="Squirtle", type="Water", description="Water mon", moves=["Tackle", "Tail Whip", "Water Gun", None])

pokedex_list = [Bulbasaur, Charmander, Squirtle]

# Prints Pokedex 
def read_pokedex():
    for entry in pokedex_list:
        print(f'{entry.ID} - {entry.name}')

# Add Pokemon to Pokedex?