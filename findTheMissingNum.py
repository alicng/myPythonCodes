def missing_num(lst):

    #return sum(range(1,11))-sum(lst)
    return [x for x in [1,2,3,4,5,6,7,8,9,10] if x not in lst][0]


a=missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])
print(a)