import random 
def ranpass(a):
  
    num=random.randint(1000,9999)
    letter=(''.join([random.choice(a) for _ in range(3)]))
    return letter+str(num)

user=input('enter your name :')
a=ranpass(user)
print(a)