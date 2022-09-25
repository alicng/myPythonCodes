def reverse(txt):
    
    return txt[::-1].swapcase()
    #return ''.join([i.lower() if i==i.upper() else i.upper() for i in txt])[::-1]
a=reverse("Hello World")
print(a)

"""
    The "Reverser" takes a string as input and 
    returns that string in reverse order, with the opposite case.
"""