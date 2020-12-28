def letters_only(s):

    return False if len(s) == 0 else all([True if i.isalpha() and i.islower() else False for i in s.replace(' ','')])

a=letters_only("")
print(a)