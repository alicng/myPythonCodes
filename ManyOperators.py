def operate(num1, num2, operator):

    return eval('{}{}{}'.format(str(num1),operator,str(num2)))

a=operate(7, 10, "-")
print(a)