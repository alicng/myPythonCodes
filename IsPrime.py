def is_prime(num):
    if num > 1: 
      for i in range(2, num): 
        if (num % i) == 0: 
           return num, "is not a prime number"
        return num, "is a prime number"
    

user=int(input('enter a number: '))
a=is_prime(user)
print(a)