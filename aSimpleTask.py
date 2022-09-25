def decimal_part(n):
    
    return 0 if type(n) == int else float('0.{}'.format(str(n).split('.')[1]))

a=decimal_part(-12.315346346)
print(a)