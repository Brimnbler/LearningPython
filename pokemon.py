"""
Off-platform project to create a Pokemon style game using Python.
"""


#   trainer has a pocket of Pokemon up to a max of 6
#   limit items in inventory to 6 (arbitrary decision)
class Trainer:
    def __init__(self, name, pokemon_in_pocket, inventory, active_pokemon):
        self.name = name
        self.pokemon_in_pocket = pokemon_in_pocket
        self.inventory = inventory
        self.active_pokemon = active_pokemon

    def __repr__(self):
        return F"{self.name} is a trainer"

    #   set Pocket Pokemon
    def add_pokemon_to_pocket(self, pokemon):
        self.pokemon_in_pocket.append(pokemon)

    #   set a Pokemon from pokemon_in_pocket to be their active_pokemon
    def call_pokemon(self):
        pass

    #   use item from inventory on active_pokemon (only thinking of healing at this point.)
    def use_item(self):
        pass

    #   make active_pokemon use their attack on opponent's pokemon.
    #   check weaknesses to calculate damage done
    def trigger_attack(self):
        pass


class Pokemon:
    def __init__(self, name, level, element, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.element = element
        self.max_health = level * 100
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out
        self.exp_value = self.level * 50

    #   string representation when calling a pokemon.
    def __repr__(self):
        return "{} is a {} Pokemon at level {} and has {} hp of a maximum {} hp." \
            .format(self.name, self.element, self.level, self.current_health, self.max_health)

    #   exp needed to level = level*100.
    #   Pokemon will have a value of exp gained based on the level of the pokemon defeated.
    def experience(self):
        pass

    def level_up(self):
        self.level += 1
        self.max_health += 10
        print("{} is now a level {} {} element Pokemon!".format(self.name, self.level, self.element))
        print("{} now has {} maximum hit points!".format(self.name, self.current_health))
        return self.level, self.max_health

    def lose_health(self, attack_value):
        self.current_health = self.current_health - attack_value
        if self.current_health <= 0:
            print("{} is knocked out by the attack!".format(self.name))
            self.current_health = 0
        return "{} loses {} hps to the attack. They have {} hp remaining." \
            .format(self.name, attack_value, self.current_health)

    #   Lesser healing pot
    def lesser_heal(self):
        if self.current_health <= self.max_health:
            self.current_health += 20
            print("You used lesser heal on {} for 20 hps!".format(self.name))
            if self.current_health > self.max_health:
                self.current_health = self.max_health
                print("Your heal went over {}'s maximum health!".format(self.name))
        return self.current_health

    # Use Lesser Healing pot on current pokemon

    #   Greater healing pot
    def greater_heal(self):
        if self.current_health <= self.max_health:
            self.current_health += 50
            print("You used greater heal on {} for 50 hps!".format(self.name))
            if self.current_health > self.max_health:
                self.current_health = self.max_health
                print("Your heal went over {}'s maximum health!".format(self.name))
        return self.current_health

    def change_name(self, new_name):
        self.name = new_name
        return self.name


class Experience:
    pass


class Attacks:
    pass


"""
List of items to be created -- Dictionary idea
"""

#   .use_item_in_inventory
inventory1 = {"Lesser Healing Pot": 1, "Greater Healing Pot": 2}


"""
Building different Pokemon.
"""
squirtle1 = Pokemon("Squirtle", 1, "water", 60, 60, False)
print(squirtle1)
charmander1 = Pokemon("Charmander", 1, "fire", 70, 70, False)
print(charmander1)
bulbasaur1 = Pokemon("Bulbasaur", 1, "grass", 60, 60, False)
print(bulbasaur1)
squirtle2 = Pokemon("Squirtle", 2, "water", 60, 60, False)
print(squirtle2)
charmander2 = Pokemon("Charmander", 2, "fire", 70, 70, False)
print(charmander2)
bulbasaur2 = Pokemon("Bulbasaur", 2, "grass", 60, 60, False)
print(bulbasaur2)

bulk_pokemon_list = [squirtle1, squirtle2, charmander1, charmander2, bulbasaur1, bulbasaur2]

trainer1 = Trainer("Michael", (squirtle1, charmander1), inventory1, charmander1)
print(trainer1)