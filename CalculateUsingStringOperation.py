def calculate(num1, num2, op):
    op=op.replace("","")
    num1=str(num1)
    num2=str(num2)
    
    return eval(num1+op+num2)

a=calculate(4, 9, "+")
print(a)