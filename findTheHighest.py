def find_highest(lst):
    h=0
    for i in lst:
        if h > i:
            i=h
        else:
            h=i
    return i

a=find_highest([-1, 3, 5, 6, 63, 12, 2])
print(a)