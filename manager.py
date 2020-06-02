from employee import Employee
# Manager class inherits all the instance variables of the Employee class

############################
class Manager(Employee):

    ############################
    def __init__(self, firstname, lastname, ssn, salary, managertitle, annualbonus):
        #  Initializes a single new Sandwich object by storing the name as its instance variable name.
        #  This __init__() method also assign the initial value of None to all of the other instance variables.

        Employee.__init__(self,  firstname, lastname, ssn, salary)
        self.managertitle = managertitle
        self.annualbonus = annualbonus
    ############################

    ############################
    def __str__(self):
        # This method returns a string containing the description of the sandwich which includes a list of all the
        # ingredients and also indicates whether it is toasted or not.

        salary = "${:,.2f}".format(self.salary)
        bonus = "${:,.2f}".format(self.annualbonus)
        ssn = str(self.socialsecuritynumber)
        formattedSSN = ssn[0:3] + '-' + ssn[3:5] + '-' + ssn[5:9]

        managerstring = f'Name: {self.firstname.title()} {self.lastname.title()} \nSSN: {formattedSSN} \
                        \nSalary: {salary} \nManager: {self.managertitle}\nAnnual Bonus: {bonus}'

        return managerstring
    ############################