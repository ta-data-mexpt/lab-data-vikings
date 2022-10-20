
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, receiveDamage):
        self.health = self.health - receiveDamage 
    pass

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self, receiveDamage):
        self.health = self.health - receiveDamage
        if self.health > 0:
            #print(f'{self.name} has received {receiveDamage} points of damage')
            return f'{self.name} has received {receiveDamage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'
        
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receiveDamage(self, receiveDamage):
        self.health = self.health - receiveDamage
        if self.health > 0:
            #print(f'{self.name} has received {receiveDamage} points of damage')
            return f'A Saxon has received {receiveDamage} points of damage'
        else:
            return f'A Saxon has died in combat'
        
    pass

# War


class War:
    #def __init__(self):
    #    self.vikingArmy = []
    #    self.saxonArmy = []
        
    #def addViking(self, Viking()):
    #    self.vikingArmy.append(Viking())
        
    #def addSaxon(self, Saxon()):
    #    self.saxonArmy.append(Saxon())
    
    #def vikingAttack(self):
    #    for viking in self.vikingArmy:
    #        viking.da
        
        
    pass
