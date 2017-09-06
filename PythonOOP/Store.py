class Store(object):
    def __init__(self, location, owner):
        self.inventory = []
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.inventory.append(product)
        return self
    
    def remove_product(self, product):
        self.inventory.remove(product)
        return self
    
    def inventoryStatus(self):
        print "Here is the stores inventory", self.inventory



store1 = Store("Tysons", "Sam")


store1.add_product("computer").inventoryStatus()

