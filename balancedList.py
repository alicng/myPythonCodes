def balanced(lst):
    one=(lst[0:(len(lst)//2)])
    two=(lst[(len(lst)//2):])
    return  one+one if sum(one) > sum(two) else lst if sum(one) == sum(two) else two + two

a=balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6])
print(a)