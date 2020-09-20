def evenly_divisible(a, b, c):

    return  0 if a < c and b < c else sum([i for i in range(0,b+1,c)]) if b > c else sum([i for i in range(0,a+1,c)])

a=evenly_divisible(10, 1, 2)
print(a)

