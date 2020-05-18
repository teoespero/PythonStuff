message = 'Hello'

yourName = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)


if age >= 18:
    additionalMsg = 'You are old enough to drive.'
else:
    additionalMsg = 'You are too young to drive.'
print(f'Hello {yourName.title()}, you are {age} years old. ' + additionalMsg)