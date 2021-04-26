
# Soldier


class Soldier:
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            message = self.name + " has died in act of combat"
            return message
        else:
            message = self.name + " has received "+ str(damage) + " points of damage"
            return message
            
    def battleCry(self):
        message = "Odin Owns You All!"
        return message
            

# Saxon


class Saxon(Soldier):
    
#    def __init__(self, health, strength):
#        super().__init__(self, health, strength)
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            message = "A Saxon has died in combat"
            return message
        else:
            message = "A Saxon has received "+ str(damage) + " points of damage"
            return message
    

# War


class War:
    pass
