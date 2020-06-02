############################
# import the objects (classes and methods that we need for the test file)
from employee import Employee
from manager import Manager
import random # because we want a randomized SSN


class EmployeeList():

    ############################
    def __init__(self):
        self.employeelist = []

    ############################

    ############################
    def add(self, Employee):
        """
        adds newContact to the ContactList
        """
        self.employeelist.append(Employee)
    ############################

    ############################
    def __str__(self):
    #returns a string containing all the data in the Employeelist

        returnedString = ''
        for employee in self.employeelist:
            returnedString = returnedString + '\n' + str(employee) + '\n'
        return returnedString
    ############################

############################
# testing the Employee Class
print()
print('testing the Employee Class\n')
myEmployee01 = Employee('teo','espero',random.randint(100000000,999999999),3000)
print(myEmployee01)

############################
# testing the Employee.percentRaise method
print('\n')
print('testing the Employee.percentRaise method\n')
myEmployee01.giveRaise(10)
print(myEmployee01)

############################
# testing the Manager class
print('\n')
print('testing the Manager class\n')
myEmployee02 = Manager('teo','espero',random.randint(100000000,999999999),3000,'IT Admin',random.randint(1000,1500))
myEmployee02.giveRaise(10)
print(myEmployee02)

############################
# testing the Employee List Class
print('\n')
print('testing the Employee List Class')
myEmployee03 = Employee('juanito','osorio',random.randint(100000000,999999999),1000)
myEmployee04 = Employee('annie','grefal',random.randint(100000000,999999999),1500)
myEmployee05 = Manager('josephine','ybanez',random.randint(100000000,999999999),2500,'Asst. IT Admin',1000)
myEmployee06 = Employee('jeff','tuan',random.randint(100000000,999999999),1750)

############################
# give the employees a 10% raise iin a loop
mylist = [myEmployee03, myEmployee04, myEmployee05,myEmployee06]

for ctr in mylist:
    ctr.giveRaise(10) # you can also use giveRaise(.10)

############################
# add the employee information to our EmployeeList object
employeeList = EmployeeList()
for ctr in mylist:
    employeeList.add(ctr)

print(employeeList)

############################
# OUTPUT
"""

testing the Employee Class

Name: Teo Espero 
SSN: 687-12-5078 
Salary: $3,000.00


testing the Employee.percentRaise method

Name: Teo Espero 
SSN: 687-12-5078 
Salary: $3,300.00


testing the Manager class

Name: Teo Espero 
SSN: 600-20-8882                         
Salary: $3,300.00 
Manager: IT Admin
Annual Bonus: $1,089.00


testing the Employee List Class

Name: Juanito Osorio 
SSN: 584-60-7863 
Salary: $1,100.00

Name: Annie Grefal 
SSN: 392-87-2878 
Salary: $1,650.00

Name: Josephine Ybanez 
SSN: 810-85-8072                         
Salary: $2,750.00 
Manager: Asst. IT Admin
Annual Bonus: $1,000.00

Name: Jeff Tuan 
SSN: 927-48-8232 
Salary: $1,925.00


Process finished with exit code 0

"""