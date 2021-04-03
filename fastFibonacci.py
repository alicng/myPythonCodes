def fib_fast(num):
    prev, cur = (0, 1)
    for i in range(2, num+1):
    	prev, cur= (cur, prev + cur)
    return cur
            

a=fib_fast(10)
print(a)