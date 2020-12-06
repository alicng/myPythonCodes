def is_anti_list(lst1, lst2):

    return all(i != x for i,x in zip (lst1, lst2))if set(lst1) == set(lst2) else False

a=is_anti_list([3.14, True, 3.14], [3.14, False, 3.14])
print(a)