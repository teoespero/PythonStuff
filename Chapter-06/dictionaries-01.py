# working with dictionaries in Python
# Teo Espero
# GIST I

# BOF

# define our basic dictionary
alien_0 = {
    'color': 'green',
    'points': 5
}

# print our dictionary
print('print our dictionary')
print(alien_0)

# print individual elements
print('print individual elements')
print(alien_0['color'])
print(alien_0['points'])

# add new items to the dictionary
print('add new items to the dictionary')
alien_0['x_position'] = 0
alien_0['y_position'] = 2
alien_0['speed'] = 'Fast'

# print the new dictionary
print('print the new dictionary')
print(alien_0)

# create another dictionary
print('create another dictionary')
alien_1 = {
    'color': 'red',
    'points': 10,
    'x_position': 1,
    'y_position': 26,
    'speed': 'Slow'
}

# show the other dictionary
print('show the other dictionary')
print(alien_1)

# EOF
