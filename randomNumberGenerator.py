from random import sample

def numbers():
	return int(''.join(sample('12345', 5)))

a=numbers()
print(a)
'''
from random import shuffle
def numbers():
	arr = ['1','2','3','4','5']
	shuffle(arr)
	return int(''.join(arr))
'''