# python using lists
# teo espero
# GIST I

# BOF

# initialize our vars
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# this will print everything on the list
print('this will print everything on the list')
print(bicycles)

print('\n')

# this prints the items on the list
# list_var[0]...list_var[n]
print('Print the list')
print(bicycles[0], bicycles[0].title())
print(bicycles[1], bicycles[1].title())
print(bicycles[2], bicycles[2].title())
print(bicycles[3], bicycles[3].title())

print('\n')
# printing in reverse
print('Print the list in reverse')
print(bicycles[-1], bicycles[-1].title())
print(bicycles[-2], bicycles[-2].title())
print(bicycles[-3], bicycles[-3].title())
print(bicycles[-4], bicycles[-4].title())

print('\n')
# using strings and lists
message = f'My first bike was a {bicycles[1].title()}.'

print('using strings and lists')
print(message)

# EOF
