
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        Soldier.__init__(self, health, strength)
    
    def attack(self):
        return super().attack()
        
    def receivdeDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has {damage} points"
        else:
            return f"{self.name} has died in act combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def saxonStrength(self):
        return self.strength
    
    def attack(self):
        return super().attack()
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"Saxon has {damage} points of damage"
        else:
            return f"Saxon died in combat"

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
        saxonDamage = Saxon.receiveDamage(Viking.attack)
        self.saxonArmy = filter(lambda x: x>0, [Saxon.health for Saxon.health in self.saxonArmy])
        return saxonDamage
    
    def saxonAttack(self):
        vikingDamage = Viking.receiveDamage(Saxon.attack)
        self.vikingArmy = filter(lambda x: x>0, [Viking.health for Viking.health in self.vikingArmy])
        return vikingDamage
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."