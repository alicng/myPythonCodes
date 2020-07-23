from fractions import gcd
import re
def a(n):
	res = [i * '>' for i in range(1, n + 1)]
	return res + res[:-1][::-1] if n % 2 else res + res[::-1]

	        
a=a (4)
print(a)
