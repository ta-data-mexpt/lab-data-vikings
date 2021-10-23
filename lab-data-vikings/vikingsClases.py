
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health=self.health-damage
        
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        Soldier.__init__(self,health,strength)
    
    def receiveDamage(self, damage): 
        self.health=self.health-damage
        if self.health>0:
            return self.name + " has received "+ str(damage) +" points of damage"
        elif self.health==0:
            return self.name + " has died in act of combat"    
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return "A Saxon has received "+ str(damage) +" points of damage"
        elif self.health==0:
            return "A Saxon has died in combat"    
# War 
#No se porque no pasa este test u.u ya lo intente varias veces, los demas si pasan  
import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
 
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        x=random.choice(self.saxonArmy)
        y=random.choice(self.vikingArmy)
        z=x.receiveDamage(y.strength)
        if z=="A Saxon has died in combat":
            self.saxonArmy.remove(x)
       
        return z
    
    def saxonAttack(self):
        r=random.choice(self.saxonArmy)
        w=random.choice(self.vikingArmy)
        p=w.receiveDamage(r.strength)
        if p== w.name +" has died in act of combat":
            self.vikingArmy.remove(w)
        return p
    
    def showStatus(self):
        if len(self.saxonArmy)==0 and len(self.vikingArmy)>0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0 and len(self.saxonArmy)>0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)>0 and len(self.vikingArmy)>0:
            return "Vikings and Saxons are still in the thick of battle."