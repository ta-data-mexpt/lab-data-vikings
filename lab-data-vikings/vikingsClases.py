
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        # add code here
        self.health=health
        self.strength=strength
        
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage
        
    pass

# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return (self.name+" has received "+str(damage)+" points of damage")
        else:
            return (self.name+" has died in act of combat")

    def battleCry(self):
        return ("Odin Owns You All!")
    
    pass

# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return ("A Saxon has received "+str(damage)+" points of damage")
        else:
            return ("A Saxon has died in combat")
    pass

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        import random
        randSax=random.choice(self.saxonArmy)
        randViking=random.choice(self.vikingArmy)
        message=randSax.receiveDamage(randViking.strength)
        if randSax.health<=0:
            self.saxonArmy.remove(randSax)
        return message
    
    def saxonAttack(self):
        import random
        randSax=random.choice(self.saxonArmy)
        randViking=random.choice(self.vikingArmy)
        message=randViking.receiveDamage(randSax.strength)
        if randViking.health<=0:
            self.vikingArmy.remove(randViking)
        return message
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return("Vikings have won the war of the century!")
        elif len(self.vikingArmy)==0:
            return("Saxons have fought for their lives and survive another day...")
        else: 
            return("Vikings and Saxons are still in the thick of battle.")

        
    pass