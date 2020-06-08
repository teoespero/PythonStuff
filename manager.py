"""
import the the Employee class from employee.py
"""
import employee

import random

class Manager(employee.Employee):
    """
    File managerDoc.
    Manager class inherits all the instance variables of the Employee class
    """

    ##############################
    def __init__(self, firstname, lastname, ssn, salary, managertitle, annualbonus):
        """
        instance method as the constructor, with a parameter for the initial value of each        :param annualbonus:
        """

        employee.Employee.__init__(self,  firstname, lastname, ssn, salary)
        self.managertitle = managertitle
        self.annualbonus = annualbonus
    ##############################

    ##############################
    def __str__(self):
        """
        instance method to return the object's data in a string
        """

        salary = "${:,.2f}".format(self.salary)
        bonus = "${:,.2f}".format(self.annualbonus)
        ssn = str(self.socialsecuritynumber)
        formattedSSN = ssn[0:3] + '-' + ssn[3:5] + '-' + ssn[5:9]

        managerstring = f'Name: {self.firstname.title()} {self.lastname.title()} \nSSN: {formattedSSN} \
                        \nSalary: {salary} \nManager Title: {self.managertitle.title()}\nAnnual Bonus: {bonus}'

        return managerstring
##############################

##############################
if __name__ == "__main__":

    print('-------------------------------------------')

    ###############################
    # create an employee object

    print('create an employee object\n')

    ee = Manager('teo','espero',123456789,2000, 'it administrator',1000)
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
    myEmployee01 = employee.Employee('a', 'Espero', random.randint(100000000, 999999999), 2000)
    myEmployee02 = employee.Employee('A', 'espero', random.randint(100000000, 999999999), 3000)
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

    print('Manager.__doc__=' + Manager.__doc__)
    print('Manager.__init__.__doc__=' + Manager.__init__.__doc__)
    print('Manager.giveRaise.__doc__=' + Manager.giveRaise.__doc__)
    print('Manager.__str__.__doc__=' + Manager.__str__.__doc__)
    print('__doc__=' + __doc__)

    print('-----------------------------------------------')
##############################

##############################
#OUTPUT

"""
-------------------------------------------
create an employee object

Name: Teo Espero 
SSN: 123-45-6789                         
Salary: $2,000.00 
Manager Title: It Administrator
Annual Bonus: $1,000.00 

-------------------------------------------
use the giveRaise method

Name: Teo Espero 
SSN: 123-45-6789                         
Salary: $2,200.00 
Manager Title: It Administrator
Annual Bonus: $1,000.00 

-------------------------------------------
create instances for our Employee class

Name: A Espero 
SSN: 314-65-3464 
Salary: $2,000.00 

Name: A Espero 
SSN: 406-77-5051 
Salary: $3,000.00 

call the magic methods
__eq__ test --> True
__lt__ test --> False

-----------------------------------------------
create the docstring

Manager.__doc__=
    File managerDoc.
    Manager class inherits all the instance variables of the Employee class
    
Manager.__init__.__doc__=
        instance method as the constructor, with a parameter for the initial value of each        :param annualbonus:
        
Manager.giveRaise.__doc__=
        instance method that takes a float "percentRaise" as parameter and doesn't return anything.
        note that this method accepts both float and int
        
Manager.__str__.__doc__=
        instance method to return the object's data in a string
        
__doc__=
import the the Employee class from employee.py

-----------------------------------------------
"""
##############################