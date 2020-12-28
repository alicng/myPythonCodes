def largest_even(lst):

    even=[i for i in lst if i % 2 ==0]
    return -1 if len(even)==0 else (even)[-1]

a=largest_even([3, 7, 1, 7, 9, 10, 13])
print(a)