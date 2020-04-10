import random
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health-=damage

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength
        
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
        
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        saxon=random.choice(self.saxonArmy)
        viking=random.choice(self.vikingArmy)
        if saxon.health <= viking.strength:
            return [saxon.receiveDamage(viking.strength),self.saxonArmy.remove(saxon)][0]
        else:
            return saxon.receiveDamage(viking.strength)

            
    def saxonAttack(self):
        saxon=random.choice(self.saxonArmy)
        viking=random.choice(self.vikingArmy)
        if viking.health <= saxon.strength:
            return [viking.receiveDamage(saxon.strength),self.vikingArmy.remove(viking)][0]
        else:
            return viking.receiveDamage(saxon.strength)
        
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."