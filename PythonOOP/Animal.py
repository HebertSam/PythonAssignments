class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = health
        self.health = 100

        
    
    def walk(self):
        self.health -= 1
        print "walking"
        return self
    
    def run(self):
        self.health -= 5
        print "running"
        return self

    def displayHealth(self):
        print self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        # self.health = 150
        
    
    def pet(self):
        self.health += 5
        print "petting"
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        print "flying"
        return self

    def dragonHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

dog1 = Dog("bob")
dragon1 = Dragon("Gary")
cat = Animal("jill")


dog1.displayHealth()
dragon1.displayHealth()
dragon1.dragonHealth()
cat.displayHealth()