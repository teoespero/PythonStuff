# A list of dictionaries
# Teo Espero
# GIST I

# BOF

# define our list
alien_0 = {
    'color': 'green',
    'points': 5,
    'power': ['telepathy', 'time travel']
}

alien_1 = {
    'color': 'red',
    'points': 10
}

alien_2 = {
    'color': 'yellow',
    'points': 15,
    'power': ['invisibility', 'fly']
}

alien_3 = {
    'color': 'pink',
    'points': 20,
    'power': ['electricity', 'stop time']
}

# define our dictionary containing our list
print('define our dictionary containing our list')
aliens = [alien_0, alien_1, alien_2, alien_3]

# print our aliens
print('print our aliens')
print(f'Our dictionary has {len(aliens)} aliens.')
for alien in aliens:
    print(alien)

# add new items to the list
print('add new items to the list')
alien_0['speed'] = '100'
alien_1['speed'] = '200'
alien_2['speed'] = '300'
alien_3['speed'] = '400'

# print the new alien dictionary
for alien in aliens:
    print(alien)

# EOF
