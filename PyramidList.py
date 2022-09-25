def pyramid_lists(n):

    return [[i]*i for i in range(1,n+1)]

a=pyramid_lists(3)
print(a)
# Given a number n, return a list containing several lists. 
# Each list increment in size, from range 1 to n inclusive, 
# contaning its length as the elements