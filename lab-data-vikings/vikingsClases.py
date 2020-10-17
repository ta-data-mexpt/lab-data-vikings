from random import choice

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, dmg):
        self.health -= dmg

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, dmg):
        if self.health - dmg > 0:
            self.health -= dmg
            return f"{self.name} has received {dmg} points of damage"
        else:
            self.health -= dmg
            return f"{self.name} has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, dmg):
        self.health -= dmg
        if self.health > 0:
            return f"A Saxon has received {dmg} points of damage"
        else:
            return "A Saxon has died in combat"
# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        ss = choice(self.saxonArmy)
        vs = choice(self.vikingArmy).strength
        if ss.health - vs > 0:
            return ss.receiveDamage(vs)
        else:
            self.saxonArmy.remove(ss)
            return ss.receiveDamage(vs)

    def saxonAttack(self):
        ss = choice(self.saxonArmy).strength
        vs = choice(self.vikingArmy)
        if vs.health - ss > 0:
            return vs.receiveDamage(ss)
        else:
            self.vikingArmy.remove(vs)
            return vs.receiveDamage(ss)

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
