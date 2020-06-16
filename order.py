############################
class Order():
    # our Order class is defined to hold the sandwich orders passed on as an argument
    # note that the sandwich argument itself is an object as defined in the Sandwich object

    ############################
    def __init__(self):
        # __init__(self) initializes an empty Order object.
        self.sandwichOrder = None
        self.orderNumber = 0
        self.orderTotal = 0.00
    ############################

    ############################
    def addSandwich(self, newSandwich):
        # addSandwich(self, newSandwich) adds newSandwich to the Order. The parameter newSandwich must already
        # be a fully initialized Sandwich object.
        if self.sandwichOrder == None:
            self.sandwichOrder = ''
        self.orderNumber = self.orderNumber + 1
        if (self.orderNumber > 1):
            self.sandwichOrder = self.sandwichOrder + '\n'
        orderitems = ''
        orderitems = 'Sandwich ' + str(self.orderNumber) + ': ' + orderitems  + str(newSandwich)
        self.orderTotal = self.orderTotal + newSandwich.price()
        self.sandwichOrder = self.sandwichOrder + orderitems
    ############################

    ############################
    def __str__(self):
        # __str__(self) returns a string containing the names and contents of all the Sandwiches in the Order.
        if self.sandwichOrder == None:
            raise ValueError
        else:
            return str(self.sandwichOrder)
    ############################

    ############################
    def price(self):
        # price(self) returns the total price of all the Sandwiches in the Order.

        return self.orderTotal
    ############################
