class Sandwich():
    # Here we define a Sandwich class that at every instance the customer's name and the sandwich contents (bread,
    # cheese, meat, condiments and if it is toasted or not)

    ############################
    def __init__(self, name):
        #  Initializes a single new Sandwich object by storing the name as its instance variable name.
        #  This __init__() method also assign the initial value of None to all of the other instance variables.

        self.name = name
        self.breadName = None
        self.cheeseName = None
        self.meatName = None
        self.condiments = []
        self.toasted = False
    ############################


    ############################
    def __str__(self):
        # This method returns a string containing the description of the sandwich which includes a list of all the
        # ingredients and also indicates whether it is toasted or not.

        fill = ''

        # concatenate the sandwich fillings only if the sandwich ingredients have been
        # given a new value other than None

        if self.breadName != None:
            fill = fill + self.breadName + ', '
        if self.cheeseName != None:
            fill = fill + self.cheeseName + ', '
        if self.meatName != None:
            fill = fill + self.meatName + ', '
        if len(self.condiments) > 0:
            fill  = fill + (str(self.condiments)) + ', '
        else:

            # if the condiments list is empty (Null) we suppress the brackets
            # [] from showing when we print it

            fill = fill + str(self.condiments)[1:-1]

        if self.toasted:
            fill = fill + 'toasted'
        else:
            fill = fill + 'not toasted'
        sandwich = self.name +': '+ fill


        return sandwich
    ############################


    ############################
    def setBread(self, breadName):
        # This method sets the bread instance variable to contain the value in the parameter "breadName".

        self.breadName = breadName
    ############################


    ############################
    def setCheese(self, cheeseName):
        # This method sets the cheese instance variable to contain the value in the parameter "cheeseName".
        # there is a defined condition that there can only be 1 type of cheese per sandwich

        self.cheeseName = cheeseName
    ############################


    ############################
    def setMeat(self, meatName):
        # This method sets the meat instance variable to contain the value in the parameter "meatName".
        # there is a defined condition that there can only be 1 type of meat per sandwich

        self.meatName = meatName
    ############################


    ############################
    def addCondiment(self, additionalCondiment):
        # this method adds "additionalCondiment" to the list of condiments stored in the instance variable
        # for the condiments list.
        # since it is a list, a sandwich can have multiple condiments

        self.condiments.append(additionalCondiment)
    ############################


    ############################
    def setToasted(self, isToasted):
        # Sets the toasted instance variable to be True if the parameter "isToasted" is True, False is set by default.

        self.toasted = isToasted
    ############################


    ############################
    def price(self):
        # Returns the price (number) of the sandwich based on the price list below:
        #
        #       Basic cheese sandwich with one condiment = $4.50
        #       Meat added to the cheese sandwich        + $1.00
        #       Each additional condiment after the first+ $ .50

        basicSandwichPrice = 4.5

        if len(self.condiments) > 0:
            # if we just have one condiment the basic price should stick
            basicSandwichPrice = basicSandwichPrice + ((len(self.condiments) - 1) * 0.50)

        if self.meatName != None:
            # note that the 'meat' is $1 and if its None the customer
            # will not be charged
            basicSandwichPrice = basicSandwichPrice + 1.00

        return basicSandwichPrice
    ############################
