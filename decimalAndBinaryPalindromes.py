def palindrome_type(n):
    n=str(n)
    return "Decimal and binary." if n==n[::-1] and bin(int(n))[2:]==bin(int(n))[::-1][:-2] else 'Decimal only.' if n==n[::-1] else "Binary only." if bin(int(n))[2:]==bin(int(n))[::-1][:-2] else "Neither!" 

a=palindrome_type(427787)
print(a)
# 