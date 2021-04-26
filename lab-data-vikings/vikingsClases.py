
# Soldier


class Soldier:
    def __init__(self, health, strenght, attack, receiveDamage):
        self.health = health
        self.strength = strength 
        self.attack = attack
        self.receiveDamage = receiveDamage
    
    def attack(self):
        return self.strenght
    
    def receiveDamage(self):
        return self.health - self.receiveDamage
    
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self):
        x = self.health - self.receiveDamage
        if x <= 0:
            return self.name + " has died in act of combat"
        else:
            return self.name + "has received " + self.receiveDamage + " points of damage"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self):
        x = self.health - self.receiveDamage
        if x <= 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxonhas has received " + self.receiveDamage + " points of damage"
        
        
    

# War


class War:
    pass
