def a(n, b):

      return [n[i:i+b] for i in range(len(n))]


a=a([3, 2, 1, 1, 3, 2], 4)
print(a)