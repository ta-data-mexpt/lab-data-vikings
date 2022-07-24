
# Soldier

import random


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!" 

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        return f"A Saxon has died in combat"

    pass

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        self.status = True
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):

        attacking_viking = random.choice(self.vikingArmy)
        print(f"{attacking_viking.name} has {attacking_viking.strength} strength")
        attacked_saxon = random.choice(self.saxonArmy)
        print(f"{attacked_saxon} has {attacked_saxon.health} health")
        attacked_saxon.receiveDamage(attacking_viking.attack())
        print(f"{attacked_saxon} has {attacked_saxon.health} health after the attack of {attacking_viking.name}")
        if attacked_saxon.health <= 0:
            self.saxonArmy.remove(attacked_saxon)
    def saxonAttack(self):
        attacking_saxon = random.choice(self.saxonArmy)
        print(f"{attacking_saxon} has {attacking_saxon.strength} strength")
        attacked_viking = random.choice(self.vikingArmy)
        print(f"{attacked_viking.name} has {attacked_viking.health} health")
        attacked_viking.receiveDamage(attacking_saxon.attack())
        print(f"{attacked_viking.name} has {attacked_viking.health} after the attack of {attacking_saxon}")
        if attacked_viking.health <= 0:
            self.vikingArmy.remove(attacked_viking)

    def showStatus(self):
        print(f"The Viking Army has {len(self.vikingArmy)} soldiers")
        print(f"The Saxon Army {len(self.saxonArmy)} soldiers")
        if len(self.saxonArmy) == 0:
            self.status = False
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            self.status = False
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    


my_war = War()

continue_war = True

for i in range(10):
    my_war.addViking(Viking(f"Viking{i}", random.randint(100, 200), random.randint(100,200)))
    my_war.addSaxon(Saxon(random.randint(100, 200), random.randint(100,200)))

def warRound1(my_war):
    print(my_war.status)
    my_war.vikingAttack()
    return my_war.showStatus()

def warRound2(my_war):
    print(my_war.status)
    my_war.saxonAttack()
    return my_war.showStatus()

while continue_war is True:
    my_war.vikingAttack()
    print(my_war.showStatus())
    if my_war.status is False:
        continue_war = False
    else:
        my_war.saxonAttack()
        print(my_war.showStatus())
        if my_war.status is False:
            continue_war = False









