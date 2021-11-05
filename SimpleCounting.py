def count_digits(n, d):
    k=[str(i**2) for i in range(n +1)]
    return (''.join(k)).count(str(d))
    # ''.join(str(i**2) for i in range(n+1)).count(str(d))
a=count_digits(5750, 0)
print(a)