def find_even_nums(num):
    
    return [i for i in range(1,num+1) if i%2 == 0]


a=find_even_nums(8)
print(a)