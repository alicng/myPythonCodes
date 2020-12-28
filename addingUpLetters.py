def add_letters(a):

    al = 'zabcdefghijklmnopqrstuvwxy'
    return al[sum(al.index(l) for l in a)%26]

a=add_letters(["x", "y", "z"])
print(a)
