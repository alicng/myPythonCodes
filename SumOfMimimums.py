def sum_minimums(lst):

    return sum([min(i) for i in lst])

a=sum_minimums([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]])
print(a)