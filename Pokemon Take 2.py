"""
Pokemon emulator take 2
"""


class Trainer:

    def __init__(self, name, pokemon_in_pocket, called_pokemon):
        self.name = name
        self.pokemon_in_pocket = pokemon_in_pocket
        self.called_pokemon = called_pokemon

    def __repr__(self):
        return F"{self.name} is a trainer with {self.pokemon_in_pocket} in their pocket"


class Pokemon:

    def __init__(self, name, level, element):
        self.name = name
        self.level = level
        self.element = element
        self.exp = 0
        self.knocked_down = False
        self.current_health = self.max_health()

    def __repr__(self):
        return F"Name: {self.name} \n" \
               F"Level: {self.level} \n" \
               F"Element: {self.element} \n" \
               F"Hit Points: {self.current_health}/{self.max_health()} \n" \
               F"Experience: {self.exp}"

    def attack(self, other_pokemon):
        # check K.O. status
        other_pokemon.current_health -= self.attack_damage
        return other_pokemon.current_health

    def level_up(self):
        self.level += 1
        self.current_health += 100  # initial heal to offset max_health gain
        print(F"{self.name} is now a level {self.level} Pokemon!")
        print(F"{self.name} now has {self.current_health} maximum hit points!")
        return self.level

    def max_health(self):
        return self.level * 100

    def attack_damage(self):
        return self.level * 50  # used 50 because .5*50 = 25 and 2*25 = 50 for ease of use not balance


"""
Pokemon Builder
"""
bulbasaur = Pokemon("Squirtle ", 1, "Grass")
squirtle = Pokemon("Squirtle", 1, "Water")
charmander = Pokemon("Charmander", 1, "Fire")

"""
Trainer Builder
"""
trainer1 = Trainer("Michael", [squirtle, charmander], squirtle)
# print(trainer1)


"""
Testing!
"""
# print(bulbasaur.attack(squirtle))
