def add_parity_bit(b):

    return b+'1' if b.count('1') % 2 != 0 else b+'0'

a=add_parity_bit("0010110")
print(a)

#If a binary string has an odd number of 1s, the parity bit is a 1.
#If a binary string has an even number of 1s, the parity bit is a 0.
#The parity bit is appended to the end of the binary string.
#return b + ['0', '1'][b.count('1') % 2]