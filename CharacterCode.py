def calc(s):
    n = ''.join([str(ord(i)) for i in s])
    n1 = n.replace('7','1')
    n,n1 = sum(map(int,n)),sum(map(int,n1))
    return n-n1

a=calc("ABCDabcd")
print(a)