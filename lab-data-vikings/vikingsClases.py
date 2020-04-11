
# Soldier
import random


class Soldier:
# Modify the Soldier constructor function and add 2 methods to its prototype: attack(), and receiveDamage()
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
            
    def attack(self):
        # (This method should be inherited from Soldier, no need to reimplement it.)
        # should return the strength property of the Viking
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage # checar si esto está bien
        # should remove the received damage from the health property
    
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength) # super hace referencia a la clase base o la clase que se está heredando
        print(name, health, strength)


    def attack(self):
        # return super().strength
        # super().attack() # cuaquier opción podría funcionar
        return self.strength
        # should return the strength property of the Viking
        
    def receiveDamage(self, damage):
        # (This method needs to be reimplemented for Viking because the Viking version needs to have different return values.)
        super().receiveDamage(damage)
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
        # should remove the received damage from the health property
        # if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
        # if the Viking dies, it should return "NAME has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"
        
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
        print(health,strength)
        
    def attack(self):
        #(This method should be inherited from Soldier, no need to reimplement it.)
        #should return the strength property of the Saxon
        return self.strength
    
    def receiveDamage(self, damage):
        #(This method needs to be reimplemented for Viking because the Viking version needs to have different return values.)
        super().receiveDamage(damage)
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
        #should remove the received damage from the health property
        #if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)
        result = s.receiveDamage(v.attack())
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return result
    
    def saxonAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)
        result = v.receiveDamage(s.attack())
        if v.health <= 0:
            self.vikingArmy.remove(v)
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."
