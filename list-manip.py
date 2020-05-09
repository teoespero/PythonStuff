# This program is to illustrate how Python manipulates
# lists (changing, adding, and removing) elements
# Teo Espero
# GIST I

# BOF

# initialize vars
motorcycles = ['honda', 'yamaha', 'suzuki']

# print current values
print('Print current values')
print(motorcycles)

print('\n')

# change the first element of the list
print('Change the first element of the list')
motorcycles[0] = 'ducati'

# print the new values
print('Print the new values')
print(motorcycles)

print('\n')

# append an element to the list
motorcycles.append('honda')

# print the new values
print('Print the new values')
print(motorcycles)

print('\n')

# insert an element into the list
print('insert an element into the list')
motorcycles.insert(0, 'triumph')

# print the new values
print('Print the new values')
print(motorcycles)

print('\n')

# remove an element from the list
del motorcycles[0]

# print the new values
print('Print the new values')
print(motorcycles)

# EOF