def ascii_capitalize(txt):

    return ''.join(i.lower() if ord(i)% 2 else i.upper() for i in txt)

a=ascii_capitalize("to be or not to be!")
print(a)

#Create a function that takes a string as input 
# and capitalizes a letter if its ASCII code is 
# even and returns its lower case version if its 
# ASCII code is odd.