def advantage_attack(self, defender):
    # X:[Y,Z]
    # X --> attacking pokemon
    # Y --> attack * 2
    # Z --> attack * .5
    advantage_table = {
        "Fire": ("Grass", "Water"),
        "Grass": ("Water", "Fire"),
        "Water": ("Fire", "Grass")
    }
    attacker = advantage_table.keys
    defender = advantage_table.values
    if defender.element in advantage_table.values():
        print(values)