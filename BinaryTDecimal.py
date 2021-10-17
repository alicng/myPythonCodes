def binary_to_decimal(lst):

    return int(''.join([str(i) for i in lst]),2)

a=binary_to_decimal([0, 0, 1, 0])
print(a)