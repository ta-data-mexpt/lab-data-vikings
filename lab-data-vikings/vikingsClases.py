
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack():
        return self.strength
    def receiveDamage(damage):
        self.health-damage
        
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        Soldier.__init__(self,health,strength)
    
    def receiveDamage(): 
        self.health-damage
        if self.health-damage>0:
            return f"{name} has received {damage} points of damage"
        elif self.health-damage=0:
            return f"{name} has died in act of combat"    
    def battleCry():
        return "Odin Owns You All!"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage()
        if self.health-damage>0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health-damage=0:
            return "A Saxon has died in combat"    
# War


class War:
    pass
