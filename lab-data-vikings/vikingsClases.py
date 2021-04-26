
# Soldier


import random


class Soldier:
    def __init__(self,health,strengh):
        self.health = health
        self.strengh = strengh
    def attack(self):
        return self.strengh
    def receiveDamage(self,damage):
        self.health = self.health - (damage)

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strengh):
        Soldier.__init__(self,health,strengh)
        self.name = name
    def receiveDamage(self,damage):
        self.health = self.health - (damage)
        if self.health <= 0:
            return("{} has died in act of combat" .format(self.name))
        else:
            return("{} has received {} points of damage" .format(self.name,damage))
    def battleCry(self):
        return "Odin Owns You All"

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strengh):
        Soldier.__init__(self,health,strengh)
    def receiveDamage(self,damage):
        self.health = self.health - (damage)
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return("A Saxon has received {} points of damage".format(damage))


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self:saxonArmy = []

