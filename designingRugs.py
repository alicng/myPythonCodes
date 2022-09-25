def make_rug(m, n, s="#"):
    
    return [s*n for i in range(m)]

a=make_rug(3, 5, '#')
print(a)