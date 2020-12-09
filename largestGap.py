def largest_gap(lst):

    lst=sorted(lst)
    return max([lst[i+1]-lst[i] for i in range(len(lst)-1)])

a=largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5])
print(a)
#return max(i-x for x, i in zip(sorted(lst), sorted(lst)[1:]))