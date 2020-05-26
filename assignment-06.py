from rectangle import Rectangle

########################################################
# valid values
########################################################
r = Rectangle()
print(r)
r.setData(3, 4)
print (r)
print (r.area())

########################################################
# test the methods with invalid values
########################################################

rec_01 = Rectangle()
try:
    rec_01.setData("3", "error")
except ValueError:
    print ("can't set the Rectangle to a negative value")
except TypeError:
    print ("can't set the Rectangle to a non-integer value")
print(rec_01)
print (rec_01.area())

########################################################
# test the methods with string values
########################################################

rec_01 = Rectangle()
try:
    rec_01.setData("3", "error")
except ValueError:
    print ("Can't set the Rectangle to a negative value")
except TypeError:
    print ("Can't set the Rectangle to a non-integer value")
print(rec_01)
print (rec_01.area())

########################################################
# test the methods with a value less than 0
########################################################
rec_02 = Rectangle()
try:
    rec_02.setData(-3, 5)
except ValueError:
    print ("Can't set the Rectangle to a negative value")
except TypeError:
    print ("Can't set the Rectangle to a non-integer value")
print(rec_02)
print (rec_02.area())

rec_03 = Rectangle()
try:
    rec_03.setData(3, -5)
except ValueError:
    print ("Can't set the Rectangle to a negative value")
except TypeError:
    print ("Can't set the Rectangle to a non-integer value")
print(rec_03)
print (rec_03.area())

########################################################
# test the methods with a value modified at runtime
########################################################

rec_04 = Rectangle()
try:
    rec_04.setData(int("3"), abs(-5))
except ValueError:
    print ("Can't set the Rectangle to a negative value")
except TypeError:
    print ("Can't set the Rectangle to a non-integer value")
print(rec_04)
print (rec_04.area())

########################################################
# OUTPUT
########################################################

"""
height = 0, and width = 0
height = 3, and width = 4
12
can't set the Rectangle to a non-integer value
height = 0, and width = 0
0
Can't set the Rectangle to a non-integer value
height = 0, and width = 0
0
Can't set the Rectangle to a negative value
height = 0, and width = 0
0
Can't set the Rectangle to a negative value
height = 0, and width = 0
0
height = 3, and width = 5
15

Process finished with exit code 0
"""