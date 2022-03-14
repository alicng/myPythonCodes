def twins(lst):
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return i
a=twins([10, 20, 30, 5, 40, 50, 40, 15])
print(a)