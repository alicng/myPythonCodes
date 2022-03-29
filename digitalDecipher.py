def digital_decipher(eMessage, key):
    
    return "".join([chr(eMessage[i] + 96 - int((str(key) * (i+1))[i])) for i in range(len(eMessage))])

a=digital_decipher([20, 12, 18, 30, 21], 1939)
print(a)