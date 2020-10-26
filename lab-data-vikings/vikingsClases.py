
# Soldier


class Soldier:
	def __init__(self, health, strength):
		self.health = health
		self.strength = strength

	def attack(self):
		return self.strength

	def receiveDamage(self):
		self.damage = f"(self.health) - (receiveDamage)"
    

# Viking


class Viking:
	Viking.__init__(Soldier)

	def __init__(self, name, health, strength):
		self.name = name
		self.health = health
		self.strength = strength

	def name(self):
		return self.name

	def attack(self):
		return self.strength

	def receiveDamage(self):
		self.damage = f"(self.health) - (receiveDamage)"
		if self.damage is != 0:
			return "self.name + " has received" + self.damage + " points of damage""
		if self.damage is == 0:
			return "self.name + " has died in act of combat""

	def battleCry(self):
		return ""Odin Owns You All!""
    

# Saxon


class Saxon(Soldier):
	Saxon.__init__(Soldier):

def __init__(self, health, strength):
	self.health = health
	self.strength = strength

def attack(self):
	return self.strength

def receiveDamage(self, damage):
	self.damage = self.health - damage
	if self.damage is != 0:
		return "self.name + " has received" + self.damage + " points of damage""
	if self.damage is == 0:
		return "self.name + " has died in act of combat""
    

# War


class War:
    pass
