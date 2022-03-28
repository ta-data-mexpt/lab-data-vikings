
# Soldier


import random

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
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        rand_viking = random.randint(0, len(self.vikingArmy) - 1)
        rand_saxon = random.randint(0, len(self.saxonArmy) - 1)
        selected_viking = self.vikingArmy[rand_viking]
        selected_saxon = self.saxonArmy[rand_saxon]
        result = selected_saxon.receiveDamage(selected_viking.strength)
        if selected_saxon.health <= 0:
            self.saxonArmy.pop(rand_saxon)
        return result

    def saxonAttack(self):
        rand_viking = random.randint(0, len(self.vikingArmy) - 1)
        rand_saxon = random.randint(0, len(self.saxonArmy) - 1)
        selected_viking = self.vikingArmy[rand_viking]
        selected_saxon = self.saxonArmy[rand_saxon]
        result = selected_viking.receiveDamage(selected_saxon.strength)
        if selected_viking.health <= 0:
            self.vikingArmy.pop(rand_viking)
        return result

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."