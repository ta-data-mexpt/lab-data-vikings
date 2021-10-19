import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health += -damage
        

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health += -damage
        if self.health > 0: return f'{self.name} has received {damage} points of damage'
        else: return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'
        
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health += -damage
        if self.health > 0: return f'A Saxon has received {damage} points of damage'
        else: return f'A Saxon has died in combat'
        
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
        rndmSax = random.choice(self.saxonArmy)
        attackingViking = random.choice(self.vikingArmy)
        message = rndmSax.receiveDamage(attackingViking.strength)
        if rndmSax.health <= 0: self.saxonArmy.remove(rndmSax)
        return message
    
    def saxonAttack(self):
        rndmVik = random.choice(self.vikingArmy)
        attackingSaxon = random.choice(self.saxonArmy)
        message = rndmVik.receiveDamage(attackingSaxon.strength)
        if rndmVik.health <= 0: self.vikingArmy.remove(rndmVik)
        return message
            

    def showStatus(self):
        if self.saxonArmy == []: return 'Vikings have won the war of the century!'
        elif self.vikingArmy == []: return 'Saxons have fought for their lives and survive another day...'
        else: return 'Vikings and Saxons are still in the thick of battle.'
        
        
        