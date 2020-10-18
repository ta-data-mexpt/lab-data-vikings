
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
        return self.name+" has received "+str(damage)+" points of damage" if self.health>0 else self.name+" has died in act of combat"
    
    def battleCry(self):
        return 'Odin Owns You All!'
# Saxon


class Saxon:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self,damage):
        self.health = self.health-damage
        return "A Saxon has received "+str(damage)+" points of damage" if self.health>0 else "A Saxon has died in combat" 

# War

class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
#         Vname=Viking(name,health,strength)
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
#         Sname=Saxon(health,strength)
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        Saxon.receiveDamage(Viking.attack(Viking))
        
    def saxonAttack(self):
        Viking.receiveDamage(Saxon.attack(Saxon))
        
    def showStatus(self):
        if self.saxonArmy==[]:
            message="Vikings have won the war of the century!"
        elif self.vikingArmy==[]:
            message="Saxons have fought for their lives and survive another day..."
        else:
            message="Vikings and Saxons are still in the thick of battle."
        return message   
    
