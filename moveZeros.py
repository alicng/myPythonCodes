def move_zeros(lst):
    zero=[]
    nozero=[]
    for i in lst:
        if i == 0 and type(i) != bool:
            zero.append(i)
        elif type(i) == bool:
            nozero.append(i)    
        else:
            nozero.append(i)
    return nozero+zero
    #return sorted(lst, key=lambda x: x==0 and type(x) is not bool)
   

a=move_zeros([0,1,None,2,False,1,0])
print(a)