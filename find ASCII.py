def counterpartCharCode(char):
    
    return ord((char).lower()) if char.isupper() else ord((char).upper())
    # return ord(char.swapcase())

a=counterpartCharCode('5')
print(a)