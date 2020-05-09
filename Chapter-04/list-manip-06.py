# Numerical lists on Python

# BOF

# count 1 - 10
# note that this range is not created as a list
print('count 1 - 10')
for value in range(1, 11):
    print(value)

# create a list
number_list = list(range(1, 11))

# print the list
print('print the list')
print(number_list)

# create a list of even numbers
print('create a list of even numbers')
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# create a list of odd numbers
print('create a list of odd numbers')
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

# print squares of numbers
print('print squares of numbers')
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# EOF