def find_difference(a, b):
    
    result1 = 1
    result2 = 1
    for x in a:
        result1 = result1 * x
    for y in b:
        result2 = result2 * y
    return result2 - result1
    


a=find_difference([ 1, 9, 25 ], [ 10, 7, 9 ])
print(a)
    