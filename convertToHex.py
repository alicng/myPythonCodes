def convert_to_hex(txt):
    
    return ' '.join(hex(ord(i))[2:] for i in txt)

a=convert_to_hex("hello world")
print(a)