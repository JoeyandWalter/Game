class Hero(object):
    def __init__(self):
        self.name = ""
        self.weapon = ""
        self.health = 0
        
    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("you died")
        

class Weapon(object):
    def __init__(self):
        self.name = ""
        self.damage = 0
       


class Monster(object):
    def __init__(self):
        self.name = ""
        self.health = 0
        self.weapon = 0
        
    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("monster died")
      


#hero instances      
joey = Hero()
joey.name = 'joey'
joey.weapon = sword
joey.health = 1000

walter = Hero()
walter.name = 'walter'
walter.weapon = bow
walter.health = 1000
         


#moster instances   
ogre = Monster()
ogre.health = 500
ogre.weapon = axe



#weapon instances
sword = Weapon()
sword.name = 'sword'
sword.damage = 30

bow = Weapon()
bow.name = 'bow'
bow.damage = 5

axe = Weapon()
axe.name = 'axe'
axe.damage = 50


#battle loop, ends when one side reaches 0 health
while walter.health >0 and ogre.health > 0:
    x = walter.weapon.damage
    y = ogre.weapon.damage
    ogre.decrease_health(x)

    walter.decrease_health(y)



    print("Ogre health: " + str(ogre.health))
    print("Hero health: " + str(walter.health))