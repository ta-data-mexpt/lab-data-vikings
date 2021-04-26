
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking

class Viking:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDemage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name,damage)
        else:
            return '{} has died'.format(self.name)
    
    def battleCry(self):
        return 'Odin owns you all'

# Saxon


class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strenght
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return 'A Saxon has received {} ppoints of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'

# War


class War:
    pass
