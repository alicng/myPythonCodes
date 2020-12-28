def num_of_digits(num):


    return sum(1 for i in str(num)if i.isdigit())


a=num_of_digits(-1305981031)
print(a)

#in "1,2,3,4,5,6,7,8,9,0"