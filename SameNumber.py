def same(a1, a2):

    return len(set(a1))==len(set(a2))

a=same([2], [3, 3, 3, 3, 3])
print(a)