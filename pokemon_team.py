# Pokemon Team Module 

# Pokemon 
class Pokemon():

    def __init__ (self, id, name, type, description, moves, stats):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.moves = moves
        self.stats = stats


# Bag 
bag = {"POKEBALL": 0, "POTION": 0}

def bag_contents():
    for item_name, item_count in bag.items():
        print(f'{item_count} {item_name}(s)')

# User Pokemon Team
user_team = []
