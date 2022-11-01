def return_only_integer(lst):
    
    return [i for i in lst if type(i) == int ]

a=return_only_integer([9, 2, "space", "car", "lion", 16])
print(a)