import math
def list_sum(lst):
    even = [i*i for i in lst if i % 2 == 0]
    odd = [math.sqrt(i) for i in lst if i % 2] 
    return round(sum(even+odd),2)
    #return round(sum(i ** .5 if i % 2 else i ** 2 for i in lst), 2)
a=list_sum([1, 3, 3, 1, 10])
print(a)
# Create a function that takes a list of numbers lst as an argument. 
# Square each number in the list if the number is even and square root 
# √ the number if it is odd. Return the sum of the new list rounded to 
# two decimal places.