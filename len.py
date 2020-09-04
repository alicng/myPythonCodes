def length(s):
    
    return sum(s.count(i) for i in set(s))

a=length("Hello World")
print(a)