def dance(hours):
      
  lst = [i*10 if i<9 else 80+(i-8)*15 for i in hours]
  return sum(lst + lst[-2:])

a=dance ([8, 10, 8, 8, 8, 1, 0])
print(a)