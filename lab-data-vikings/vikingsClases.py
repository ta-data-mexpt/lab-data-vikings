#Soldier
class Soldier:
    #add constructor with health and strength parameters
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    #add attack method
    def attack(self):
        return self.strength
    
    #add receiveDamage method
    def receiveDamage(self, damage):
        self.health -= damage
# Viking
class Viking:
    #add constructor with name, health and strength parameters
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name      
    
    #add receiveDamage method
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    #add battleCry method
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"    
# War
class War:
    
    #add constructor with no parameters
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    #add addViking method
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    #add addSaxon method
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    #add vikingAttack method
    def vikingAttack(self):
        from random import choice
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    #add saxonAttack method
    def saxonAttack(self):
        from random import choice
        saxon = choice(self.saxonArmy)
        viking = choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    
    #add showStatus method
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."