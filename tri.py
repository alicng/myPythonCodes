def is_triangle(a, b, c):
    d=a+b
	e=a+c
	f=b+c
	
	return True if d>c and e>b and f > a else False