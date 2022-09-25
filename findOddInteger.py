def find_odd(lst):
   
     return [x for x in set(lst) if lst.count(x)%2!=0][0]

a=find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
print(a)