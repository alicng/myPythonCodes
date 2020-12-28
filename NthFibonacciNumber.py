def fibonacci(n):
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return str(a)

a=fibonacci(10)
print(a)