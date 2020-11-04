def is_harshad(n):

    return n%sum([int(i) for i in str(n)])==0

a=is_harshad(171)
print(a)