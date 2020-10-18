import random

# Soldier
class Soldier():
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
        Soldier.__init__(self,health,strength)
        self.name = name

    def attack(Soldier):
        return Soldier.strength(self)

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0 :
            return ('{name} has received {damage} points of damage')
        else:
            return ('{name} has died in act of combat')
    
    def battleCry(self):
        return ('Odin Owns you All!')

# Saxon
class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack(Soldier):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return ('A Saxon has received {damage} points of damage')
        else:
            return ('A Saxon has died in combat')

# War
class War(): 
    def __init__ (self):
        self.vikingArmy = [] 
        self.saxonArmy= []   
    
    def addViking(self):
        self.vikingArmy.append(Viking)

    def addSaxon(self):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon= random.choice(self.saxonArmy)
        viking= random.choice(self.vikingArmy)
        battle1 = saxon.receiveDamage(viking.strength)
        if saxon.health == 0:
            self.saxonArmy.remove(saxon)
            return saxon.receiveDamage(viking.strength)
    
    def saxonAttack(self):
        saxon= random.choice(self.saxonArmy)
        viking= random.choice(self.vikingArmy)
        battle2 = viking.receiveDamage(saxon.strength)
        if viking.health == 0:
            self.vikingArmy.remove(viking)
            return viking.receiveDamage(saxon.strength)

    def showStatus(self):
        if saxonArmy == []:
            return ('Vikings have won the war of the century!')
        if vikingArmy == []:
            return ('Saxons have won the war of the century!')
        else:
            return ('Vikings and Saxons are still in the thick battle')