# Pokemon Game??? 

# Imports 
from pokemon_team import Pokemon
from pokedex import pokedex_list

# Initialize Variables 

# Introduction 
print("Welcome to Pokemon")

# Choose Starter Pokemon
starter_Pokemon = False
while not starter_Pokemon:
    starter = input("Choose your starter [CHARMANDER] [BULBASAUR] [SQUIRTLE] ")

    for entry in pokedex_list:  # Checks every Pokemon in Pokedex
        if starter.capitalize() == entry.name:
            user_pokemon_1 = Pokemon(entry.ID, entry.name, entry.type, entry.description, entry.moves)  # Creates Pokemon Object with the right settings
            starter_Pokemon = True
        


