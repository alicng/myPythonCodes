def cars_needed(n):

    return (n//5)+1 if n%5!=0 else n//5

a=cars_needed(11)
print(a)