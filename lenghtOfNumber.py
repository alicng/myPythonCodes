def number_length(num):

    count = 0
    num=str(num).replace('-','')
    for i in str(num): 
        count+= 1
    return count

a=number_length(-654321)
print(a)
#return sum(1 for i in str(num))