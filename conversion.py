from fractions import gcd
import re
def a(n,b):
	for i in n:
		if 'kilos' in n:
			return int(''.join([i[0] for i in n.split(' ')[0]]))
		return round(int(''.join([i[0] for i in n.split(' ')[0]]))*0.453592)
	for i in b:
		if 'meter' in b:
			return int(''.join([i[0] for i in b.split(' ')[0]]))
		return round(int(''.join([i[0] for i in b.split(' ')[0]]))*0.0254)
	
		# r
	
         
a=a ("205 pounds", "73 inches")
print(a)
