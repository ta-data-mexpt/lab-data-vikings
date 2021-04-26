
# Soldier
class Soldier:
    # constructor function
    # should receive **2 arguments** (health & strength)
    # should receive the **`health` property** as its **1st argument**
    # should receive the **`strength` property** as its **2nd argument**
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    #### `attack()` method
    # should be a function
    # should receive **0 arguments**
    # should return **the `strength` property of the `Soldier`**
    def attack(self):
        return self.strength

    #### `receiveDamage()` method
    # should be a function
    # should receive **1 argument** (the damage)
    # should remove the received damage from the `health` property
    # **shouldn't return** anything 
    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking
# Viking should inherit from Soldier
class Viking(Soldier):
    # constructor function
    # should receive 3 arguments (name, health & strength)
    # should receive the name property as its 1st argument
    # should receive the health property as its 2nd argument
    # should receive the strength property as its 3rd argument   
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    # viking strength method
    def vikingStrength(self):
        return self.strength

    #### `attack()` method
    # (This method should be **inherited** from `Soldier`, no need to reimplement it.)
    # should be a function
    # should receive **0 arguments**
    # should return **the `strength` property of the `Viking`**
    def attack(self):
            return super().attack()
    
    #### `receiveDamage()` method
    # (This method needs to be **reimplemented** for `Viking` because the `Viking` version needs to have different return values.)
    # should be a function
    # should receive **1 argument** (the damage)
    # should remove the received damage from the `health` property
    # **if the `Viking` is still alive**, it should return **"NAME has received DAMAGE points of damage"**
    # **if the `Viking` dies**, it should return **"NAME has died in act of combat"**
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            answer = self.name + " has received " + str(damage) + " points of damage"
        else:
            answer = self.name + " has died in act of combat"
        return answer

    #### `battleCry()` method
    # [Learn more about battle cries](http://www.artofmanliness.com/2015/06/08/battle-cries/).
    # should be a function
    # should receive **0 arguments**
    # should return **"Odin Owns You All!"**
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
# inheritance
# Saxon should inherit from Soldier
class Saxon(Soldier):
    # constructor function
    # should receive 2 arguments (health & strength)
    # should receive the health property as its 1st argument
    # should receive the strength property as its 2nd argument
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    # viking strength method
    def saxonStrength(self):
        return self.strength

    # attack() method
    # (This method should be inherited from Soldier, no need to reimplement it.)
    # should be a function
    # should receive 0 arguments
    # should return the strength property of the Saxon           
    def attack(self):
        return super().attack()

    # receiveDamage() method
    # (This method needs to be reimplemented for Saxon because the Saxon version needs to have different return values.)
    # should be a function
    # should receive 1 argument (the damage)
    # should remove the received damage from the health property
    # if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
    # if the Saxon dies, it should return "A Saxon has died in combat"
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            answer = "A Saxon has received " + str(damage) + " points of damage"
        else:
            answer = "A Saxon has died in combat"
        return answer

# War
class War:
    # constructor function
    # When we first create a War, the armies should be empty. We will add soldiers to the armies later.
    # should receive 0 arguments
    # should assign an empty array to the vikingArmy property
    # should assign an empty array to the saxonArmy property    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    # addViking() method
    # Adds 1 Viking to the vikingArmy. If you want a 10 Viking army, you need to call this 10 times.
    # should be a function
    # should receive 1 argument (a Viking object)
    # should add the received Viking to the army
    # shouldn't return anything
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    # addSaxon() method
    # The Saxon version of addViking().
    # should be a function
    # should receive 1 argument (a Saxon object)
    # should add the received Saxon to the army
    # shouldn't return anything
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    # vikingAttack() method
    # A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.
    # should be a function
    # should receive 0 arguments
    # should make a Saxon receiveDamage() equal to the strength of a Viking
    # should remove dead saxons from the army
    # should return result of calling receiveDamage() of a Saxon with the strength of a Viking
    def vikingAttack(self):
        saxonDamage = Saxon.receiveDamage(Viking.attack)
        self.saxonArmy = filter(lambda x: x>0, [Saxon.health for Saxon.health in self.saxonArmy])
        return saxonDamage

    # saxonAttack() method
    # The Saxon version of vikingAttack(). A Viking receives the damage equal to the strength of a Saxon.
    # should be a function
    # should receive 0 arguments
    # should make a Viking receiveDamage() equal to the strength of a Saxon
    # should remove dead vikings from the army
    # should return result of calling receiveDamage() of a Viking with the strength of a Saxon
    def saxonAttack(self):
        vikingDamage = Viking.receiveDamage(Saxon.attack)
        self.vikingArmy = filter(lambda x: x>0, [Viking.health for Viking.health in self.vikingArmy])
        return vikingDamage

    # showStatus() method
    # Returns the current status of the War based on the size of the armies.
    # should be a function
    # should receive 0 arguments
    # if the Saxon array is empty, should return "Vikings have won the war of the century!"
    # if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
    # if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."

