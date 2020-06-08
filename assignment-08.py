"""
import the objects (classes and methods that we need for the test file)
"""
import employee
import manager
import random

############################
# create instances for our Employee class
print('-----------------------------------------------')
print('create instances for our Employee class\n')
myEmployee01 = employee.Employee('a','Espero',random.randint(100000000,999999999),2000)
myEmployee02 = employee.Employee('A','espero',random.randint(100000000,999999999),3000)
print(myEmployee01,'\n')
print(myEmployee02,'\n')

############################
# call the magic methods
print('call the magic methods')
print('__eq__ test -->', myEmployee01 == myEmployee02)
print ('__lt__ test -->', myEmployee01 < myEmployee02)

print('\n-----------------------------------------------')

############################
# create more instances for our Employee class
print('create more instances for our Employee class\n')
myEmployee03 = employee.Employee('d','espero',random.randint(100000000,999999999),2000)
myEmployee04 = manager.Manager('c','ybanez',random.randint(100000000,999999999),3000,'customer service supervisor', 500)
print(myEmployee03,'\n')
print(myEmployee04,'\n')

############################
# call the magic methods again
print('call the magic methods again')
print('__eq__ test -->', myEmployee03 == myEmployee04)
print ('__lt__ test -->', myEmployee03 < myEmployee04)

print('\n-----------------------------------------------')

############################
# create a list of employees
print('create a list of employees\n')

employee01 = manager.Manager('keith','van der maaten',random.randint(100000000,999999999),4000,'general manager',1000)
employee02 = employee.Employee('paula','riso',random.randint(100000000,999999999),2100)
employee03 = manager.Manager('kelly','cadiente',random.randint(100000000,999999999),2200, 'admin director',1000)
employee04 = employee.Employee('teo','espero',random.randint(100000000,999999999),2300)
employee05 = employee.Employee('derek','cray',random.randint(100000000,999999999),2400)
employee06 = employee.Employee('rose','gill',random.randint(100000000,999999999),2600)
employee07 = manager.Manager('tamela','hatfield',random.randint(100000000,999999999),2600, 'acctg supervisor',1000)

theEmployeeList = [employee01, employee02, employee03, employee04, employee05, employee06, employee07]

print('-----------------------------------------------')

print('before sorting\n')
for ee in theEmployeeList:
    print(ee,'\n')

print('-----------------------------------------------')

############################
# sort the list, note that
# we did not specify a key

print('after sorting\n')

theEmployeeList.sort()
for ee in theEmployeeList:
    print(ee,'\n')

print('-----------------------------------------------')
###############################

###############################
#OUTPUT

"""
-----------------------------------------------
create instances for our Employee class

Name: A Espero 
SSN: 712-65-1172 
Salary: $2,000.00 

Name: B Espero 
SSN: 217-98-9067 
Salary: $3,000.00 

call the magic methods
__eq__ test --> False
__lt__ test --> True

-----------------------------------------------
create more instances for our Employee class

Name: D Espero 
SSN: 648-52-1499 
Salary: $2,000.00 

Name: C Ybanez 
SSN: 441-65-7831                         
Salary: $3,000.00 
Manager Title: Customer Service Supervisor
Annual Bonus: $500.00 

call the magic methods again
__eq__ test --> False
__lt__ test --> True

-----------------------------------------------
create a list of employees

-----------------------------------------------
before sorting

Name: Keith Van Der Maaten 
SSN: 214-02-0888                         
Salary: $4,000.00 
Manager Title: General Manager
Annual Bonus: $1,000.00 

Name: Paula Riso 
SSN: 276-99-2673 
Salary: $2,100.00 

Name: Kelly Cadiente 
SSN: 819-05-7351                         
Salary: $2,200.00 
Manager Title: Admin Director
Annual Bonus: $1,000.00 

Name: Teo Espero 
SSN: 343-26-5726 
Salary: $2,300.00 

Name: Derek Cray 
SSN: 946-16-2463 
Salary: $2,400.00 

Name: Rose Gill 
SSN: 723-94-0612 
Salary: $2,600.00 

Name: Tamela Hatfield 
SSN: 203-55-9270                         
Salary: $2,600.00 
Manager Title: Acctg Supervisor
Annual Bonus: $1,000.00 

-----------------------------------------------
after sorting

Name: Kelly Cadiente 
SSN: 819-05-7351                         
Salary: $2,200.00 
Manager Title: Admin Director
Annual Bonus: $1,000.00 

Name: Derek Cray 
SSN: 946-16-2463 
Salary: $2,400.00 

Name: Teo Espero 
SSN: 343-26-5726 
Salary: $2,300.00 

Name: Rose Gill 
SSN: 723-94-0612 
Salary: $2,600.00 

Name: Tamela Hatfield 
SSN: 203-55-9270                         
Salary: $2,600.00 
Manager Title: Acctg Supervisor
Annual Bonus: $1,000.00 

Name: Paula Riso 
SSN: 276-99-2673 
Salary: $2,100.00 

Name: Keith Van Der Maaten 
SSN: 214-02-0888                         
Salary: $4,000.00 
Manager Title: General Manager
Annual Bonus: $1,000.00 

-----------------------------------------------
"""
###############################