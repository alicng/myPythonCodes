def cap_to_front(s):
    u=[i for i in s if i.isupper()]
    sm=[i for i in s if i.islower()]
    return ''.join(u+sm)
    
    #return ''.join(sorted(s, key=str.isupper, reverse=True))

a=cap_to_front("shOrtCAKE")
print(a)

#Create a function that moves all capital letters to the front of a word.