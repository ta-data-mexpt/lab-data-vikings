
from random import randint


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
            print(self.name, 'has received', damage, 'points of damage')
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
            print('A Saxon has received', damage, 'points of damage')
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

    def __init__(self, vikingArmy = [], saxonArmy = []):
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy

    def addViking(self, name, health, strength):
        self.vikingArmy.append(Viking(name, health, strength))

    def addSaxon(self, health, strength):
        self.saxonArmy.append(Saxon(health, strength))

    def vikingAtack(self):
        random_saxon = self.saxonArmy[randint(0,len(self.saxonArmy)-1)]
        random_viking = self.vikingArmy[randint(0,len(self.vikingArmy)-1)]
        viking_attack = random_saxon.receiveDamage(random_viking.attack())

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)

        return viking_attack

    def saxonAttack(self):
        random_saxon = self.saxonArmy[randint(0,len(self.saxonArmy)-1)]
        random_viking = self.vikingArmy[randint(0,len(self.vikingArmy)-1)]
        saxon_attack = random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

        return saxon_attack

    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            print('Vikings have won the war of the century!')

        elif len(self.vikingArmy) <= 0:
            print('Saxons have fought for their lives and survive another day...')

        else:
            print('Vikings and Saxons are still in the thick of battle.')

test_war = War()

print(test_war.vikingArmy)
print(test_war.saxonArmy)

test_war.addViking('Ragnar',120,40)
test_war.addViking('Rollo',80,60)
test_war.addSaxon(80, 20)
test_war.addSaxon(80, 20)

test_war.vikingAtack()
test_war.showStatus()

test_war.saxonAttack()
test_war.showStatus()

test_war.vikingAtack()
test_war.showStatus()

test_war.saxonAttack()
test_war.showStatus()


test_war.vikingAtack()
test_war.showStatus()

test_war.saxonAttack()
test_war.showStatus()


test_war.vikingAtack()
test_war.showStatus()
