
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    

    def attack(self):
        return self.strength
    

    def receiveDamage(self,damage):
         self.health -= damage
      

# Viking


class Viking(Soldier):

    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength

    #def attack(self): 
    #    return self.strength
        #al haber heredado, me regresará la fuerza de la clase actual osea vikingo
        

    def receiveDamage(self,damage):
        self.health -= damage
        #no se crean variables por que si no la vida nunca se actualizaría
        if self.health > 0:
           return (f"{self.name} has received {damage} points of damage")
        else: 
           return (f"{self.name} has died in act of combat")

    def battleCry(self):
        return ('Odin Owns You All!')



# Saxon


class Saxon(Soldier):
    
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    #def attack(self): 
    #    return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
           return (f"A Saxon has received {damage} points of damage")
        else: 
           return ("A Saxon has died in combat")
        

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []#lista o arreglo

    def addViking(self,viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)       

    def vikingAttack(self):
        mensaje_saxones = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).attack())
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon) 
        return mensaje_saxones


    pass
