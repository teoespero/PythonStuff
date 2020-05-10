# Python and tuples
# Teo Espero
# GIST I

# BOF

# defining a Tuple
my_tuple = ('leonard', 'westbrook', 'davis', 'james', 'curry', 'harden')
print('defining a Tuple')
print(my_tuple)

# creating a list
my_list = []

# initialize the list from the Tuple
print('initialize the list from the Tuple')
ctr = 0
for element in my_tuple:
    my_list.insert(ctr, element.title())
    ctr = ctr + 1

# print the list
print('print the list')
print(my_list)

# sort the list
print('sort the list')
my_list.sort()

# print the sorted list
print('print the sorted list')
print(my_list)

# store the sorted list in the current Tuple
print('store the sorted list in the current Tuple')
my_tuple = my_list

# print the sorted tuple
print('print the sorted tuple')
print(my_tuple)

# EOF
