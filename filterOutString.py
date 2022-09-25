def filter_list(lst):
    
    return [i for i in lst if type(i) != str]

a=filter_list([1, 2, "aasf", "1", "123", 123])
print(a)

"""
Create a function that takes a list of non-negative integers 
and strings and return a new list without the strings.

"""