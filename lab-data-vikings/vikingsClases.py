
# Soldier

import random as rd

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength= strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health= self.health - damage
    pass
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name= name
    def receiveDamage(self, damage):
        self.health= self.health - damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health= self.health - damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return (f"A Saxon has died in combat")    
    pass

# War

class War:
    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy= []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        Viking= rd.choice(self.vikingArmy)
        Saxon= rd.choice(self.saxonArmy)
        
        saxon_damage= Saxon.receiveDamage(Viking.attack())
        
        if Saxon.health<=0:
            self.saxonArmy.remove(Saxon)
        return saxon_damage
        
    def saxonAttack(self):
        Viking= rd.choice(self.vikingArmy)
        Saxon= rd.choice(self.saxonArmy)
        
        viking_damage= Viking.receiveDamage(Saxon.attack())
        
        if Viking.health<=0:
            self.vikingArmy.remove(Viking)
        return viking_damage
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:    
            return "Vikings and Saxons are still in the thick of battle."
    pass

