def min_miss_pos(lst):
    a=[i for i in range(min(lst), max(lst)+1) if i > 0]
    b=[i for i in sorted(lst) if i > 0]
    c=[str(i) for i in a if i not in b]
    return 1 if len(b) is 0 else max(b)+1 if len(c) is 0 else int(''.join(min([str(i) for i in a if i not in b])))

a=min_miss_pos([7, 6, 5, 4, 3, 2, 1, ])
print(a)
# return min(set(range(1, max(lst)+2))-set(lst))