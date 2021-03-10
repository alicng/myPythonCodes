def moving_partition(lst):

    return [[lst[:i],lst[i:]] for i in range(1,len(lst))]

a=moving_partition([1, 2, 3, 4, 5])
print(a)