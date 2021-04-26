
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
        super().__init__(health, strength)
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return f'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
    

# War
import random

class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy  = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxonWarrior = random.randrange(len(self.saxonArmy))
        vikingWarrior = random.randrange(len(self.vikingArmy))
        result = self.saxonArmy[saxonWarrior].receiveDamage(self.vikingArmy[vikingWarrior].strength)
        if self.saxonArmy[saxonWarrior].health <= 0:
            self.saxonArmy.pop(saxonWarrior)
            
        return result
    
    def saxonAttack(self):
        vikingWarrior = random.randrange(len(self.vikingArmy))
        saxonWarrior = random.randrange(len(self.saxonArmy))
        result = self.vikingArmy[vikingWarrior].receiveDamage(self.saxonArmy[saxonWarrior].strength)
        if self.vikingArmy[vikingWarrior].health <= 0:
            self.vikingArmy.pop(vikingWarrior)
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return f'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return f'Vikings and Saxons are still in the thick of battle.'
        else: 
            return f'Battle continue!!!'
    
    
