def prime_in_range(n1, n2):

    return any(all(n%x!=0 for x in range(2,n)) for n in range(n1,n2))
    

a=prime_in_range(10, 15)
print(a)