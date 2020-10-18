
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        #should remove the received damage from the `health` property
        self.health = self.health - damage
        return

# Viking

#Viking should inherit from `Soldier`
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

#attack method should be **inherited** from `Soldier`, no need to reimplement it
    def receiveDamage(self,damage):
        #should remove the received damage from the `health` property
        self.health = self.health - damage
        if self.health > 0:
            return self.name + "has received " + str(damage) + "points of damage"
        else:
            return self.name + "has died in act of combat"
            
    def battleCry(self):
         return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def receiveDamage(self,damage):
        #should remove the received damage from the `health` property
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + "points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    #def vikingAttack():
       
    
    #def saxonAttack()

    #def showStatus()
    pass
