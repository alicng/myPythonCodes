def not_share(lst1, lst2):
     
    return not set(lst1) & set(lst2)

a=not_share([1, 2, 3], [4, 5, 6])
print(a)