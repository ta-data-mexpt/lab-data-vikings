
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    

    def attack(self):
        return self.strength
    

    def receiveDamage(self,damage):
        self.health = self.health - damage
      

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
        self.health = self.health - damage
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
        self.health = self.health - damage
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
        viking_aleatorio = random.choice(self.vikingArmy)
        saxon_aleatorio = random.choice(self.saxonArmy)
        saxon_dañado = saxon_aleatorio.receiveDamage(viking_aleatorio.attack)
        #mensaje_saxones = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).attack())
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon) 
        return saxon_dañado
 
    def saxonAttack(self):
        viking_aleatorio = random.choice(self.vikingArmy)#elige a un vikingo de forma aleatoria
        saxon_aleatorio = random.choice(self.saxonArmy)#elige a un saxon de forma aleatoria
        vikingo_dañado = viking_aleatorio.receiveDamage(saxon_aleatorio.attack)#el vikingo recibe el daño equivalente al ataque del saxon
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking) 
        return vikingo_dañado #El for lo que hace es cada vikingo que este dentro de la lista vikingarmy será eliminado si su health es menor o igual a cero
    
    def showStatus(self):  
        if not self.saxonArmy:#ejmplo de qe no hay nada en la lista 
            return ("Vikings have won the war of the century!")

        elif self.vikingArmy == []:#ejmplo de qe no hay nada en la lista, falta revisar que funcione
                return ("Saxons have fought for their lives and survive another day...")

        elif len(self.vikingArmy) == 1 and len(self.saxonArmy) == 1:
            return ("Vikings and Saxons are still in the thick of battle.")
