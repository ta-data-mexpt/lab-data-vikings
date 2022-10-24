
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def attack(self)
        return self.strength
    
    
    def receiveDamage(self, damage):
        self.health=self.health - damage
        
    pass

# Viking

#The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class.

class Viking(Soldier):
    
    def __init__(self, name, health, strenght):
        self.name=name
        super().__init__(health,strength):
    
    def receiveDamage(self,damage):
        super().receivesDamage(damage)
        if self.health>0:
            return print(f"{self.name} has received {damage} points of damage")
        else
            return print(f"{self.name} has died in act of combat")
            
    def battlecry(self):
        return print("Odin Owns You All!")
    
                
        
    pass

# Saxon

##se usa la libreria random??
##import random


class Saxon(Soldier):
    
       def __init__(self, health, strenght):
            super().__init__(health,strength):
                
        def receiveDamage(self, damage):
            super().receiveDamage(damage)
            if self.health>0:
                return print(f"A Saxon has received {damage} points of damage")
            else:
                return print("A Saxon has died in combat")
            
    pass

# War


class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        
    def addViking(self, Viking)
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon)
        self.saxonArmy.append(Saxon)      
        
    
    pass
