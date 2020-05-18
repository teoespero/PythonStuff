class Sandwich():
    ## modified 05182020 - 1:43 PM

    def __init__(self, name):
        # name - a string containing the name of the person who is asking for this sandwich to be made.
        # bread - a string containing the type of bread that the sandwich is on.
        # cheese - a string containing the type of cheese that will be put into the sandwich
        # meat - a string containing the type of meat that will be put into the sandwich
        # condiments - a Python list of strings, where each string in the Python list contains the name of the requested condiment.
        # toasted - a boolean variable set to True if the customer wants the sandwich to be toasted, and set to False if the customer wants the sandwich NOT to be toasted.

        self.name = name
        self.breadName = 'None'
        self.cheeseName = 'None'
        self.meatName = 'None'
        self.additionalCondiment = []
        self.toasted = False



    def __str__(self):
        delimeter = ''

        # null out the empty fills before concatenation
        if self.breadName == 'None': self.breadName = ''
        if self.cheeseName == 'None': self.cheeseName = ''
        if self.meatName == 'None': self.meatName = ''

        # concatenate the sandwich fillings
        fill =  self.breadName.title() \
                + self.cheeseName.title() \
                + self.meatName.title()


        if len(self.additionalCondiment) >= 1:
            # if our condiments list is still empty, suppress the brackets
            # print(len(self.additionalCondiment))
            fill  = fill + (str(self.additionalCondiment).title()) + ', '
        else:
            fill = fill + str(self.additionalCondiment)[1:-1].title()
        #if len(fill.strip()) > 0:
        #    # if we have more than the breadname, change the initial delimeter to a ,
        #    delimeter = ','

        if self.toasted:
            fill = fill + f'{delimeter}toasted'
        else:
            fill = fill + f'{delimeter}not toasted'
        sandwich = self.name.title() +': '+ fill.title()

        return sandwich


    def setBread(self, breadName):
        self.breadName = breadName + ', '

    def setCheese(self, cheeseName):
        self.cheeseName = cheeseName + ', '

    def setMeat(self, meatName):
        self.meatName = meatName + ', '

    def addCondiment(self, additionalCondiment):
        self.additionalCondiment.append(additionalCondiment)

    def setToasted(self, isToasted):
        if isToasted == True:
            self.toasted = True

    def price(self):
        basicSandwichprice = 4.5

        if len(self.additionalCondiment) > 0:
            # if we just have one condiment the basic price should stick
            basicSandwichprice = basicSandwichprice + ((len(self.additionalCondiment) - 1) * 0.50)
        else:
            # otherwise charge an additional .50 cents
            basicSandwichprice = basicSandwichprice + (len(self.additionalCondiment) * 0.50)

        if len(self.meatName) > 0:
            basicSandwichprice = basicSandwichprice + 1.00
        return basicSandwichprice