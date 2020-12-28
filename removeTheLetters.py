l = "abc"
def remove_abc(txt):
  w = "".join([i for i in txt if i not in l])
  return None if len(w)  == len(txt) else w

a=remove_abc("hello world! ")
print(a)

#(i for i in txt if i not in 'a,b,c' else 