def sum_missing_numbers(lst):
    
    return sum([i for i in range(min(lst), max(lst)+1) if i not in lst])

a=sum_missing_numbers([1, 2, 3, 4, 5])
print(a)
'''
Create a function that returns the sum of missing numbers from the given list.
Examples
sum_missing_numbers([4, 3, 8, 1, 2]) ➞ 18
# 5 + 6 + 7 = 18
'''