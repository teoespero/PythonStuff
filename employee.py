import string


class Employee():
# class Employee where one object of class Employee represents one Employee
# Employee will be our main class

    ############################
    def __init__(self, firstname, lastname, ssn, salary):
    # instance method as the initializer/constructor, with a parameter for the initial value of each instance variable


        self.firstname = firstname
        self.lastname = lastname
        self.socialsecuritynumber = ssn
        self.salary = salary
    ############################


    ############################
    def __str__(self):
    #  instance method to return the object's data in a string

        salary = "${:,.2f}".format(self.salary)
        ssn = str(self.socialsecuritynumber)
        formattedSSN = ssn[0:3] + '-' + ssn[3:5] + '-' + ssn[5:9]
        employeestring = f'Name: {self.firstname.title()} {self.lastname.title()} \nSSN: {formattedSSN} \nSalary: {salary}'

        return employeestring
    ############################

    def giveRaise(self, percentRaise):
    # instance method that takes a float "percentRaise" as parameter and doesn't return anything.
    # note that this method accepts both float and int

        if type(percentRaise) != float:
            if percentRaise > 1:
                percentRaise = float(percentRaise)/100

        self.salary = self.salary + (self.salary * percentRaise)

    ############################









