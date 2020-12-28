def my_fact(n):
    
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

        
a=my_fact(5)
print(a)
