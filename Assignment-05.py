##################################################################################
# Assignment-05.py
# Teo Espero
# 20200518
# Objectives:
#       Create a new, reusable class
#       Develop a program to test the new class that is separate from the new class itself


# this allows us to use the objects and methods defined in the sandwich.py module
from sandwich import Sandwich

# the following tests are from the assignment page themselves

print('\n--------------------------------------')
print('Test data in the assignment')
print('--------------------------------------')
s = Sandwich("Bennie")
print (s)
print (s.price())
s.setBread("wheat")
print (s)
print (s.price())
s.setCheese("Cheddar")
print (s)
print (s.price())
s.setMeat("turkey")
print(s)
print (s.price())
s.addCondiment("mayo")
print (s)
print (s.price())
s.addCondiment("mustard")
print (s)
print (s.price())
s.addCondiment("lettuce")
print (s)
print (s.price())
s.setToasted(True)
print (s)
print (s.price())

### additional tests that i included
print('\n--------------------------------------')
print('additional tests with more condiments')
print('--------------------------------------')

s.addCondiment("catsup")
print (s)
print (s.price())
s.addCondiment("pickles")
print (s)
print (s.price())
s.addCondiment("sauerkraut")
print (s)
print (s.price())
s.setToasted(False)
print (s)
print (s.price())


print('\n------------------------------------------')
print('additional tests with a new object instance')
print('------------------------------------------')
sandwich02 = Sandwich("Teo")
sandwich02.addCondiment("mustard")
print (sandwich02)
print (sandwich02.price())
sandwich02.setMeat("turkey")
print(sandwich02)
print (sandwich02.price())
sandwich02.addCondiment("catsup")
print (sandwich02)
print (sandwich02.price())
sandwich02.addCondiment("sauerkraut")
print (sandwich02)
print (sandwich02.price())
sandwich02.setToasted(True)
print (sandwich02)
print (sandwich02.price())
sandwich02.setCheese("Provolone")
print (sandwich02)
print (sandwich02.price())
sandwich02.setBread("Flatbread")
print (sandwich02)
print (sandwich02.price())

## OUTPUT

"""
--------------------------------------
Test data in the assignment
--------------------------------------
Bennie: Not Toasted
4.5
Bennie: Wheat, Not Toasted
4.5
Bennie: Wheat, Cheddar, Not Toasted
4.5
Bennie: Wheat, Cheddar, Turkey, Not Toasted
5.5
Bennie: Wheat, Cheddar, Turkey, ['Mayo'], Not Toasted
5.5
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard'], Not Toasted
6.0
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard', 'Lettuce'], Not Toasted
6.5
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard', 'Lettuce'], Toasted
6.5

--------------------------------------
additional tests with more condiments
--------------------------------------
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard', 'Lettuce', 'Catsup'], Toasted
7.0
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard', 'Lettuce', 'Catsup', 'Pickles'], Toasted
7.5
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard', 'Lettuce', 'Catsup', 'Pickles', 'Sauerkraut'], Toasted
8.0
Bennie: Wheat, Cheddar, Turkey, ['Mayo', 'Mustard', 'Lettuce', 'Catsup', 'Pickles', 'Sauerkraut'], Not Toasted
8.0

------------------------------------------
additional tests with a new object instance
------------------------------------------
Teo: ['Mustard'], Not Toasted
4.5
Teo: Turkey, ['Mustard'], Not Toasted
5.5
Teo: Turkey, ['Mustard', 'Catsup'], Not Toasted
6.0
Teo: Turkey, ['Mustard', 'Catsup', 'Sauerkraut'], Not Toasted
6.5
Teo: Turkey, ['Mustard', 'Catsup', 'Sauerkraut'], Toasted
6.5
Teo: Provolone, Turkey, ['Mustard', 'Catsup', 'Sauerkraut'], Toasted
6.5
Teo: Flatbread, Provolone, Turkey, ['Mustard', 'Catsup', 'Sauerkraut'], Toasted
6.5

Process finished with exit code 0
"""