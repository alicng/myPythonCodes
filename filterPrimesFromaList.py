def filter_primes(num):
    t=[i for i in range(2, max(num) + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]
    return [i for i in t if i in num]

a=filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097])
print(a)
#[n for n in num if n > 1 and all(n%i for i in range(2,int(n**0.5)+1))]