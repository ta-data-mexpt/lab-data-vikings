
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    #pass
    
    def attack(self):
        return self.strength 
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier): 
    def __init__(self, name, health, strength): 
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > damage:
            print(str(self.name) + " has received " + str(damage) + " points of damage")
        elif self.health <= damage:
            print(str(self.name) + " has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage 
        if self.health > damage:
            print("A Saxon has received " + str(damage) + " points of damage")
        elif self.health <= damage:
            print("A Saxon has died in combat")


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append("Viking")

    def addSaxon(self, Saxon):
        self.saxonArmy.append("Saxon")

    def vikingAttack(self):
#Anna: algo esta mal aqui, no lo se
        self.vikingAttack = Saxon.receiveDamage(self, damage=Viking.attack)
        return Saxon.receiveDamage(self, damage=Viking.attack)
        
    def saxonAttack(self):
#Anna: algo esta mal aqui, no lo se
        self.saxonAttack = Viking.receiveDamage(self, damage=Saxon.attack)
        return Viking.receiveDamage(self, damage=Saxon.attack)
        
    def showStatus(self):
        if (len(self.saxonArmy)==0):
            print("Vikings have won the war of the century!")
        elif (len(self.vikingArmy)==0):
            print("Saxons have fought for their lives and survive another day...")
        elif (len(self.vikingArmy) >=1) and (len(self.saxonArmy) >=1):
            print("Vikings and Saxons are still in the thick of battle.")

    
        
        
        
        
        
        