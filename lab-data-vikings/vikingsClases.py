
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, receiveDamage):
        self.health = self.health - receiveDamage
                

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
      
    def receiveDamage(self, receiveDamage):
        self.health = self.health - receiveDamage
        if self.health > 0:
            return(f'{self.name} has received {receiveDamage} points of damage')
        else:
            return(f'{self.name} has died in act of combat')
    
    def battleCry(self):
        return "Odin Owns You All!"
    
    
# Saxon


class Saxon(Soldier):
    
    def receiveDamage(self, receiveDamage):
        self.health = self.health - receiveDamage
        if self.health > 0:
            return(f'A Saxon has received {receiveDamage} points of damage')
        else:
            return(f'A Saxon has died in combat')

        
# War

import random

class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
       
    def addViking(self, addviking):
        self.vikingArmy.append(addviking)
        
    def addSaxon(self, addsaxon):
        self.saxonArmy.append(addsaxon)
    
    def vikingAttack(self):
        viking_attack = random.choice(self.vikingArmy)
        saxon_defense = random.choice(self.saxonArmy)
        attackviking = saxon_defense.receiveDamage(viking_attack.attack())
        if saxon_defense.health <= 0:
            self.saxonArmy.remove(saxon_defense)
        return attackviking
    
    def saxonAttack(self):
        viking_defense = random.choice(self.vikingArmy)
        saxon_attack = random.choice(self.saxonArmy)
        attacksaxon = viking_defense.receiveDamage(saxon_attack.attack())
        if viking_defense.health <= 0:
            self.vikingArmy.remove(viking_defense)
        return attacksaxon
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        