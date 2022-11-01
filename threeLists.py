def sum_common(lst1, lst2, lst3):
     
    return sum(i for i in lst1 if i in lst2 and i in lst3)

a=sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2])
print(a)