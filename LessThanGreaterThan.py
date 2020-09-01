def list_between(num1, num2, lst):

    return [ i for i in lst if num1< i < num2]

a=list_between(3, 8, [1, 5, 95, 0, 4, 7])
print(a)