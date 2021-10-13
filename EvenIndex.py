def even_last(lst):

    return 0 if len(lst)==0 else sum([i for i in lst[0::2]])*lst[-1]

a=even_last([1, 3, 3, 1, 10])
print(a)