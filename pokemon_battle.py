# Pokemon Battles (Keeps code less cluttered)

# Imports 
from pokemon_general_commands import error_statement
from pokemon_team import user_team
from pokedex import moves_dictionary
from random import randint

battle_options = ["Fight", "Bag", "Pokemon", "Run"]

def fight_option(user_poke, encounter_poke):
    encounter_hp = encounter_poke.stats["HP"]
    user_poke_hp = user_poke.stats["HP"]
    random_encounter_move = encounter_poke.moves[randint(0, len(encounter_poke.moves))].upper()
    user_chose_move = False

    while True: 
        # User Pokemon Turn
        print(f'\n{user_poke.moves}')  # Prints list of User Pokemon moves
        user_move = input(f'What would {user_poke.name} like to do? ').upper()
        for move_name, move_damage in moves_dictionary.items(): 
            if move_name == user_move:
                input(f'\n{user_poke.name} used {user_move}! It does {move_damage} damage! ')
                encounter_hp -= move_damage
                if encounter_hp <= 0:
                    encounter_hp = 0
                input(f'{encounter_poke.name} has {encounter_hp} left! ')
                if encounter_hp == 0:
                    input(f'{encounter_poke.name} fainted! ')
                    return False
                user_chose_move = True
        # Enemy Pokemon Turn
        if user_chose_move is True:
            for move_name, move_damage in moves_dictionary.items():
                if  random_encounter_move == move_name: 
                    input(f'\n{encounter_poke.name} used {move_name}! It does {move_damage} damage! ')
                    user_poke_hp -= move_damage
                    if user_poke_hp <= 0:
                        user_poke_hp = 0
                    input(f'{user_poke.name} has {user_poke_hp} left! ')
                    if user_poke_hp == 0: 
                        input(f'{user_poke.name} fainted! You blacked out! ')
                        return False

    
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
        
        if user_option == battle_options[0]:  # Fight
            input(f'\nI choose you: {user_current_pokemon.name}!')  # First Pokemon's Name 
            battle_key = fight_option(user_current_pokemon, wild_pokemon)
        elif user_option == battle_options[1]: # Bag
            bag_option()
        elif user_option == battle_options[2]: # Pokemon
            pokemon_option()
        elif user_option == battle_options[3]:  # Run
            run_option()
            # else:
            #     raise Exception

        # except Exception:
        #     error_statement()



    
