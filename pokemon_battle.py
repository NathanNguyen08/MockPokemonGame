# Pokemon Battles (Keeps code less cluttered)

# Imports 
from pokemon_general_commands import error_statement
from pokemon_team import user_team

battle_options = ["Fight", "Bag", "Pokemon", "Run"]

def fight_option(user_poke, encounter_poke):
    print(user_poke.moves)  # Prints list of Pokemno moves
    user_move = input(f'What would {user_poke.name} like to do? ')
    print("Current hpeaoa", encounter_poke.stats["HP"])
    encounter_poke.stats["HP"] -= 30
    print("Current hpeaoa", encounter_poke.stats["HP"])

    
def bag_option():
    pass
def pokemon_option():
    pass
def run_option():
    pass


def battle(wild_pokemon: object): 
    battle_key = True
    input(f'You encountered a {wild_pokemon.name}! ')
    user_current_pokemon = user_team[0]

    while battle_key:
        user_option = input("What would you like to do? [FIGHT] [BAG] [POKEMON] [RUN] ").capitalize()
        
        try:
            if user_option == battle_options[0]:  # Fight
                print(f'I choose you: {user_current_pokemon.name}!')  # First Pokemon's Name 
                fight_option(user_current_pokemon, wild_pokemon)
            elif user_option == battle_options[1]: # Bag
                bag_option()
            elif user_option == battle_options[2]: # Pokemon
                pokemon_option()
            elif user_option == battle_options[3]:  # Run
                run_option()
            else:
                raise Exception

        except Exception:
            error_statement()



    
