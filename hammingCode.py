def hamming_code(message):

    return ''.join([i*3 for i in ''.join([bin(x)[2:].zfill(8) for x in [ord(i) for i in message]])])

a=hamming_code("3")
print(a)
