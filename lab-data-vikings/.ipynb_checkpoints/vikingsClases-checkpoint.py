
# Soldier


class Soldier:
    
    def __init__(self,health,strength):
        self.health = health
        self.strenght = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        

# Viking


class Viking(Soldier):
    
    def __init__(self,name,health,strength):
        self.name=name
        self.health = health
        self.strenght = strength
        
    #Attack heredado de la clase de Soldier
    
    def receiveDamaged(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name+"has received"+str(damage)+"points of damage"
        else:
            return self.name+"has died in act of combat"
    
    def battleCry(self):
        return print("Odin owns you all!")
        
    
    

# Saxon


class Saxon(Soldier):
    
    def __init__(self,health,strength):
        self.health = health
        self.strenght = strength
        
    #Attack() es heredado de Soldier class
        
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A saxon has received"+str(damage)+"points of damage"
        else:
            return "A saxon has died in act of combat"
        
    
#Bonus pending to do

# War


class War:
    pass
