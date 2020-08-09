def a(n,b,c):

     return c.join(n[i:i+b] for i in range(0, len(n),3))

a=a("magnify", 3, ":")
print(a)
