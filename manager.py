import employee
# Manager class inherits all the instance variables of the Employee class

############################
class Manager(employee.Employee):

    ############################
    def __init__(self, firstname, lastname, ssn, salary, managertitle, annualbonus):
        #  instance method as the constructor, with a parameter for the initial value of each

        employee.Employee.__init__(self,  firstname, lastname, ssn, salary)
        self.managertitle = managertitle
        self.annualbonus = annualbonus
    ############################

    ############################
    def __str__(self):
        # instance method to return the object's data in a string
        salary = "${:,.2f}".format(self.salary)
        bonus = "${:,.2f}".format(self.annualbonus)
        ssn = str(self.socialsecuritynumber)
        formattedSSN = ssn[0:3] + '-' + ssn[3:5] + '-' + ssn[5:9]

        managerstring = f'Name: {self.firstname.title()} {self.lastname.title()} \nSSN: {formattedSSN} \
                        \nSalary: {salary} \nManager Title: {self.managertitle}\nAnnual Bonus: {bonus}'

        return managerstring
    ############################