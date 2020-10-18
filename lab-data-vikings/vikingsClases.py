
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        return None

#test_sold1= Soldier(100,30)
#test_sold2 = Soldier(100,50)

#print(test_sold2.health)

#test_sold2.receiveDamage(test_sold1.attack())

#print(test_sold1.strength)
#print(test_sold2.health)

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            print(self.name, 'has received', damage, 'points of damage')
        else:
            print(self.name, 'has died in act of combat')

    def battleCry(self):
        return print('Odin Owns You All!')

#test_vik1= Viking('Ragnar',120,40)
#test_vik2 = Viking('Rollo',80,60)

#print(test_vik2.health)

#test_vik2.receiveDamage(test_vik1.attack())

#print(test_vik1.strength)
#print(test_vik2.health)

#test_vik2.receiveDamage(test_vik1.attack())

#test_vik2.battleCry()
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            print('A Saxon has received', damage, 'points of damage')
        else:
            print('A Saxon has died in combat')

#test_sax1= Saxon(80,20)
#test_sax2 = Saxon(80,20)

#print(test_sax2.health)

#test_sax2.receiveDamage(test_vik2.attack())

#print(test_sax1.strength)
#print(test_sax2.health)

#test_sax2.receiveDamage(test_sax1.attack())

# War

class War:
    
    pass
