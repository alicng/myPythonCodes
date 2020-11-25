def binary_to_decimal(binary):

    return int(''.join(map(str, binary)),2)

a=binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0])
print(a)