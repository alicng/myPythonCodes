def a(n):
    t=max([n[i+1]-n[i] for i in range(len(n)-1)])
    ave=(max(n)-min(n))/(len(n))
    return [n[i]+ave for i in range(len(n)-1)if (n[i+1]-n[i])==t]
     
a=a([2, 4, 6, 8, 10, 14, 16])
print(a)
