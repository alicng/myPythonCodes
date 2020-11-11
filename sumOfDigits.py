def is_equal(lst):

    return sum([int(i) for i in str(lst[0])])==sum([int(i) for i in str(lst[1])])

a=is_equal([105, 42])
print(a)
#return sum(map(int, str(lst[0]))) == sum(map(int, str(lst[1])))