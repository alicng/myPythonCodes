def XO(txt):
    
    return txt.upper().count('O') == txt.upper().count('X') 
    
a=XO("oox")
print(a)

"""    
    Return a boolean value (True or False).
    Return True if the amount of x's and o's are the same.
    Return False if they aren't the same amount.
    The string can contain any character.
    When "x" and "o" are not in the string, return True.
"""