############################
# import the objects (classes and methods that we need for the test file)
import employee
import manager
import random # because we want a randomized SSN

############################
# create instances for our Employee class
print('create instances for our Employee class\n')
myEmployee01 = employee.Employee('a','espero',random.randint(100000000,999999999),2000)
myEmployee02 = employee.Employee('b','espero',random.randint(100000000,999999999),3000)
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
print('\ncreate more instances for our Employee class\n')
myEmployee03 = employee.Employee('d','espero',random.randint(100000000,999999999),2000)
myEmployee04 = employee.Employee('c','ybanez',random.randint(100000000,999999999),3000)
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

print('\n-----------------------------------------------')

print('before sorting\n')
for ee in theEmployeeList:
    print(ee,'\n')

print('\n-----------------------------------------------')

############################
# sort the list, note that
# we did not specify a key

print('after sorting\n')

theEmployeeList.sort()
for ee in theEmployeeList:
    print(ee,'\n')




