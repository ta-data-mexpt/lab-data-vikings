import random as rand


# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.strength = strength
        self.health = health
        Soldier.attack(self)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {str(damage)} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health
        Soldier.attack(self)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {str(damage)} points of damage"
        else:
            return "A Saxon has died in combat"


# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        saxon = rand.choice(self.saxonArmy)
        viking = rand.choice(self.vikingArmy)
        viking_attack = saxon.receiveDamage(viking.strength)
        [self.saxonArmy.remove(saxon) for saxon in self.saxonArmy if saxon.health <= 0]
        return viking_attack

    def saxonAttack(self):
        saxon = rand.choice(self.saxonArmy)
        viking = rand.choice(self.vikingArmy)
        saxon_attack = viking.receiveDamage(saxon.strength)
        [self.vikingArmy.remove(viking) for viking in self.vikingArmy if viking.health <= 0]
        return saxon_attack

    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
