def list_operation(x, y, n):


    return [i for i in range (x, y+1) if i % n ==0]

a=list_operation(1, 10, 3)
print(a)
#list(filter(lambda a:a%n==0,range(x,y+1)))