def leader(lst):

    return [lst[i] for i in range(len(lst)) if lst[i] == max(lst[i:])]

a=leader([8, 7, 1, 2, 10, 3, 5])
print(a)
# if lst[i]>lst[i:]