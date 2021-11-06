import random

# SOLDIER = superclass 
# 2 powers(functions) 
class Soldier:
    def __init__(self, health, strength):
        self.health == health
        self.strength == strength 
     
    def attack(self):
        return self.strenght 
    
    def receiveDamage(self, damage):
        self.health -= damage   #remove the received damage from the `health` property
        
            
## VIKING = subclass 
# 3 powers(functions) // Attack is inherited from SOLDIER
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name == name
        self.health == health
        self.strength == strength 
     
     def viking(self, damage):
        self.health -= damage   #remove the received damage from the `health` property
        if health >= 1:
            return ({self.name}, "has received", {damage}, "points of damage")
        else:
            return ({self.name}, "has died in act of combat")
   
    def battleCry(self):
        return ("Odin Owns You All!")
    
## SAXON = subclass
# 2 powers(functions) // Attack is inherited from SOLDIER
class Viking(Soldier):
    def __init__(self, health, strength):
        self.health == health
        self.strength == strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if healht >= 1:
            return ("A Saxon has received", {DAMAGE}, "points of damage"}
        else:
            return ("A Saxon has died in combat")
    

#----------------------------------------------------------------------------

## WAR = superclass
class War():
    def __init__ (self, )
    self.vikingArmy = []
    self.saxonArmy = []
    
    def addViking(self, Viking):
    self.vikingArmy.append(Viking)
                    
    def addSaxon(self, Saxon):
    self.saxonArmy.append(Saxon)
                    
    def vikingAttack(self):
    saxonRandom = random.choice(self.saxonArmy) #Select a random 'saxonArmy'
    vikingStrenght = random.choice(self.vikingArmy).strength #Select a random 'vikingArmy', select `strength` of a `Viking
    damageViking = saxon.receiveDamage(vikingStrenght) #Select damage equal to the the `strength` of a `Viking`
    if saxonHealth <= 0: 
       self.saxonArmy.remove(saxonRandom) #remove dead saxons from the army
    return damageViking
                    
    def saxonAttack(self):
    vikingRandom = random.choice(self.vikingArmy) #Select a random 'vikingArmy'
    saxonStrenght = random.choice(self.saxonArmy).strength #Select a random 'saxonArmy', select `strength` of a 'saxon'
    damageSaxon = viking.receiveDamage(saxonStrenght)
    if vikingHealth = 0:
       self.vikingArmy.remove(vikingRandom)
    return damageSaxon

    def showStatus():
    if self.saxonArmy == []:
        return ("Vikings have won the war of the century!")
    elif:
        return ("Saxons have fought for their lives and survive another day...")
                    
    else:
        return("Saxons have fought for their lives and survive another day...")
                    
                  