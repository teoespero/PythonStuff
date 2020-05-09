# Working with lists
# Teo Espero
# GIST I

# BOF

# initialize our vars
magicians = ['houdini', 'alice', 'david', 'carolina']

# print the original list
print('print the original list')
print(magicians)

# sort the list
print('sort the list')
magicians.sort()

# count how many are in the list
how_many_magicians = len(magicians)
magician_count = f'there are {how_many_magicians} magicians in the list.'

print(magician_count)

# print the magician names
for magician in magicians:
    magic_message = f'{magician.title()} is a great magician.'
    print(magic_message)
    print(f'{magician.title()} I look forward seeing your show.')

# EOF