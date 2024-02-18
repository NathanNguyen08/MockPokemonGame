# Pokemon Battles (Keeps code less cluttered)

# Imports 
from pokemon_general_commands import error_statement
from pokemon_team import user_team, bag, bag_contents
from pokedex import moves_dict, health_items_dict, catch_items_dict
from random import randint


# Initialized Variables
battle_options = ["Fight", "Bag", "Pokemon", "Run"]


# Functions for battling 
def fight_option(user_poke, encounter_poke):
    encounter_hp = encounter_poke.stats["HP"]
    user_poke_hp = user_poke.stats["HP"]
    random_encounter_move = encounter_poke.moves[randint(0, len(encounter_poke.moves))].upper()
    chosen_action = False

    while True: 
        # User Pokemon Turn
        print(f'\n{user_poke.moves}')  # Prints list of User Pokemon moves
        user_move = input(f'What would {user_poke.name} like to do? ').upper()
        for move_name, move_damage in moves_dict.items(): 
            if move_name == user_move:
                input(f'\n{user_poke.name} used {user_move}! It does {move_damage} damage! ')
                encounter_hp -= move_damage
                if encounter_hp <= 0:
                    encounter_hp = 0
                input(f'{encounter_poke.name} has {encounter_hp} HP left! ')
                if encounter_hp == 0:
                    input(f'{encounter_poke.name} fainted! ')
                    return False
                chosen_action = True
        # Enemy Pokemon Turn
        if chosen_action is True:
            for move_name, move_damage in moves_dict.items():
                if  random_encounter_move == move_name: 
                    input(f'\n{encounter_poke.name} used {move_name}! It does {move_damage} damage! ')
                    user_poke_hp -= move_damage
                    if user_poke_hp <= 0:
                        user_poke_hp = 0
                    input(f'{user_poke.name} has {user_poke_hp} HP left! ')
                    if user_poke_hp == 0: 
                        input(f'{user_poke.name} fainted! You blacked out! ')
                        return False


def pokemon_catch():
    pass


def pokemon_healing_item(user_poke, health_item):
    for item_name, item_health in health_items_dict.items():
        if health_item == item_name:
            user_poke.stats['HP'] += item_health
            input(f'{user_poke.name} restored {item_health} HP! ')
            return

    


def bag_option(user_poke):
    bag_contents()

    while True: 
        user_option = input("Which item would you like to use? ").upper()
        for item_name, item_count in bag.items():
            if user_option == item_name:
                if item_count == 0:
                    input(f'No more {item_name}(s)! ')
                    return True

                if user_option == "POKEBALL":
                    pokemon_catch(user_option)
                elif user_option == "POTION":
                    pokemon_healing_item(user_poke, user_option)
                    
                item_count -= 1
                return True



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
            user_action = bag_option(user_current_pokemon)
            battle_key = fight_option(user_current_pokemon, wild_pokemon, user_action)
        elif user_option == battle_options[2]: # Pokemon
            pokemon_option()
        elif user_option == battle_options[3]:  # Run
            run_option()
            # else:
            #     raise Exception

        # except Exception:
        #     error_statement()



    
