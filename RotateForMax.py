def rotate_max_number(num):
    num=sorted(str(num))
    return ''.join(sorted(num, reverse=True))
    

a=rotate_max_number('001')
print(a)
