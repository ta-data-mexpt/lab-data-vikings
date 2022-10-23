
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
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    
    def vikingAttack(self):
        
        if Saxon.receiveDamage(Viking.strength) < 0:
            War.saxonArmy.remove(Saxon)
        return War.saxonArmy.remove(Saxon)
    
    def SaxonAttack(self):
        
        if Viking.receiveDamage(Saxon.strength) < 0:
            War.VikingArmy.remove(Viking.name)
        return War.VikingArmy.remove(Viking.name)
    
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
    pass
