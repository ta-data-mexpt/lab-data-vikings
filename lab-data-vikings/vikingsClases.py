   
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
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        
        # still alive?
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'

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
        # viking & saxon indeces
        idx_viking = random.choice(range(len(self.vikingArmy)))
        idx_saxon = random.choice(range(len(self.saxonArmy)))
       
        # inflict damage
        damage = self.vikingArmy[idx_viking].attack()
        attack_result = self.saxonArmy[idx_saxon].receiveDamage(damage)

        # remove dead saxon
        if self.saxonArmy[idx_saxon].health <= 0:
            self.saxonArmy.pop(idx_saxon)

        return attack_result

    def saxonAttack(self):
        # viking & saxon indeces
        idx_viking = random.choice(range(len(self.vikingArmy)))
        idx_saxon = random.choice(range(len(self.saxonArmy)))
       
        # inflict damage
        damage = self.saxonArmy[idx_saxon].attack()
        attack_result = self.vikingArmy[idx_viking].receiveDamage(damage)

        # remove dead saxon
        if self.vikingArmy[idx_viking].health <= 0:
            self.vikingArmy.pop(idx_viking)

        return attack_result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
