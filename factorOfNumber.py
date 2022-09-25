def find_factors(n):
    # n=str(n)
    return [i for i in range(1, n+1) if n % i == 0]

a=find_factors(12)
print(a)