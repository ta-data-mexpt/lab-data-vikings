from random import choice


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
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'

# War


class War:

    def __init__(self):
        self.saxonArmy = []
        self.vikingArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        self.saxon = choice(self.saxonArmy)
        message_return = self.saxon.receiveDamage(choice(self.vikingArmy).attack())
        if self.saxon.health <= 0:
            self.saxonArmy.remove(self.saxon)
        return message_return

    def saxonAttack(self):
        self.viking = choice(self.vikingArmy)
        message_return = self.viking.receiveDamage(choice(self.saxonArmy).attack())
        if self.viking.health <= 0:
            self.vikingArmy.remove(self.viking)
        return message_return

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'

