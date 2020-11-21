def sum_odd_and_even(lst):
    even=sum([i for i in lst if i % 2 == 0])
    odd= sum([i for i in lst if i % 2])
    return [even, odd]
 
a=sum_odd_and_even([-1, -2, -3, -4, -5, -6])
print(a)
