# checking whether a value is in the list
# Teo Espero
# GIST I

# BOF

# create a list of toppings
toppings_list = [
    'mushrooms',
    'onions',
    'pineapple',
    'ham',
    'pepperoni'
]

# print the header
print('PIZZA!!! PIZZA!!!')

# get a topping from the customer
topping_request = input('What topping do you like? ')

# check if the topping is in the list
if topping_request == '':
    print('You need to choose a topping.')

    # bug the customer for a topping
    topping_request = input('What topping do you like? ')

    # check if its on the list
    if topping_request in toppings_list:
        print(f'{topping_request.title()} is in the list.')
elif topping_request in toppings_list:
    print(f'{topping_request.title()} is in the list.')
else:
    print(f'{topping_request.title()} is not in the list.')

# EOF
