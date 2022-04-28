import random
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # super().__init__(health, strength) No supe si esto funcionaría para heredar 
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        v_attack = chosen_saxon.receiveDamage(chosen_viking.strength)
        if chosen_saxon.health <= 0:
            self.saxonArmy.remove(chosen_saxon)
        return v_attack
              
    def saxonAttack(self):
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        s_attack = chosen_viking.receiveDamage(chosen_saxon.strength)
        if chosen_viking.health <= 0:
            self.vikingArmy.remove(chosen_viking)
        return s_attack
    
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
