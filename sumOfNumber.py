def numbers_sum(lst):


    return sum([i for i in lst if type(i)==int])

a=numbers_sum([1, 2, "13", "4", "645"])
print(a)
#lst if type(lst)==<class 'int'> else 0