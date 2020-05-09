# Using pop and remove for lists
# Teo Espero
# GIST I

# BOF

# initialize our vars
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# print the current list
print('print the current list')
print(motorcycles)

print('\n')

# pop e anlements from the list
print('pop an element from the list')

popped_italian = motorcycles.pop()

print('pop another element from the list')
popped_japanese = motorcycles.pop()

print('pop another element from the list')
popped_another_jap_bike = motorcycles.pop(0)

italian_bike = f'{popped_italian.title()} is an Italian bike.'
japanese_bike = f'{popped_japanese.title()} is a Japanese bike.'
another_jap_bike = f'{popped_another_jap_bike.title()} is another Japanese bike.'
print('\n')

# print the current list
print('print the current list')
print(motorcycles)
print(italian_bike)
print(japanese_bike)
print(another_jap_bike)

print('\n')

# pop the last element
print('pop the last element')
bike_i_will_buy = motorcycles.pop()

message = f'My bike will be a {bike_i_will_buy.title()}.'
print(message)

# print the current list
print('print the current list')
print(motorcycles)

# EOF
