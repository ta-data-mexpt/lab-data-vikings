
# Soldier
class Soldier:
    def __init__(self,health,strenght):
        self.health=health
        self.strenght=strenght
    def attack(self):
        return self.strenght=strenght
    def receiveDamage(damage):
        self.health-=damage

# Viking
class Viking:
    def __init__(self,nombre,health,strenght):
        Soldier.__init__(self,health,strengh)
        self.nombre=nombre
    def receiveDamage(self,damage):
        self.health-=damage
        if Viking.health>0:
            return print(self.nombre,"has received DAMAGE points of damage")
        else:
            return print(self.nombre,"has died in act of combat")
    def battleCry(self):
        return print("Odin Owns You All!")

# Saxon
class Saxon(Soldier):
    def receiveDamage(self,damage):
        self.health-=damage
        if Viking.health>0:
            return print("A Saxon has received DAMAGE points of damage")
        else:
            return print("A Saxon has died in combat")

# War

class War:
    def __init__(self):
        vikingArmy=[]
        saxonArmy=[]
    def addViking():
        self.vikingArmy.append(Viking)
    def addSaxon():
        self.saxonArmy.append(Saxon)
    def vikingAttack():
    def saxonAttack():
    def showStatus():