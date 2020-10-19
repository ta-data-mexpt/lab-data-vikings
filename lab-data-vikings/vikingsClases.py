
# Soldier


class Soldier:
    pass

    def __init__(self,health,strenght):
    	self.health = health 
    	self.strenght = strenght

    def attack(self):
    	return self.strenght 

    def receiveDamage(self,damage):
    	self.health = self.health - damage


# Viking


class Viking:
    pass

    def __init__(self,name,health,strenght)
        self.name = name
        self.health = health
        self.strength = strength

##NO NEED TO REIMPLEMENT DE ATTACK METHOD AS IT INHERITS FROM SOLDIER AND THERE IS NO NEED TO BE MODIFIED 

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+"has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon:
    pass

	def __init__(self,health,strenght)
        self.health = health
        self.strength = strength

##NO NEED TO REIMPLEMENT DE ATTACK METHOD AS IT INHERITS FROM SOLDIER AND THERE IS NO NEED TO BE MODIFIED 

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in act of combat"


#BONUSSS

# War


class War:
    pass
