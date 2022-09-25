def possible_path(lst):
    d=all(type(i) == int for i in lst[0::2])
    e=all(type (i) == str for i in lst[1::2])
    f=all(type(i) == str for i in lst[0::2])
    g=all(type (i) == int for i in lst[1::2])
    return True if d and e or f and g else False

a=possible_path([ "H", 2, 3, "H"])
print(a)
#return len(set(type(i) for i in lst[::2])) == 1