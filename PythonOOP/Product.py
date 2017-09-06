class Product(object):
    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def displayInfo(self):
        print "Price:", self.price
        print "Item name:", self.itemName
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
    
    def sell (self):
        self.status = "sold"
        return self
    
    def addTax (self, tax):
        self.price = (self.price * tax) + self.price
        return self
    
    def returnItem (self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "box open":
            self.status = "box opened"
            self.price = self.price - (self.price * .2)
        return self


computer = Product(1000, "Computer", "5lbs", "Asus", 700)

computer.addTax(.05).returnItem("box open").displayInfo()
            