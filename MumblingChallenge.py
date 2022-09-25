def mumbling(s):
    s=' '+s
    #return '-'.join([str(i*s.index(i)).title() for i in s[1:]])
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

a=mumbling("maTT")
print(a)

#"A-Ii-Rrr-Ffff-Ooooo-Rrrrrr-Ccccccc-Eeeeeeee"