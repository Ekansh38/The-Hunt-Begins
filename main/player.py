class Player:
    def __init__(self, name, strength, agility, intelligence, stealth):
        self.name = name

        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stealth = stealth

    def __str__(self):
        return f"{self.name}"
