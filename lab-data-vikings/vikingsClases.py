
# Soldier


class Soldier:
    
    def __init__(self,health,strength) :
        self.health = health
        self.strength = strength 
    
    def attack(self) :
        return self.strength
    def recieveDamage(self,damage) :
        self.health = self.health - damage
   
 
# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength) :
        self.name = name
        
    def recieveDamage(self.damage) :
        self.health = self.health - damage
        if self.heath > 0 :
            return f'{self.name} has recieved {damage} points of damage'
        else :
            return f'{self.name} has died in combat'
        
    
    def battleCry(self) :
        return 'Odin Owns You All!'
        
    

# Saxon


class Saxon(Soldier):
    def __init__(self,health,stregth) :
        super()__init__(health, strenght)
    def recieveDamage(self,damage) :
        self.health = self.health - damage
        if self.health > 0 :
            return f'A Saxon has received {damage} points of damage'
        else :
            return f'A Saxon has died in combat'

# War


class War: #:(
    pass
