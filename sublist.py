def sublst(sl):
     
     return [sl[i:k]for i in range(len(sl) + 1) for k in range(i + 1, len(sl) + 1)]     
    
a=sublst([1,2,3])
print(a)