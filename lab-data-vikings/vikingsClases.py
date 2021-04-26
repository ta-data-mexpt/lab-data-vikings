
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    @staticmethod        
    def attack():
        return self.strength

    
    @staticmethod
    def receiveDamage(damage):
        return self.health - damage
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    @staticmethod    
    def receiveDamage(damage):
        self.health - damage
        if self.health > 0:
            print(self.name, "has received ", damage, " points of damage")
        else:
            print(self.name, " has died in act of combat")
    
    @staticmethod
    def battleCry():
        return "Odin Owns You All!"
        

# Saxon


class Saxon(Soldier):
    def __init__(health, strength):
        super().__init__(health, strength)
    
    @staticmethod
    def receiveDamage(damage):
        self.health - damage
        if self.health > 0:
            print("A Saxon has received ",damage," points of damage")
        else:
            print("A Saxon has died in combat")
    

# War


class War:
    pass
    def __init__(self, vikingArmy=None, saxonArmy=None):
        if vikingArmy and saxonArmy is None:
            self.vikingArmy = []
            self.saxonArmy = []
        else:
            self.vikingArmy = vikingArmy
            self.saxonArmy = saxonArmy
            
    def addViking(self, viking):
        if viking not in self.vikingArmy:
            self.vikingArmy.append(viking)
            
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
            
    def vikingAttack():
        saxon_attacked = random.choice(saxonArmy)
        
