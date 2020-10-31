def how_many_missing(lst):


    return 0 if lst == [] else len([i for i in range(lst[0], lst[-1]+1)]) - len(lst)

a=how_many_missing([])
print(a)
#return lst[-1] - lst[0] + 1 - len(lst) if lst else 0