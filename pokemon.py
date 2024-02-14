# Pokemon Game??? 

# Imports 
from pokemon_team import Pokemon
from pokedex import pokedex

# Initialize Variables 

# Introduction 
print("Welcome to Pokemon")

# Choose Starter Pokemon
while True:
    starter = input("Choose your starter [CHARMANDER] [BULBASAUR] [SQUIRTLE] ")

    if starter.upper() in pokedex:
        print("name", starter.name)
        # user_pokemon_1 = Pokemon(starter)
        # print("user pokemon", user_pokemon_1.name)
        # break
        


