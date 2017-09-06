class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax


car1 = Car(2000, 45, "full", "25mpg")
car2 = Car(11000, 100, "full", "15mpg")
car3 = Car(1100, 100, "half full", "30mpg")
car4 = Car(11000, 100, " full", "50mpg")
car5 = Car(1500, 100, "half full", "20mpg")
car6 = Car(10000, 100, "half full", "100mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()