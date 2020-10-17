from random import choice

# Soldier

class Soldier:
    def __init__(self, hp, str):
        self.hp = hp
        self.str = str

    def atack(self):
        return self.str

    def receiveDamage(self, dmg):
        self.hp -= dmg

# Viking


class Viking(Soldier):
    def __init__(self, name, hp, str):
        Soldier.__init__(self, hp, str)
        self.name = name

    def receiveDamage(self, dmg):
        self.hp -= dmg
        if self.hp > 0:
            print(f"{self.name} has recived {dmg} points of damage.")
        else:
            print(f"{self.name} has died in combat.")

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, hp, str):
        Soldier.__init__(self, hp, str)

    def receiveDamage(self, dmg):
        self.hp -= dmg
        if self.hp > 0:
            print(f"A Saxon has received {dmg} points of damage.")
        else:
            print("A Saxon has died in combat")
# War


class War(self):
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        ss = choice(self.saxonArmy)
        vs = choice(self.vikingArmy).str
        if ss.hp - vs > 0:
            return ss.receiveDamage(vs)
        else:
            ss.receiveDamage(vs)
            self.saxonArmy.remove(ss)

    def saxonAttack(self):
        ss = choice(self.saxonArmy).str
        vs = choice(self.vikingArmy)
        if vs.hp - ss > 0:
            return vs.receiveDamage(ss)
        else:
            vs.receiveDamage(ss)
            self.vikingArmy.remove(vs)

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!":
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
