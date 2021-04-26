
# Soldier

@@ -10,15 +5,45 @@ 

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strenght = strength

#Poder del ataque de Soldier
    def attack(self):
        return self.strenght

#Para recibir un ataque, restamos el daño a la salud que tiene.
    def receiveDamage(self,damage):
        self.health = health - damage


    
# Viking


class Viking:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strenght = strength
        
    def receiveDemage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name,damage)
        else:
            return '{} has died in act of combat'.format(self.name)

    def battleCry(self):
        return 'Odin Owns You All!'       
        
               
        
# Saxon


class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strenght

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'

        
        
# War


class War:
    pass
