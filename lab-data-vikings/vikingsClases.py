
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > self.damage:
            return (self.name + " " + 'has received'+ " " + str(self.damage) + " " + 'points of damage')
        else:
            return (self.name + " " + 'has died in act of combat')
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > self.damage:
            return (f'A Saxon has received {str(self.damage)} points of damage')
        else:
            return 'A Saxon has died in combat'
    pass

# War


class War:
    pass
