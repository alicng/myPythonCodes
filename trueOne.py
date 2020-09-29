def integer_boolean(n):
    
    return [True if i=='1' else False for i in n]

a=integer_boolean("100101")
print(a)


#Create a function which returns a list of booleans, from a given number. 
# Iterating through the number one digit at a time, append 
# True if the digit is 1 and False if it is 0.