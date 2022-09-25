def add_str_nums(num1, num2):
  
    num1, num2 = '0' + num1, '0' + num2
    return str(int(num1) + int(num2)) if num1.isdigit() and num2.isdigit() else '-1'

a=add_str_nums("1","")
print(a)