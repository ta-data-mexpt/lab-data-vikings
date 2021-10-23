
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
        elif self.health-damage==0:
            return f"{name} has died in act of combat"    
    def battleCry():
        return "Odin Owns You All!"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(damage):
        if self.health-damage>0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health-damage==0:
            return "A Saxon has died in combat"    
# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
 
    def addViking(viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack():
        x=random.choice(self.saxonArmy)
        y=random.choice(self.vikingArmy)
        z=x.reciveDamage(y.strength)
        if z=="A Saxon has died in combat":
            self.saxonArmy.remove(x)
        return x.reciveDamage(y.strength)
    
    def saxonAttack():
        r=random.choice(self.saxonArmy)
        w=random.choice(self.vikingArmy)
        p=w.reciveDamage(r.strength)
        if p==f"{name} has died in act of combat":
            self.vikingArmy.remove(w)
        return p
    
    def showStatus():
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)!=0 and len(self.vikingArmy)!=0:
            return "Vikings and Saxons are still in the thick of battle."