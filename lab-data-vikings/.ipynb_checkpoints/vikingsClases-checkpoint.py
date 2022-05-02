# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return f'Odin owns you all!'

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strenght)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        return f'A Saxon has died in combat'

# War
class War:
    pass
