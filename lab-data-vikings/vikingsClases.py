
# Soldier


class Soldier:
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
        def attack(self):
            return strength
        
        def receiveDamage(self,damage):
            self.health = self.health - damage
    pass

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        super().__inti__(self, health, strength)
        self.name = name
        
        def receiveDamage(damage):
            self.health = self.health - damage
            if self.health <= 0:
                message = name + " has died in act of combat"
                return message
            else:
                message = name + " has received "+ damage + "points of damage"
                return message
            
        def battleCry():
            message = "Odin Owns You All!"
            return message
            
    pass

# Saxon


class Saxon:
    
    def __init__(self, health, strength):
        
        super().__inti__(self, health, strength)
        
        def receiveDamage(damage):
            self.health = self.health - damage
            if self.health <= 0:
                message = "A Saxon has died in combat"
                return message
            else:
                message = "A Saxon has received "+ damage + "points of damage"
                return message
    
    pass

# War


class War:
    pass
