def consonants(word):

    return len([i for i in word.lower() if i.isalpha() and i not in "a,e,i,o,u" ])

a=consonants('He|\o mY Fr*End')
print(a)