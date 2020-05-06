# this program is used to illustrate both
# the rstrip and lstrip functions


# intialize our vars

# note that the first string has spaces on both ends
myPersonalMessage = '     This is my first message       '

# concat our names
myFirstName = 'teo'
myLastName = 'espero'

myFullName = myFirstName.title() +' '+myLastName.title()

# combine our message and our name
myFullMessage = myPersonalMessage + myFullName

# show original content
print(myFullMessage)

# strip the whitespaces on the left
myPersonalMessage = myPersonalMessage.lstrip()

# re-concat our message
myFullMessage = myPersonalMessage + myFullName

# show message without the spaces on the left
print(myFullMessage)

# strip the whitespaces on the right
myPersonalMessage = myPersonalMessage.rstrip()

# re-concat our message
myFullMessage = myPersonalMessage + myFullName

# show message without the spaces on the right
print(myFullMessage)

# re-concat our message
myFullMessage = myPersonalMessage + ' '+ myFullName

# show message with proper spacing
print(myFullMessage)

# EOF