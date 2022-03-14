def little_big(n):
    
    return 5 + n//2 if n % 2 else 50 * 2**(n//2)

a=little_big(8)
print(a)
# 5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200, ...