
# Soldier


class Soldier:
    def __init__(self, health, strength):
        
        self.health= health
        self.strength = strength
        
    def attack ():
    
        return self.strength
    
    def receiveDamage(damage):
    
        self.health = self.health - damage
    pass

# Viking


class Viking (Soldier):
    
    def __init__(self,name,health,strength):
    
        self.name=name
        
    def receiveDamage(damage):
        
        self.health = self.health - damage
        
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name) 
    
    def battleCry():
        
        return "Odin Owns You All!"
        
    
    pass

# Saxon


class Saxon (Soldier):
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def receiveDamage(damage):
        
        self.health = self.health - damage
        
        if self.health > 0:
            
            return "A Saxon has received DAMAGE points of damage"
        
        else:
            return "A Saxon has died in combat" 
        
    pass

# War


class War:
    pass
