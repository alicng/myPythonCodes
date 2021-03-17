def consecutive_combo(lst1, lst2):
    s=sorted(lst1+lst2)
    return s==[i for i in range(min(s), max(s)+1)]

a=consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])
print(a)

