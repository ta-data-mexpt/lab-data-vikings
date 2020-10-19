import random

# Soldier

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage 
    pass

# Viking

class Viking(Soldier) :
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon

class Saxon(Soldier):
    def __init__(self,health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"
    pass

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
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        damagedSaxon = saxon.receiveDamage(viking.attack())
        
        for soldier in self.saxonArmy:
            if soldier.health <=0:
                self.saxonArmy.remove(soldier)
        
        return damagedSaxon
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        damagedVikings = viking.receiveDamage(saxon.attack()) 
        
        for soldier in self.vikingArmy:
            if soldier.health <=0:
                self.vikingArmy.remove(soldier)
        
        return damagedVikings
    
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
                   
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        elif len(self.vikingArmy) == 1 and len(self.saxonArmy) == 1:
            
            return "Vikings and Saxons are still in the thick of battle."

        
