
import random

# Soldier


class Soldier:
    def __init__(self,health, strength):
        self.health = health
        self.strength = strength  
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        
    

# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
             return f'{self.name} has died in act of combat'

    def battleCry(self):
        return "Odin Owns You All!"
    
        
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self,damage):
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
    
    def addViking(self, vik):
        self.vikingArmy.append(vik)
    
    def addSaxon(self, sak):
        self.saxonArmy.append(sak)
        
    def vikingAttack(self):
        saxon_ind = random.choice(range(len(self.saxonArmy)))
        viking_ind = random.choice(range(len(self.vikingArmy)))
    
        result = self.saxonArmy[saxon_ind].receiveDamage(self.vikingArmy[viking_ind].strength)
        
        #self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health > 0]
        self.saxonArmy = list(filter(lambda x: x.health > 0,self.saxonArmy ))
        #print(self.saxonArmy)
        return result
    
    def saxonAttack(self):
        saxon_ind = random.choice(range(len(self.saxonArmy)))
        viking_ind = random.choice(range(len(self.vikingArmy)))
    
        result = self.vikingArmy[viking_ind].receiveDamage(self.saxonArmy[saxon_ind].strength)
        
        #self.vikingArmy = [viking for viking in self.vikingArmy if viking.health > 0]
        self.vikingArmy = list(filter(lambda x: x.health > 0,self.vikingArmy ))
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
            
        
        
    
        
