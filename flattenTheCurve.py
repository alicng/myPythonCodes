def flatten_the_curve(lst):
    mean=round(sum(lst) // len(lst),1)
    return [mean for i in lst]

a=flatten_the_curve([0, 0, 0, 2, 7, 3])
print(a)

#Given a list of integers, replace every number with the mean of all numbers.