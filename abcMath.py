def abcmath(a, b, c):

    return a*(2**b) % c == 0

a=abcmath(42, 5, 10)
print(a)