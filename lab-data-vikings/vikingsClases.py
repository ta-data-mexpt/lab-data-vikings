
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self,damage):
        self.health = self.health-damage

# Viking


class Viking:
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self,damage):
        self.health = self.health-damage
        return print(name+ " has received " + damage+" points of damage") if self.healt>0 else print(name + " has died in act of combat") 
    
    def battleCry()
        return print("Odin Owns You All!")
# Saxon


class Saxon:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self,damage):
        self.health = self.health-damage
        return print("A Saxon has received" + damage+" points of damage") if self.healt>0 else print("A Saxon has died in combat") 

# War


class War:
    pass
