def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a=gcd(10, 20)
print(a)