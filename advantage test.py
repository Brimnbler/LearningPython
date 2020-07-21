# X:[Y,Z]
# X --> attacking pokemon
# Y --> attack * 2
# Z --> attack * .5

class Pokemon:

    def __init__(self, name, level, element):
        self.name = name
        self.level = level
        self.element = element

    def advantage(self, attacker, defender):
        advantage_table = {
            "Fire": ("Grass", "Water"),
            "Grass": ("Water", "Fire"),
            "Water": ("Fire", "Grass")
        }
        for key in advantage_table:
            print(advantage_table["attacker.element"])


attacker_test = Pokemon("Attacker", 1, "Fire")
defender_test = Pokemon("Defender", 1, "Water")

print(advantage(attacker_test, defender_test))
