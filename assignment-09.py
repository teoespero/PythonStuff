import string
import ast
from sandwich import Sandwich
from order import Order


############################
def createFile(itemOrder):
    # Opens filename for reading and makes a copy of it in a new file named 'dataCopy.txt'.

    file = open('sandwichObject.txt', 'w')
    file.write(str(itemOrder))
    file.close()

############################

############################
def readFile():
    # Opens filename for reading and makes a copy of it in a new file named 'dataCopy.txt'.

    file = open('sandwichObject.txt', 'r')
    file_contents = file.read()
    file.close()
    return file_contents
    ############################


print('\n----------------------------------------------')
############################
# Test data from assignment

# 1st Order, 1st sandwich
print('Test data from assignment:')
s1 = Sandwich("Joe")
s1.setMeat("steak")
s1.addCondiment("Lettuce")
print (s1)

############################
# store Order1 as a Pickle file

myDict = {}
for attr, value in s1.__dict__.items():
        myDict[attr] = value

createFile(myDict)


# 1st Order, 2nd sandwich
s2 = Sandwich("Mary")
s2.setCheese("cheddar")
s2.addCondiment("Mayo")
print (s2)

order1 = Order()
try:
    print(order1)
except ValueError:
    print('No sandwiches in the order.')
order1.addSandwich(s1)

print ("Total Price:"+ str(order1.price()))
order1.addSandwich(s2)
print (order1)
print ("Total Price:" + str(order1.price()))

print('\n----------------------------------------------')

############################
# Test data by creating another order
print('Test data by creating another order:')
order2 = Order()
try:
    print(order2)
except ValueError:
    print('No sandwiches in the order.')

# 2nd Order, 1st sandwich
s3 = Sandwich("Teo")
s3.setCheese("Pepperjack")
s3.setMeat('Ham')
s3.addCondiment("Mayo")
s3.addCondiment("Mustard")
s3.addCondiment("Catsup")
s3.setBread('Flatbread')
s3.setToasted(True)
s3.addCondiment("Lettuce")
print (s3)
order2.addSandwich(s3)

myDict = {}
for attr, value in s1.__dict__.items():
        myDict[attr] = value

createFile(myDict)

# 2nd Order, 2nd sandwich
s4 = Sandwich("Josie")
s4.setCheese("Pepperjack")
s4.setMeat('Turkey')
s4.addCondiment("Mayo")
s4.addCondiment("Mustard")
s4.addCondiment("Sauerkraut")
s4.addCondiment("Catsup")
s4.setBread('Wheat')
s4.setToasted(True)
s4.addCondiment("Lettuce")
print (s4)
order2.addSandwich(s4)

print (order2)
print ("Total Price:" + str(order2.price()))

print('\n----------------------------------------------')

############################
# Create a new Sandwich object from a Pickle file
print('Create a new Sandwich object from a Pickle file')
myStr = readFile()
print(f'File contents "{myStr}"')
myStr = myStr.replace('[','')
myStr = myStr.replace(']','')

print('\n----------------------------------------------')

############################
# A string can be converted to a dictionary if the string contains a dictionary expression. For example,
# the string '{"a": 1, "b": 2}' can be converted to a dictionary.

print('converting it to a dictionary')
newDict = ast.literal_eval(myStr)
print(newDict)
print(type(newDict))

print('\n----------------------------------------------')

############################
#creating the new Sandwich object
print('creating the new Sandwich object')
s5 = Sandwich(newDict['name'])
s5.setCheese(newDict['cheeseName'])
s5.setMeat(newDict['meatName'])
s5.addCondiment(newDict['condiments'])
s5.setToasted(newDict['toasted'])

print(s5)

print('\n----------------------------------------------')

############################
# Create a new Order object
print('creating a new Order object')
order3 = Order()
order3.addSandwich(s5)
print(order3)
print ("Total Price:" + str(order3.price()))

print('\n----------------------------------------------')


##############################
# OUTPUT

"""
----------------------------------------------
Test data from assignment:

Joe: steak, ['Lettuce'], not toasted
Mary: cheddar, ['Mayo'], not toasted
No sandwiches in the order.
Sandwich 1:Joe: steak, ['Lettuce'], not toasted
Total Price:5.5
Sandwich 1:Joe: steak, ['Lettuce'], not toasted
Sandwich 2:Mary: cheddar, ['Mayo'], not toasted
Total Price:10.0

----------------------------------------------
Test data by creating another order:

No sandwiches in the order.
Teo: Flatbread, Pepperjack, Ham, ['Mayo', 'Mustard', 'Catsup', 'Lettuce'], toasted
Josie: Wheat, Pepperjack, Turkey, ['Mayo', 'Mustard', 'Sauerkraut', 'Catsup', 'Lettuce'], toasted
Sandwich 1:Teo: Flatbread, Pepperjack, Ham, ['Mayo', 'Mustard', 'Catsup', 'Lettuce'], toasted
Sandwich 2:Josie: Wheat, Pepperjack, Turkey, ['Mayo', 'Mustard', 'Sauerkraut', 'Catsup', 'Lettuce'], toasted
Total Price:14.5

----------------------------------------------
Create a new object from a Pickle file
File contents "{'name': 'Joe', 'breadName': None, 'cheeseName': None, 'meatName': 'steak', 'condiments': ['Lettuce'], 'toasted': False}"

----------------------------------------------
converting it to a dictionary
{'name': 'Joe', 'breadName': None, 'cheeseName': None, 'meatName': 'steak', 'condiments': 'Lettuce', 'toasted': False}
<class 'dict'>

----------------------------------------------
creating the new Sandwich object
Joe: steak, ['Lettuce'], not toasted

----------------------------------------------
creating a new Order object
Sandwich 1:Joe: steak, ['Lettuce'], not toasted
Total Price:5.5
"""