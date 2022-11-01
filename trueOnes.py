def integer_boolean(n):
    
    return [True if i == '1' else False for i in n]

a=integer_boolean("100101")
print(a)