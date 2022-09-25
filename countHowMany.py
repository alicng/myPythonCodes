def count_repetitions(lst):

    return {i: (lst.count(i)) for  i in set(lst)}

a=count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"])
print(a)
#