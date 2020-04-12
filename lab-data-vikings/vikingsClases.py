
# Soldier

#Modify the Soldier constructor function and add 2 methods to its prototype: attack(), and receiveDamage().
#constructor function
#should receive 2 arguments (health & strength)
#should receive the health property as its 1st argument
#should receive the strength property as its 2nd argument

class Soldier:
    def __init__(self, health, strength):
        # add code here
        #self.soldiers_health = health
        self.health = health
        #self.soldiers_strength = strength   
        self.strength = strength
        
#attack() method
#should be a function
#should receive 0 arguments
#@staticmethod
#def test():
#    print('test')
#should return the strength property of the Soldier
 
    #@staticmethod   #decorator para no usar attack(self) --> lo detectó como error el test, por qué?
    def attack(self):
        #return self.soldiers_strength
        return self.strength
    
#receiveDamage() method
#should be a function
#should receive 1 argument (the damage)
#should remove the received damage from the health property
#shouldn't return anything

    def receiveDamage(self, damage):
        self.health -= damage


# Viking


#A Viking is a Soldier with an additional property, their name. They also have a different receiveDamage() method and new method, battleCry().
#Modify the Viking constructor function, have it inherit from Soldier, reimplement the receiveDamage() method for Viking, and add a new battleCry() method.
#inheritance:
#Viking should inherit from Soldier
#constructor function
#should receive 3 arguments (name, health & strength)
#should receive the name property as its 1st argument
#should receive the health property as its 2nd argument
#should receive the strength property as its 3rd argument

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        #self.viking_name = name
        self.name = name
        
#class Student(Person):
#  def __init__(self, fname, lname, year):
#    super().__init__(fname, lname) <==> Person.__init__(self, fname, lname)
#    self.graduationyear = year


#attack() method

#(This method should be inherited from Soldier, no need to reimplement it.)

#should be a function
#should receive 0 arguments
#should return the strength property of the Viking

# Attack ya está desde el parent

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
    

#receiveDamage() method

#(This method needs to be reimplemented for Viking because the Viking version needs to have different return values.)

#should be a function
#should receive 1 argument (the damage)
#should remove the received damage from the health property
#if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
#if the Viking dies, it should return "NAME has died in act of combat"


    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            #print(self.name + ' has received ' + str(damage) + ' points of damage')
            #return "{self.name} has received {str(damage)} points of damage"
            return self.name + ' has received ' + str(damage) + ' points of damage'
        else:
            #print(self.name + ' has died in act of combat')
            return self.name + " has died in act of combat"

            
#battleCry() method

#Learn more about battle cries.

#should be a function
#should receive 0 arguments
#should return "Odin Owns You All!"

    def battleCry(self):
        return "Odin Owns You All!"

    
# Saxon


#A Saxon is a weaker kind of Soldier. Unlike a Viking, a Saxon has no name. Their receiveDamage() method will also be different than the original Soldier version.
#Modify the Saxon, constructor function, have it inherit from Soldier and reimplement the receiveDamage() method for Saxon.
#inheritance
#Saxon should inherit from Soldier
#constructor function
#should receive 2 arguments (health & strength)
#should receive the health property as its 1st argument
#should receive the strength property as its 2nd argument


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)


#receiveDamage() method
#(This method needs to be reimplemented for Saxon because the Saxon version needs to have different return values.)
#should be a function
#should receive 1 argument (the damage)
#should remove the received damage from the health property
#if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
#if the Saxon dies, it should return "A Saxon has died in combat"


    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
    

# War


#Now we get to the good stuff: WAR! Our War constructor function will allow us to have a Viking army and a Saxon army that battle each other.

#Modify the War constructor and add 5 methods to its prototype:

#addViking()
#addSaxon()
#vikingAttack()
#saxonAttack()
#showStatus()
#constructor function

#When we first create a War, the armies should be empty. We will add soldiers to the armies later.

#should receive 0 arguments
#should assign an empty array to the vikingArmy property
#should assign an empty array to the saxonArmy property


import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
#import random
#addViking() method

#Adds 1 Viking to the vikingArmy. If you want a 10 Viking army, you need to call this 10 times.

#should be a function
#should receive 1 argument (a Viking object)
#should add the received Viking to the army
#shouldn't return anything


    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        

#addSaxon() method

#The Saxon version of addViking().

#should be a function
#should receive 1 argument (a Saxon object)
#should add the received Saxon to the army
#shouldn't return anything


    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        

#vikingAttack() method

#A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.

#should be a function
#should receive 0 arguments
#should make a Saxon receiveDamage() equal to the strength of a Viking
#should remove dead saxons from the army
#should return result of calling receiveDamage() of a Saxon with the strength of a Viking


    def vikingAttack(self):
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)
        saxon_damage = saxon_soldier.receiveDamage(viking_soldier.attack())
        if saxon_soldier.health <= 0:
            self.saxonArmy.remove(saxon_soldier)
        return saxon_damage    
            
        
#saxonAttack() method

#The Saxon version of vikingAttack(). A Viking receives the damage equal to the strength of a Saxon.

#should be a function
#should receive 0 arguments
#should make a Viking receiveDamage() equal to the strength of a Saxon
#should remove dead vikings from the army
#should return result of calling receiveDamage() of a Viking with the strength of a Saxon


    def saxonAttack(self):
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)
        viking_damage = viking_soldier.receiveDamage(saxon_soldier.attack())
        if viking_soldier.health <= 0:
            self.vikingArmy.remove(viking_soldier)
        return viking_damage    
        

#showStatus() method

#Returns the current status of the War based on the size of the armies.

#should be a function
#should receive 0 arguments
#if the Saxon array is empty, should return "Vikings have won the war of the century!"
#if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
#if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."

        
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







