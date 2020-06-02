############################
# import the objects (classes and methods that we need for the test file)
import employee
import manager
import random # because we want a randomized SSN


class EmployeeList():

    ############################
    def __init__(self):
        self.employeelist = []

    ############################

    ############################
    def add(self, Employee):
        """
        adds a new Employee to the EmployeeList
        """
        self.employeelist.append(Employee)
    ############################

    ############################
    def __str__(self):
    # returns a string containing all the data in the Employeelist

        returnedString = ''
        for employee in self.employeelist:
            returnedString = returnedString + '\n' + str(employee) + '\n'
        return returnedString
    ############################

############################
# testing the Employee Class
print('testing the Employee Class\n')
myEmployee01 = employee.Employee('teo','espero',random.randint(100000000,999999999),3000)
print(myEmployee01)

############################
# testing the Employee.giveRaise method
print('\n')
print('testing the Employee.giveRaise method\n')
try:
  myEmployee01.giveRaise(10) # you can also use giveRaise(.10)
except TypeError:
  print('Cannot work with non-numeric values')
except ValueError:
  print('Cannot compute raises for negative values')
print(myEmployee01)

############################ContactList
# testing the Manager class
print('\n')
print('testing the Manager class\n')
myEmployee02 = manager.Manager('teo','espero',random.randint(100000000,999999999),3000,'IT Admin',random.randint(1000,1500))
try:
  myEmployee02.giveRaise(.10) # you can also use giveRaise(10)
except TypeError:
  print('Cannot work with non-numeric values')
except ValueError:
  print('Cannot compute raises for negative values')
print(myEmployee02)

############################
# testing the Employee List Class
print('\n')
print('testing the Employee List Class')
myEmployee03 = employee.Employee('juanito','osorio',random.randint(100000000,999999999),1000)
myEmployee04 = employee.Employee('annie','grefal',random.randint(100000000,999999999),1500)
myEmployee05 = manager.Manager('josephine','ybanez',random.randint(100000000,999999999),2500,'Asst. IT Admin',1000)
myEmployee06 = employee.Employee('jeff','tuan',random.randint(100000000,999999999),1750)

############################
# give the employees a 10% raise iin a loop
mylist = [myEmployee03, myEmployee04, myEmployee05,myEmployee06]

for ctr in mylist:
  try:
    ctr.giveRaise(.10)  # you can also use giveRaise(10)
  except TypeError:
    print('Cannot work with non-numeric values')
  except ValueError:
    print('Cannot compute raises for negative values')

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
SSN: 749-55-6296 
Salary: $3,000.00


testing the Employee.giveRaise method

Name: Teo Espero 
SSN: 749-55-6296 
Salary: $3,300.00


testing the Manager class

Name: Teo Espero 
SSN: 109-05-7228                         
Salary: $3,300.00 
Manager Title: IT Admin
Annual Bonus: $1,272.00


testing the Employee List Class

Name: Juanito Osorio 
SSN: 793-34-8331 
Salary: $1,100.00

Name: Annie Grefal 
SSN: 110-61-7163 
Salary: $1,650.00

Name: Josephine Ybanez 
SSN: 752-37-3516                         
Salary: $2,750.00 
Manager Title: Asst. IT Admin
Annual Bonus: $1,000.00

Name: Jeff Tuan 
SSN: 821-06-1293 
Salary: $1,925.00


Process finished with exit code 0
"""