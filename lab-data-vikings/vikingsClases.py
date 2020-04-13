
# Soldier


class Soldier:
    # add code here
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,Damage):
        self.health=self.health-Damage
    pass

# Viking


class Viking(Soldier):
    pass
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,Damage):
        self.health=self.health-Damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name,Damage)
        else:
            return '{} no has died in act of combat'.format(self.name)
            
    def battleCry(self):
        return "Odin Owns You All!"
 

# Saxon


class Saxon(Soldier):
    pass
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,Damage):
        self.health=self.health-Damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(Damage)
        else:
            return "A Saxon has died in combat"
 
    pass

# War


class War:
    pass
