def prime_fact(num):
	num1 = num
	i = 2
	prime_lst = []
	while i < num1:
		while num % i == 0:
			num = num/i
			prime_lst.append(i)
		i += 1
	return prime_lst

user=int(input('enter a number: '))
a=prime_fact(user)
print(a)