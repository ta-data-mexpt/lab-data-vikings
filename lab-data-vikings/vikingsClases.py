
# Soldier


class Soldier():
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage (self,damage):
        self.health=self.health-damage
    

# Viking


class Viking(Soldier):
    def _init_(self,name,health,strength):
        self.name=name
        self.health=health
        self.stength=strength
    
    def receiveDamage(self,damage):
        self.health=damage
        if self.health>0:
            return name, 'has received', damage, 'points of damage'
        else:
            return name, 'has died in act of combat'
        
        def battleCry(self):
            return 'Odin Owns You All!'
        
    


# Saxon


class Saxon(Soldier):
    def _init_(self,health,strength):
        self.health=health
        self.strength=strength
        
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return 'A Saxon has received',damage,'points of damage'
        else:
            return 'A Saxon has died in combat'
    

# War


class War():
    def _init_(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        if Saxon.health<=0:
            self.saxonArmy.remove(Saxon)
        return Saxon.receiveDamage==Viking.strength
    
    def saxonAttack(self):
        if Viking.health<=0:
            self.vikingArmy.remove(Viking)
        return Viking.receiveDamage==Saxon.strength
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy)==0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
        
