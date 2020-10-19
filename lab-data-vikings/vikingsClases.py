
# Soldier


class Soldier:
    def __init__(self, health, strength):
    	self.health = health
    	self.strength =	strength
    	
    def attack(self):
    	return self.strength

    def receiveDamage(self, damage):
    	self.damage=damage
    	self.health= self.health-damage
    	return
    	

    pass

# Viking


class Viking(Soldier):
	def __init__(self, name, health, strength):
		self.name =	name
		Soldier.__init__(self, health, strength)

	def attack(self):
		return self.strength
	def receiveDamage(self, damage):
		self.health = self.health- damage
		if self.health > 0:
			return self.name + " has received "+ str(damage) + " points of damage"
		else:
			return self.name +' has died in act of combat'

	def battleCry(self):
		return "Odin Owns You All!"
	pass

# Saxon


class Saxon(Soldier):
	def __init__(self, health, strength):
		super().__init__(health, strength)
	def attack(self):
		return self.strength
	def receiveDamage(self,damage):
		self.health=self.health-damage
		if self.health>0:
			return "A Saxon has received "+ str(damage)+" points of damage"
		else:
			return "A Saxon has died in combat"
	
# War
class War:
	vikingArmy =[]
	saxonArmy=[]
	def addViking(self, Viking):
		self.Viking= vikingArmy.append(1)
		return
	def addSaxon(self, Saxon):
		self.Saxon= saxonArmy.append(1)
	pass


