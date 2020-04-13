
# Soldier


class Soldier():
    health = 300
    strength = 150
    
    def attack(self):
        return strength
    def receiveDamage(self, damage):
        newhealth=health-damage
        #return newhealth
       

# Viking


class Viking(Soldier):
    name="Ragnar"
    def receiveDamage(self, damage):
        newhealth=health-damage
        if newhealth >0:
            print(name," has received", damage," points of damage.")
        else:
            print(name," has died in act of combat.")
    def battleCry():
        return print("Odin owns you all!")
        

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        newhealth=health-damage
        if newhealth >0:
            print("A Saxon has received ", damage," points of damage.")
        else:
            print("A Saxon has died in combat.")

# War


class War():
    vikingArmy=[]
    saxonArmy=[]
    def addViking(Viking):
        vikingArmy.append(Viking)
    def addSaxon(Saxon):
        saxonArmy.append(Saxon)
    #def vikingAttack():
        
     