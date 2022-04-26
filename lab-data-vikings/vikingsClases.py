
# Soldier


from tkinter import S
import random


class Soldier:
    
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        # add code here
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health=self.health-damage
        return 

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health>0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")


    def battleCry(self):
        return ("Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health>0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return ("A Saxon has died in combat")

# War


class War:

    vikingArmy=[]
    saxonArmy=[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        print(f'el numero de vikingos es {len(self.vikingArmy)}')
        return ;

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        print(f'el numero de saxones es {len(self.saxonArmy)}')
        return ;

    def vikingAttack(self):
        v = random.randint(0, len(self.vikingArmy))
        s = random.randint(0, len(self.saxonArmy))
        print(f'El numero v es {v}')
        print(f'El numero s es {s}')
        at=self.vikingArmy[v].strength
        he=self.saxonArmy[s].health
        ms=self.saxonArmy[s].receiveDamage(at)

        if at>=he:
            self.saxonArmy.pop(s)
            return ms
        else:
            return ms    


    def saxonAttack(self):
        v = random.randint(0, len(self.vikingArmy))
        s = random.randint(0, len(self.saxonArmy))

        at=self.saxonArmy[s].strength
        he=self.vikingArmy[v].health
        ms=self.vikingArmy[v].receiveDamage(at)

        if at>=he:
            self.vikingArmy.pop(v)
            return ms
        else:
            return ms   


    def showStatus(self):
        if len(self.vikingArmy)==0 and len(self.saxonArmy)!=0:
            return ("Saxons have fought for their lives and survive another day...")
        elif len(self.vikingArmy)!=0 and len(self.saxonArmy)==0:
            return ("Vikings have won the war of the century!")
        elif len(self.vikingArmy)!=0 and len(self.saxonArmy)!=0:
            return ("Vikings and Saxons are still in the thick of battle.")
        else:
            return ;
