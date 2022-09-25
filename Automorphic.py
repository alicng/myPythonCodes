def automorphic(n):

    return (str(n*n))[-(len(str(n))):] == (str(n))       
   
    
a=automorphic(25)
print(a)

#A number is called Automorphic number if its square ends in the original 
# number. Create a function that takes a number n and returns True 
# if it is an Automorphic number, otherwise False.