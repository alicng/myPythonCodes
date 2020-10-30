def war_of_numbers(lst):
    odd=sum([i for i in lst if i % 2])
    even=sum([i for i in lst if i % 2==0])
    return abs(odd-even)


a=war_of_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)