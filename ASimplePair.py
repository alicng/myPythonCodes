def simple_pair(lst, n):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]*lst[j]==n:
                return [lst[i],lst[j]]
    return None
# Given an array of integers lst and an integer n, 
# find out a pair of numbers [x, y] from a given array 
# such that x * y = n .
#If the pair is not found, return None.
a=simple_pair([1, 2, 3], 6)
print(a)