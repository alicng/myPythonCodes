def is_disarium(n):

    return sum([int(i)**int(str(n).index(i)+1) for i in str(n)])==n

a=is_disarium(518)
print(a)