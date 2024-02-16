# Pokemon Battles (Keeps code less cluttered)

battle_options = ["Fight", "Bag", "Pokemon", "Run"]

def battle(wild_pokemon):
    battle_key = True
    input(f'You encountered a {wild_pokemon}! ')

    while battle_key:
        user_option = input("What would you like to do? [FIGHT] [BAG] [POKEMON] [RUN] ").capitalize()
        
        if user_option not in battle_options:
            print("Error")
        


    
