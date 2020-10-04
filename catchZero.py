def catch_zero_division(expr):
    try:
        eval(expr)
    except ZeroDivisionError:
    
        return True 
    return False

a=catch_zero_division("4 / (2 + 3 - 4)")
print(a)