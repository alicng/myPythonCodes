def digital_cipher(message, key):

    s=list(map(int,str(key)))
    t=len(s)
    return [ord(x)-96+s[i%t] for i,x in enumerate(message)]

a=digital_cipher("mubashir", 1990)
print(a)