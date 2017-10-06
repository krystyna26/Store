class Product(object):
    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        taxAmount = tax * self.price
        self.price += taxAmount
        print "Tax:",taxAmount
        return self
    def returnProduct(self,reason):
        if reason == "defective": # reason is not for each product that why we dont say "self.reason"
            self.status = "defective"
            self.price = 0
        if reason == "box":
            self.status = "for sale"
        if reason == "openBox":
            self.status = "used"
            discount =(0.20 * self.price)
            self.price = self.price - discount
            print "Reason:", reason
            print "Discount:",discount
        return self
    def displayInfo(self):
        print "Price:", self.price
        print "Name:", self.itemName
        print "Status:",self.status
        print "Brand:", self.brand
        print "Weight:", self.weight
        print "Cost:", self.cost
        print "\n"

shoes = Product(50, "Snickers", "5", "Nike", 2)
pants = Product(80, "Blue jeans", "6", "Lewis", 10)
shirt = Product(60, "White Shirt", "2", "Kalvin Klein", 9)





class Store(object):
    def __init__(self, location, owner):
        self.products = [] # an list of products objects
        self.location = location # store address
        self.owner = owner #  store owner's name
    
    def addProduct(self,items): # add a product to the store's product list
        self.products = items
        count = 0
        for i in self.products:
            # i.displayInfo()
            count += 1
        print count, "item(s) added to products list"
        return self
    def remove_product(self, item): # hould remove a product according to the product name
        self.products.remove(item)
        return self
    def inventory(self): # print relevant information about each product in the store
        # self.products = items
            for i in self.products:
                print i.itemName.upper()
                i.displayInfo()

ikea = Store("San Jose", "John Smith")
myProducts = []
myProducts.append(shoes)
myProducts.append(pants)
myProducts.append(shirt)
ikea.addProduct(myProducts)
# ikea.remove_product(pants) # ValueError: list.remove(x): x not in list
ikea.inventory()