class Converter:
    # this class and methods are created to perform the
    # computations needed in the conversion

    ############################
    def __init__(self):
        # initialize the object that will hold our
        # converted value

        self.resultingTemp = 0

    ############################

    ############################
    def FtoC(self, temp):
        # convert temperatures in fahrenheit to temperatures in celsius

        self.resultingTemp =  (5/9)*(temp-32)
    ############################

    ############################
    def CtoF(self, temp):
        # convert temperatures in celsius to temperatures in fahrenheit\

        self.resultingTemp = ((9/5)*temp)+32
    ############################

    ############################
    def __str__(self):
        # return the converted value as a string

        formattedValue = '%.2f' % self.resultingTemp
        return str(formattedValue)
    ############################