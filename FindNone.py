def find_none(lst):

    return lst.index(None) if None in lst else -1

a=find_none([1, 2, None])
print(a)