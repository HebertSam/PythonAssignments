class Bike (object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        if self.miles <= 0:
            print "you have not gone anywhere"
        else:
            self.miles -= 5
            print "Reversing"
        return self

bike1 = Bike(100, 50)
bike2 = Bike(200, 60)
bike3 = Bike(150, 55)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()