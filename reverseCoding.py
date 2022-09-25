def mystery_func(txt):
    h=[i for i in txt if i.isalpha()]
    r=[i for i in txt if i.isdigit()]
    return ''.join([i*int(j) for i,j in zip(h,r) ])
    #return ''.join([x*int(y) for (x,y) in zip(txt[::2],txt[1::2])])
    #return ''.join([txt[i]*int(txt[i+1]) for i in range(0,len(txt),2)])
a=mystery_func("A4B5C2")
print(a)