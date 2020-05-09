# More sorting lists in Python
# Teo Espero
# GIST I

# BOF

# initialize vars
alphabet = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
    'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
]

# print the current list
print('print the current list')
print(alphabet)

# sorting the list temporarily
print('sorting the list temporarily')
print(sorted(alphabet))
print('print the unsorted list')
print(alphabet)

# reverse the list
print('reverse the list')
alphabet.reverse()
print(alphabet)

# counting how many elements
print('counting how many elements')
elements_count = len(alphabet)
message = f'There are {elements_count} elements in the list.'
print(message)

# print each element
print('print each element')
for letter in alphabet:
    print(letter)

# EOF
