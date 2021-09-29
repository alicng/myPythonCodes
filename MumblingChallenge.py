def mumbling(s):
    s=' '+s
    return '-'.join([str(i*s.index(i)).title() for i in s[1:]])
    #

a=mumbling("maTT")
print(a)

#"A-Ii-Rrr-Ffff-Ooooo-Rrrrrr-Ccccccc-Eeeeeeee"