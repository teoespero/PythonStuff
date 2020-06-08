
"""
File employeeDoc.
class Employee where one object of class Employee represents one Employee. Employee will be our main class
"""

import random

class Employee():
    """
    File employeeDoc.
    class Employee where one object of class Employee represents one Employee. Employee will be our main class
    """

    ##############################
    def __init__(self, firstname, lastname, ssn, salary):
        """
        instance method as the initializer/constructor, with a parameter for the initial value of each instance variable
        :param firstname: string
        :param lastname: string
        :param ssn: integer
        :param salary: integer
        """


        self.firstname = firstname
        self.lastname = lastname
        self.socialsecuritynumber = ssn
        self.salary = salary
    ##############################

    ##############################
    def __str__(self):
        """
        instance method to return the object's data in a string

        :return: employeestring
        """

        salary = "${:,.2f}".format(self.salary)
        ssn = str(self.socialsecuritynumber)
        formattedSSN = ssn[0:3] + '-' + ssn[3:5] + '-' + ssn[5:9]
        employeestring = f'Name: {self.firstname.title()} {self.lastname.title()} \nSSN: {formattedSSN} \nSalary: {salary}'

        return employeestring
    ##############################

    ##############################
    def giveRaise(self, percentRaise):
        """
        instance method that takes a float "percentRaise" as parameter and doesn't return anything.
        note that this method accepts both float and int
        """

        if type(percentRaise) != float:
            if type(percentRaise) == int:
                if percentRaise >= 1:
                    percentRaise = float(percentRaise)/100
        self.salary = self.salary + (self.salary * percentRaise)
    ##############################

    ##############################
    def __eq__(self, other):
        """
        Returns True if self == other, False otherwise
        :param other:
        :return: True/False
        """

        return (self.firstname.lower() == other.firstname.lower() and self.lastname.lower() == other.lastname)
    ##############################

    ##############################
    def __lt__(self, other):
        """
        Returns True if self < other, False otherwise
        :param other:
        :return: True/False
        """

        if self.lastname.lower() == other.lastname.lower():
            if self.firstname.lower() < other.firstname.lower():
                return True
            else:
                return False
        elif self.lastname.lower() < other.lastname.lower():
            return True
        else:
            return False
##############################

##############################
if __name__ == "__main__":

    print('-------------------------------------------')

    ###############################
    # create an employee object

    print('create an employee object\n')
    ee = Employee('teo','espero',123456789,2000)
    print(ee,'\n')

    print('-------------------------------------------')

    ###############################
    # use the giveRaise method
    print('use the giveRaise method\n')
    ee.giveRaise(10)
    print(ee,'\n')

    print('-------------------------------------------')

    ############################
    # create instances for our Employee class
    print('create instances for our Employee class\n')
    myEmployee01 = Employee('alvin', 'Espero', random.randint(100000000, 999999999), 2000)
    myEmployee02 = Employee('Alvin', 'espero', random.randint(100000000, 999999999), 3000)
    print(myEmployee01, '\n')
    print(myEmployee02, '\n')

    ############################
    # call the magic methods
    print('call the magic methods')
    print('__eq__ test -->', myEmployee01 == myEmployee02)
    print('__lt__ test -->', myEmployee01 < myEmployee02)

    print('\n-----------------------------------------------')

    ###############################
    # create the docstring

    print('create the docstring\n')

    print('Employee.__doc__=' + Employee.__doc__)
    print('Employee.__init__.__doc__=' + Employee.__init__.__doc__)
    print('Employee.giveRaise.__doc__=' + Employee.giveRaise.__doc__)
    print('Employee.__str__.__doc__=' + Employee.__str__.__doc__)
    print('__doc__=' + __doc__)

    print('-----------------------------------------------')
##############################

##############################
# OUTPUT
"""
-------------------------------------------
create an employee object

Name: Teo Espero 
SSN: 123-45-6789 
Salary: $2,000.00 

-------------------------------------------
use the giveRaise method

Name: Teo Espero 
SSN: 123-45-6789 
Salary: $2,200.00 

-------------------------------------------
create instances for our Employee class

Name: Alvin Espero 
SSN: 999-12-4755 
Salary: $2,000.00 

Name: Alvin Espero 
SSN: 322-42-7080 
Salary: $3,000.00 

call the magic methods
__eq__ test --> True
__lt__ test --> False

-----------------------------------------------
create the docstring

Employee.__doc__=
    File employeeDoc.
    class Employee where one object of class Employee represents one Employee. Employee will be our main class
    
Employee.__init__.__doc__=
        instance method as the initializer/constructor, with a parameter for the initial value of each instance variable
        :param firstname: string
        :param lastname: string
        :param ssn: integer
        :param salary: integer
        
Employee.giveRaise.__doc__=
        instance method that takes a float "percentRaise" as parameter and doesn't return anything.
        note that this method accepts both float and int
        
Employee.__str__.__doc__=
        instance method to return the object's data in a string

        :return: employeestring
        
__doc__=
File employeeDoc.
class Employee where one object of class Employee represents one Employee. Employee will be our main class

-----------------------------------------------
"""
##############################