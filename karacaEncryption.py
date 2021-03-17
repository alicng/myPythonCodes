def encrypt(word):

    d={'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'}
    return ''.join(d[i] if i in d else i for i in word[::-1]) +'aca'

a=encrypt("London")
print(a)