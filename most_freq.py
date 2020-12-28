def most_freq(n):
    
   return max(set(n), key = n.count)
    

a=most_freq([1,2,3,3,3,3,4,4,5,5])
print(a)