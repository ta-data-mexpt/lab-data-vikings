
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
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        return 'A Saxon has died in combat'

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, oneViking):
        self.vikingArmy.append(oneViking)

    def addSaxon(self, oneSaxon):
        self.saxonArmy.append(oneSaxon)

    def vikingAttack(self):
        from random import randint
        vikingIndex = randint(0, len(self.vikingArmy)-1)
        saxonIndex = randint(0, len(self.saxonArmy)-1)
        viking = self.vikingArmy[vikingIndex]
        saxon = self.saxonArmy[saxonIndex]

        message = saxon.receiveDamage(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.pop(saxonIndex)
        return message

    def saxonAttack(self):
        from random import randint
        vikingIndex = randint(0, len(self.vikingArmy)-1)
        saxonIndex = randint(0, len(self.saxonArmy)-1)
        viking = self.vikingArmy[vikingIndex]
        saxon = self.saxonArmy[saxonIndex]

        message = viking.receiveDamage(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.pop(vikingIndex)
        return message

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."