# Looping through dictionaries
# Teo Espero
# GIST I

# BOF

# define our user list
users_0 = {
    'username': 'teospero',
    'first name': 'teo',
    'last name': 'espero'
}

for field, value in users_0.items():
    print(f'\nKey: {field.title()}')
    if field == 'username':
        print(f'Value: {value}')
    else:
        print(f'Value: {value.title()}')

# EOF
