def clone(lst):
    l=lst.copy()
    lst.append(l)
    return lst

a=clone([1, 2, 3])
print(a)
#lst.append(lst[:])