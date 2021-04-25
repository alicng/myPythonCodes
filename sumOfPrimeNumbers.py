def sum_primes(lst):

    plist=[]
    for i in lst:
        c=0
        for j in range (1,i):
            if i%j==0:
                c+=1
        if c==1:
            plist.append(i)
    if len(plist) == 0:
        return None
    return sum(plist)

a=sum_primes([3,5,7,8])
print(a)