def my_fact(n):
    
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product
#def factorial(num):
    # return 1 if num == 1 else num * factorial(num - 1)
        
a=my_fact(5)
print(a)
