# Pokedex Module (NamedTuple just kidding)

from collections import namedtuple

Pokemon_entry = namedtuple("Pokemon_entry", "ID name type description, moves")

BULBASAUR = Pokemon_entry(ID="001", name="Bulbasaur", type="Grass", description="Grass mon", moves=["Tackle", "Growl", "Vine Whip", None])
CHARMANDER = Pokemon_entry(ID="004", name="Charmander", type="Fire", description="Fire mon", moves=["Scratch", "Growl", "Ember", None]) 
SQUIRTLE = Pokemon_entry(ID="007", name="Squirtle", type="Water", description="Water mon", moves=["Tackle", "Tail Whip", "Water Gun", None])

pokedex = [BULBASAUR, CHARMANDER, SQUIRTLE]

# Prints Pokedex 
def read_pokedex():
    for entry in pokedex:
        print(f'{entry.ID} - {entry.name}')

read_pokedex()

# Add Pokemon to Pokedex?